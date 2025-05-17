from flask import Flask, render_template, request, jsonify, session, redirect
# from src.routes import main_bp, auth_bp

app = Flask(__name__)
app.secret_key = 'your_secret_key'
# app.register_blueprint(main_bp)
# app.register_blueprint(auth_bp)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    