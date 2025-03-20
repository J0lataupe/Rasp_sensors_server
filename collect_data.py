import sqlite3
import random
from datetime import datetime, timedelta

# Connexion à la base de données (crée le fichier s'il n'existe pas)
conn = sqlite3.connect('mesures.db')
cursor = conn.cursor()

# Fonction pour générer des horodatages aléatoires
def generate_timestamps(start, end, n):
    """Génère n horodatages entre start et end."""
    delta = (end - start).total_seconds()
    return [start + timedelta(seconds=random.randint(0, int(delta))) for _ in range(n)]

# Données de test
start_time = datetime(2023, 10, 1, 12, 0, 0)  # Début : 1er octobre 2023 à 12:00
end_time = datetime(2023, 10, 1, 13, 0, 0)    # Fin : 1er octobre 2023 à 13:00
num_entries = 20  # Nombre d'entrées à générer pour chaque type de mesure

# Types de mesures et leurs unités
measure_types = {
    "temp": "°C",
    "pressure": "hPa",
    "flow": "L/min"
}

# Générer et insérer des données aléatoires
for measure_type, unit in measure_types.items():
    timestamps = generate_timestamps(start_time, end_time, num_entries)
    for timestamp in timestamps:
        # Générer une valeur aléatoire en fonction du type de mesure
        if measure_type == "temp":
            value = round(random.uniform(20, 30), 2)  # Température entre 20°C et 30°C
        elif measure_type == "pressure":
            value = round(random.uniform(1000, 1020), 2)  # Pression entre 1000 hPa et 1020 hPa
        elif measure_type == "flow":
            value = round(random.uniform(10, 20), 2)  # Débit entre 10 L/min et 20 L/min

        # Insérer les données dans la table
        cursor.execute('''
        INSERT INTO mesures (capteur, type_mesure, valeur, unite, horodatage)
        VALUES (?, ?, ?, ?, ?)
        ''', (f"Capteur1", measure_type, value, unit, timestamp))

# Valider les changements et fermer la connexion
conn.commit()
conn.close()

print("Données de test insérées avec succès.")