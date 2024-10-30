from flask import Blueprint, request, jsonify
from controllers.UserController import UserController

user_blueprint = Blueprint('user_blueprint', __name__)
class UserView:

    @staticmethod
    @user_blueprint.route('/users/create', methods=['POST'])
    def create_user():
        # Recibe la solicitud para crear un usuario y delega al servicio
        data = request.get_json()
        username = data.get('username')
        new_user = UserController.create_user_controller(username)
        
        return jsonify({"mensaje": "Usuario creado", 
                        "user": {"id": new_user.id, "username": new_user.username}}), 201

    @staticmethod
    @user_blueprint.route('/users', methods=['GET'])
    def get_all_users():
        # Llama al controlador para obtener todos los usuarios
        users = UserController.get_users_controller()
        users_list = [{"id": user.id, "username": user.username} for user in users]
        return jsonify({"users": users_list}), 200

    @staticmethod
    @user_blueprint.route('/users/<int:user_id>', methods=['GET'])
    def get_user_by_id(user_id):
        # Llama al controlador para obtener un usuario por su ID
        user = UserController.get_user_by_id_controller(user_id)
        if user is None:
            return jsonify({"mensaje" : "Usuario inexistente"}), 404
        
        return jsonify({"id": user.id, "username": user.username}), 200
