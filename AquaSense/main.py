import machine
import onewire
import ds18x20
import time
import network
import ubinascii
import urandom
from umqtt.simple import MQTTClient
from machine import Pin, ADC

# --------- Configurações Wi-Fi ---------
SSID = "Wokwi-GUEST"
PASSWORD = ""

# --------- Configurações MQTT ---------
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "aquaSense/dados"
CLIENT_ID = ubinascii.hexlify(machine.unique_id())

# --------- Conecta ao Wi-Fi ---------
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    print("Conectando-se ao Wi-Fi", end="")
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)
    print("\nConectado ao Wi-Fi:", wlan.ifconfig())

connect_wifi()

# --------- Conecta ao Broker MQTT ---------
client = MQTTClient(CLIENT_ID, MQTT_BROKER, port=MQTT_PORT)
client.connect()
print("Conectado ao broker MQTT")

# --------- Sensores ---------
dat = Pin(4)  # DS18B20
ds_sensor = ds18x20.DS18X20(onewire.OneWire(dat))
roms = ds_sensor.scan()

ph_sensor = ADC(Pin(34))  # pH
ph_sensor.atten(ADC.ATTN_11DB)

turbidity_sensor = ADC(Pin(35))  # turbidez
turbidity_sensor.atten(ADC.ATTN_11DB)

# --------- Loop principal ---------
while True:
    ds_sensor.convert_temp()
    time.sleep_ms(750)

    # Leitura do pH com variação aleatória
    ph_value = ph_sensor.read()
    ph_variation = (urandom.getrandbits(3) - 4) * 0.1  # variação de -0.4 a +0.3
    ph = ((ph_value / 4095) * 14) + ph_variation
    ph = max(0, min(ph, 14))  # limita entre 0 e 14

    # Leitura da turbidez com variação aleatória
    turbidity_value = turbidity_sensor.read()
    turb_variation = urandom.getrandbits(8) % 200 - 100  # variação de -100 a +99
    turbidity_value = min(max(turbidity_value + turb_variation, 0), 4095)
    turbidity = (turbidity_value / 4095) * 100

    # Cria o payload
    payload = '{{ "pH": {:.2f}, "turbidity": {:.2f} }}'.format(ph, turbidity)
    print("Publicando:", payload)

     # Envia os dados ao broker
    client.publish(MQTT_TOPIC, payload)
   

    time.sleep(5)
