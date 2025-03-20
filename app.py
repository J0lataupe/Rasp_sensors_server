from flask import Flask, render_template, redirect, url_for, session, flash, jsonify, request 
from auth import auth
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.register_blueprint(auth)


def init_db():
    conn = sqlite3.connect('mesures.db')
    cursor = conn.cursor()
    """
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
    """
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    
    conn.commit()
    conn.close()

def get_measurements(measure_type):
    conn = sqlite3.connect('mesures.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT valeur, horodatage, unite FROM mesures WHERE type_mesure = ? ORDER BY horodatage DESC LIMIT 10", 
        (measure_type,)
    )
    rows = cursor.fetchall()
    conn.close()
    return [{"value": row[0], "timestamp": row[1], "unit": row[2]} for row in rows]

# Ajout de la route manquante
@app.route('/get_measure_data')
def get_measure_data():
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401
        
    measure_type = request.args.get('measure')
    data = get_measurements(measure_type)
    return jsonify(data)

@app.route('/index')
def index():
    if 'user_id' not in session:
        flash("Veuillez vous connecter pour accéder à cette page.", "error")
        return redirect(url_for('auth.handle_login'))

    temperatures = get_measurements("temp")
    return render_template("index.html", temperatures=temperatures)

@app.route('/')
def home():
    flash("Veuillez vous connecter pour accéder à cette page.", "error")
    return redirect(url_for('auth.handle_login'))


with app.app_context():
    init_db()
    print("Base de données initialisée avec succès")
