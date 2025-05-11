from flask import Blueprint, redirect, render_template, url_for, request
from app import db
bp = Blueprint('main', __name__)

@bp.route('/')
def display_all_users():
    result = db.child("members").get()
    print("Raw result:", result.val())
    if result.val() is not None:
        for user in result.each():
            print(user.val())
    else:
        print("No data found.")
    return 
    

@bp.route('/add_member', methods=['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        available = request.form.get('available') == 'on'  # Checkbox for availability

        # Create a new member entry
        new_member = {
            "name": name,
            "phone": phone,
            "available": available
        }

        # Push the new member to the database
        db.child("members").push(new_member)

        # Redirect to the home page
        return redirect(url_for('main.home'))

    # Render the form to add a new member
    return render_template('add_member.html')