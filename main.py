import network
import socket
import json
from time import sleep
from machine import Pin
import dht

# Wi-Fi credentials
ssid = 'Rudra'
password = '12345678'

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
print("Connecting to Wi-Fi...", end="")
while not wlan.isconnected():
    sleep(1)
print("\nConnected. IP:", wlan.ifconfig()[0])

# Setup DHT sensor and onboard LED (Pin 2 on Pico W)
sensor = dht.DHT22(Pin(15))
led = Pin("LED", Pin.OUT)

# Setup socket server
addr = socket.getaddrinfo('0.0.0.0', 8081)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print("Listening on", addr)

while True:
    cl, addr = s.accept()
    print('Client connected from', addr)
    request = cl.recv(1024)
    print("Request:", request)

    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print(f"Updated Temp: {temp}°C | Humidity: {hum}%")

        led.on()  # Turn on LED to show it's working

        response = json.dumps({
            "temperature": temp,
            "humidity": hum
        })

        # Send proper HTTP + CORS headers
        cl.send('HTTP/1.1 200 OK\r\n')
        cl.send('Content-Type: application/json\r\n')
        cl.send('Access-Control-Allow-Origin: *\r\n')
        cl.send('Connection: close\r\n\r\n')
        cl.send(response)
        cl.close()

        led.off()  # Turn off LED after response
    except Exception as e:
        print("Sensor read error:", e)
        cl.close()
