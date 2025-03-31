import sqlite3
import random
import time
from datetime import datetime

def collect_data():
    conn = sqlite3.connect('mesures.db', check_same_thread=False)
    cursor = conn.cursor()

    measure_types = {
        "temp": "°C",
        "pressure": "hPa",
        "flow": "L/min"
    }

    while True:
        for measure_type, unit in measure_types.items():
            timestamp = datetime.now()
            value = round(random.uniform(20, 30), 2) if measure_type == "temp" else \
                    round(random.uniform(1000, 1020), 2) if measure_type == "pressure" else \
                    round(random.uniform(10, 20), 2)

            cursor.execute('''
            INSERT INTO mesures (capteur, type_mesure, valeur, unite, horodatage)
            VALUES (?, ?, ?, ?, ?)
            ''', ("Capteur1", measure_type, value, unit, timestamp))

            conn.commit()

        print(f"Données insérées à {timestamp}")
        time.sleep(2)

    conn.close()
