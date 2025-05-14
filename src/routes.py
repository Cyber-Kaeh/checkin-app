from flask import Blueprint, redirect, render_template, url_for, request, jsonify, session
from src.config import db
import firebase_admin
from firebase_admin import credentials, auth

main_bp = Blueprint('main', __name__)
auth_bp = Blueprint('auth', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/signup')
def signup():
    return render_template('signup.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    data = request.get_json()
    id_token = data.get('idToken')

    try:
        decoded_token = auth.verify_id_token(id_token)
        session['uid'] = decoded_token['uid']
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        print("Token verification failed:", e)
        return jsonify({'error': 'Unauthorized'}), 401
    

@auth_bp.route('/logout')
def logout():
    session.pop('uid', None)
    return redirect(url_for('main.index'))

@auth_bp.route('/dashboard')
def dashboard():
    if 'uid' not in session:
        return redirect(url_for('auth.login'))
    return render_template('dashboard.html')

# @main_bp.route('/')
# def display_all_users():
#     result = db.child("members").get()
#     print("Raw result:", result.val())
#     if result.val() is not None:
#         for user in result.each():
#             print(user.val())
#     else:
#         print("No data found.")
#     return 
    

# @main_bp.route('/add_member', methods=['GET', 'POST'])
# def add_member():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         phone = request.form.get('phone')
#         available = request.form.get('available') == 'on'  # Checkbox for availability

#         # Create a new member entry
#         new_member = {
#             "name": name,
#             "phone": phone,
#             "available": available
#         }

#         # Push the new member to the database
#         db.child("members").push(new_member)

#         # Redirect to the home page
#         return redirect(url_for('main.home'))

#     # Render the form to add a new member
#     return render_template('add_member.html')