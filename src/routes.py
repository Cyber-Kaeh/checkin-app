from flask import Blueprint, redirect, render_template, url_for, request, jsonify, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from src.db_config import Session, User
from src.forms import SignupForm, LoginForm

main_bp = Blueprint('main', __name__)
auth_bp = Blueprint('auth', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/signup')
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data.strip()
        phone = form.phone.data.strip()
        available = form.available.data

        session_db = Session()
        new_user = User(name=name, available=available)
        new_user.set_phone(phone)
        session_db.add(new_user)
        session_db.commit()
        session_db.close()

        flash('Glad your here!', 'success')
        return redirect(url_for('auth.dashboard'))

    return render_template('signup.html', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.name.data.strip()
        phone = form.phone.data.strip('()- ')

        session_db = Session()
        user = session_db.query(User).filter_by(name=name).first()
        session_db.close()
        if user and user.check_phone(phone):
            session['uid'] = user.id
            flash('Welcome Back!', 'success')
            return redirect(url_for('auth.dashboard'))
        else:
            flash('Invalid username or password', 'danger')
            session_db.close()
    return render_template('login.html', form=form)
    

@auth_bp.route('/logout')
def logout():
    session.pop('uid', None)
    return redirect(url_for('main.index'))

@auth_bp.route('/dashboard')
def dashboard():
    if 'uid' not in session:
        return redirect(url_for('auth.login'))
    return render_template('dashboard.html')

# @main_bp.route('/add_member', methods=['GET', 'POST'])
# def add_member():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         phone = request.form.get('phone')
#         available = request.form.get('available') == 'on'

#         session_db = Session()
#         new_user = User(name=name, phone=phone, available=available)
#         new_user.set_phone(phone)
#         session_db.add(new_user)
#         session_db.commit()
#         session_db.close()

#         flash('Glad your here!', 'success')
#         return redirect(url_for('main.index'))

#     # Render the form to add a new member
#     return render_template('add_member.html')