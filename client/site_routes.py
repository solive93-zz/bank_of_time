from flask import Blueprint, render_template

site = Blueprint('site', __name__)

@site.route('/')
def hello_world():
    return 'Hello, World!'

@site.route('/home')
def index():
    return render_template('home.html')
