from flask import Blueprint

api = Blueprint('api', url_defaults='/api')


@api.route('/services')
def get_services():
    return "here I'd have all the data"
