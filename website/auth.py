from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_harsh, check_password_harsh

auth = Blueprint('auth', __name__)

@auth.route('/login' , methods=['GET', 'POST'])
def login():
    return render_template("login.html",boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash ('Email must be more than 3 characters. , category= error')
        elif len(firstName) < 2:
            flash ('First name must be more than 1 character. , category= error')
        elif password1 != password2:
             flash ('Passwords don\'t match , category= error')
        elif len(password1) < 7:
            flash ('Passwords must be at least 7 characters. , category= error')
        else:   
            new_user = User(eamil=email, firstName=firstName, password=generate_password_harsh(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash ('Account created!', category='success' )
            

            




    return render_template("sign_up.html")
