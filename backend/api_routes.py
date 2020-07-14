from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/services')
def get_services():
    return "here I'd have all the data"
