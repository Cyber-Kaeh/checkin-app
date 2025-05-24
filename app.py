from flask import Flask, render_template, request, jsonify, session, redirect
from flask_wtf import CSRFProtect
from src.routes import main_bp, auth_bp, guest_bp
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
csrf = CSRFProtect(app)

app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(guest_bp)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    