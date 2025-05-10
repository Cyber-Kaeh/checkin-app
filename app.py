from flask import Flask, render_template
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
firebase_config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID"),
}

@app.route('/')
def index():
    return render_template('index.html', firebase_config=firebase_config)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    