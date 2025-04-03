# Rasp_sensors_server

[English version below](#english)

## 🇫🇷 Serveur de Capteurs Raspberry Pi

### Description
Une application web Flask pour la surveillance en temps réel des capteurs connectés à un Raspberry Pi. Le système permet de visualiser les données des capteurs de température et d'humidité avec un système d'alarme intégré.

### Installation
1. Clonez le dépôt
2. Installez les dépendances :
```bash
pip install -r requirements.txt
```
3. Connectez vos capteurs au Raspberry Pi (DHT11 sur le GPIO 4)
   > Note : Vous pouvez facilement ajouter d'autres capteurs en les déclarant dans le fichier `current_data.py`
4. Connectez la LED d'alarme sur le GPIO 17

### Utilisation
1. Lancez l'application :
```bash
python main.py
```
2. Accédez à l'interface web via http://[adresse-ip-raspberry]:5000
3. Créez un compte ou connectez-vous
4. Visualisez les données en temps réel

### Fonctionnalités
- 📊 Interface web responsive
- 🔐 Système d'authentification
- 📈 Graphiques en temps réel
- 🚨 Système d'alarme avec LED
- 🌡️ Support des capteurs DHT11

---

## 🇬🇧 Raspberry Pi Sensors Server {#english}

### Description
A Flask web application for real-time monitoring of sensors connected to a Raspberry Pi. The system allows visualization of temperature and humidity sensor data with an integrated alarm system.

### Installation
1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Connect your sensors to the Raspberry Pi (DHT11 on GPIO 4)
   > Note: You can easily add more sensors by declaring them in the `current_data.py` file
4. Connect the alarm LED to GPIO 17

### Usage
1. Launch the application:
```bash
python main.py
```
2. Access the web interface via http://[raspberry-ip-address]:5000
3. Create an account or log in
4. View real-time data

### Features
- 📊 Responsive web interface
- 🔐 Authentication system
- 📈 Real-time charts
- 🚨 Alarm system with LED
- 🌡️ DHT11 sensors support