from flask import Blueprint

site = Blueprint('site', __name__)

@site.route('/')
def index():
    return "this is a route for the site"
