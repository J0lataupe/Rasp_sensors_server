from flask import Blueprint, request, jsonify, redirect, url_for, session, render_template, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

auth = Blueprint('auth', __name__)

# Route d'inscription
@auth.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "Requête invalide."}), 400

        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        repassword = data.get("repassword")

        if not all([username, email, password, repassword]):
            return jsonify({"success": False, "error": "Tous les champs sont requis."}), 400

        if password != repassword:
            return jsonify({"success": False, "error": "Les mots de passe ne correspondent pas."}), 400

        hashed_password = generate_password_hash(password)
        conn = None
        try:
            conn = sqlite3.connect('mesures.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                           (username, email, hashed_password))
            conn.commit()
            return jsonify({"success": True}), 200
        except sqlite3.IntegrityError as e:
            return jsonify({"success": False, "error": "Nom d'utilisateur ou email déjà utilisé."}), 400
        except Exception as e:
            print("Erreur détaillée :", str(e))
            return jsonify({"success": False, "error": str(e)}), 500
        finally:
            if conn:
                conn.close()
    return render_template('register.html')

# Route pour afficher la page de connexion (GET)
@auth.route('/login', methods=['GET'])
def show_login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def handle_login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    conn = sqlite3.connect('mesures.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, password FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user and check_password_hash(user[1], password):
        session['user_id'] = user[0]
        return jsonify({"success": True}), 200

    return jsonify({"success": False, "error": "Identifiants incorrects"}), 401

# Route de déconnexion
@auth.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("Vous avez été déconnecté.", "success")
    return redirect(url_for('auth.handle_login'))