from flask import Blueprint, redirect, render_template, url_for, request, jsonify, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from src.db_config import Session, User
from src.forms import SignupForm, LoginForm
import re

main_bp = Blueprint('main', __name__)
auth_bp = Blueprint('auth', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        name = ''.join(form.name.data.split()).lower()
        phone = re.sub(r'\D', '', form.phone.data)
        print(f"Name: {name}, Phone: {phone}")
        available = form.available.data

        session_db = Session()
        new_user = User(name=name, available=available)
        new_user.set_phone(phone)
        session_db.add(new_user)
        session_db.commit()
        session['uid'] = new_user.id
        session_db.close()

        flash('Glad your here!', 'success')
        return redirect(url_for('auth.dashboard'))

    return render_template('signup.html', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        name = ''.join(form.name.data.split()).lower()
        phone = re.sub(r'\D', '', form.phone.data)

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
    flash('Keep coming back!', 'danger')
    return redirect(url_for('main.index'))

@auth_bp.route('/dashboard')
def dashboard():
    form = SignupForm()
    if 'uid' not in session:
        return redirect(url_for('auth.login'))
    session_db = Session()
    user = session_db.query(User).filter_by(id=session.get('uid')).first()
    return render_template('dashboard.html', user=user, form=form)

@auth_bp.route('/toggle-available', methods=['POST'])
def toggle_available():
    if 'uid' not in session:
        flash('Your not logged in?!', 'danger')
        return redirect(url_for('auth.login'))
    session_db = Session()
    user = session_db.query(User).get(session['uid'])
    if user:
        user.available = not user.available
        session_db.commit()
        session_db.close()
        flash('Your availability has been updated!', 'success')
    else:
        flash('User not found', 'danger')
    return redirect(url_for('auth.dashboard'))
