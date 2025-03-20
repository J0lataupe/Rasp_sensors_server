import sqlite3

# Creer un db et ajouter une mesure
def ajouter_mesure(str_Sensor, str_Type_mesure, f_Value, str_Unite):

        # Connexion la base de donnees
        conn = sqlite3.connect('mesures.db')

        # Creation d’un curseur
        cursor = conn.cursor ()

        # Creation de la table des mesures
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS mesures (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                capteur TEXT NOT NULL,
                type_mesure TEXT NOT NULL,
                valeur REAL NOT NULL,
                unite TEXT NOT NULL,
                horodatage DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        ''')

        # Insertion des données dans la table 'mesures'
        cursor.execute('''
                INSERT INTO mesures (capteur, type_mesure, valeur, unite)
                VALUES (?, ?, ?, ?)
        ''', (str_Sensor, str_Type_mesure, f_Value, str_Unite))

        # Validation des changements
        conn.commit()

        # Fermeture de la connexion
        conn.close()
