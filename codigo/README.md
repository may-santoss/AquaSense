# Código - AquaSense

Este diretório contém o código principal do projeto.

### Estrutura
- Conexão Wi-Fi
- Conexão MQTT
- Leitura de sensores (pH e turbidez)
- Simulação de variação natural dos dados
- Publicação no broker MQTT

### Principais bibliotecas:
- `machine` – controle de pinos e ADC
- `urandom` – variações simuladas
- `umqtt.simple` – envio via MQTT
