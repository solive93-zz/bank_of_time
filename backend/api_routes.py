from flask import Blueprint, jsonify

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/services')
def get_services():
    return "here I'd have all the data"


@api.route('/services/<int:service_id>')
def get_service(service_id):
    return jsonify(service_id)
