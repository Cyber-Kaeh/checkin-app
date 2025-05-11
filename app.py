from flask import Flask, request, jsonify, session, redirect
import firebase_admin
from firebase_admin import credentials, auth
from src.routes import main_bp, auth_bp

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)

cred = credentials.Certificate('firebase_key.json')
firebase_admin.initialize_app(cred)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    