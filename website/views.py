from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/home', methods=['GET', 'POST'])
def home():
       return render_template("home.html", user=current_user)


@views.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
       return render_template("dashboard.html", user=current_user)

        
@views.route('/settings', methods=['GET','POST'])
def settings():
           return render_template('settings.html',  user=current_user)

