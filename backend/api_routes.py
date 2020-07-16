from flask import Blueprint, jsonify, request

from backend.infrastructure.repositories.services_repository import ServicesRepository
from backend.infrastructure.repositories.users_repository import UsersRepository

api = Blueprint('api', __name__, url_prefix='/api')


services_repo = ServicesRepository()


@api.route('/services')
def get_services():
    query = services_repo.get_all()
    services = services_repo.execute_query(query)
    return jsonify({'services': services})


@api.route('/services/<int:service_id>')
def get_service(service_id):
    query = services_repo.get_by_id(service_id)
    service = services_repo.execute_query(query)
    return jsonify({'service': service})


@api.route('/services', methods=['POST'])
def post_service():
    #TODO
    return jsonify()


@api.route('/services', methods=['PATCH'])
def patch_service():
    #TODO
    return


@api.route('/services', methods=['DELETE'])
def delete_service():
    #TODO
    return



users_repo = UsersRepository()


@api.route('/users')
def get_users():
    query = users_repo.get_all()
    users = users_repo.execute_query(query)
    return jsonify(users)


@api.route('/users/<int:user_id>')
def get_user(user_id):
    query = users_repo.get_by_id(user_id)
    user = users_repo.execute_query(query)
    return jsonify(user)


@api.route('/users', methods=['POST'])
def post_user():
    #TODO
    return


@api.route('/users', methods=['PATCH'])
def patch_user():
    #TODO
    return


@api.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    query = users_repo.delete()
    users_repo.save_changes(query)
    return jsonify({'result': True})
