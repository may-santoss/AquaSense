# Projeto AquaSense 🌊💡

Este projeto tem como objetivo monitorar em tempo real a qualidade da água utilizando sensores de pH e turbidez, com envio dos dados para um broker MQTT via protocolo TCP/IP. Foi desenvolvido utilizando o microcontrolador ESP32 na plataforma de simulação Wokwi.

## Como funciona
- Lê dados dos sensores de pH e turbidez.
- Adiciona variações randômicas para simular comportamento real.
- Conecta-se via Wi-Fi e envia os dados para o tópico MQTT `aquaSense/data` no broker público HiveMQ.

## Como executar
1. Suba o código no ESP32 usando a plataforma Wokwi (https://wokwi.com/)
2. Configure o Wi-Fi como "Wokwi-GUEST"
3. Observe os dados publicados no terminal (mensagens não visualizáveis no painel HiveMQ)

---
