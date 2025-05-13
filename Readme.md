# 🌡️ IoT Weather Station using Raspberry Pi Pico W

This is a simple Internet of Things (IoT) project built by **Dev** using a **Raspberry Pi Pico W**. It reads real-time **temperature and humidity** data from a DHT22 sensor and serves it over Wi-Fi using MicroPython.

---

## 🔧 Hardware Used
- 🧠 Raspberry Pi Pico W
- 🌡️ DHT22 Temperature & Humidity Sensor
- 💡 Onboard LED (used as activity indicator)
- 📶 Wi-Fi Network (2.4 GHz)

---

## ⚙️ Features
- Connects to a Wi-Fi network using MicroPython
- Reads temperature and humidity from DHT22 sensor
- Serves live data as JSON over HTTP (`port 8080`)
- Sends proper HTTP + CORS headers
- Onboard LED blinks during each data reading

---

## 📁 Project Files
- `main.py` – MicroPython script (run on Pico W)
- `IoT.html` – Frontend web interface to display data
- `README.md` – Project documentation

---

## 🌐 How to Use
1. Flash MicroPython firmware to your Pico W.
2. Connect the DHT22 sensor to GPIO 15.
3. Upload `main.py` using [Thonny IDE](https://thonny.org/).
4. Connect to Wi-Fi; the IP will be shown in the serial output.
5. Open `IoT.html` and change the fetch URL to match your Pico W's IP address.

---

## 🖼️ Screenshots

### 🌤 Comfortable Weather Mode
![Comfortable](https://raw.githubusercontent.com/Deox00/iot-weather-station/main/Screenshot%202025-05-13%20114723.png)

### 🔥 Hot Weather Alert
![Hot](https://raw.githubusercontent.com/Deox00/iot-weather-station/main/Screenshot%202025-05-13%20160115.png)


## 🙋‍♂️ Created by Dev Kaushik

A computer science student passionate about embedded systems and IoT.

---

## 🔗 Connect with Me
- 💼 [LinkedIn](https://www.linkedin.com/in/dev-kaushik-607784337/)
- 💻 [GitHub](https://github.com/Deox00)
"# pico_iot_project" 
