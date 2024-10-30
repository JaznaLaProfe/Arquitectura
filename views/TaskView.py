from flask import Blueprint, request, jsonify

from controllers.TaskController import TaskController

task_blueprint = Blueprint('task_blueprint', __name__)

# Definir la clase TaskView
class TaskView:
    
    @staticmethod
    @task_blueprint.route('/tasks/create', methods=['POST'])
    def create_task():
        # Obtener los datos del cuerpo de la solicitud y crear una tarea
        data = request.get_json()
        descripcion = data.get('descripcion')
        user_id = data.get('user_id')
        
        new_task = TaskController().create_task_controller(user_id, description=descripcion)
        return jsonify({"mensaje": "Tarea creada", 
                        "task": {"id": new_task.id, "descripcion": new_task.descripcion}}), 201

    @staticmethod
    @task_blueprint.route('/tasks', methods=['GET'])
    def get_all_tasks():
        # Llama al controlador para obtener todos los usuarios
        tasks = TaskController.get_tasks_controller()
        tasks_list = [{"id": task.id, "descripcion": task.descripcion, "estado" : task.estado} for task in tasks]
        return jsonify({"tasks": tasks_list}), 200
            
    @staticmethod
    @task_blueprint.route('/tasks/<int:task_id>/done', methods=['PATCH'])
    def mark_task_done(task_id):
        task = TaskController.mark_task_done_controller(task_id)
        
        return jsonify({"mensaje": "Tarea marcada como terminada", 
                        "task":  {"id": task.id, "descripcion": task.descripcion}}), 200

    @staticmethod
    @task_blueprint.route('/tasks/done', methods=['GET'])
    def get_tasks_done():
        all_tasks = TaskController.get_tasks_done_controller()

        if all_tasks is None:
            return jsonify({"mensaje" : "Ninguna tarea terminada"}), 404
        
        tasks_list = [{"id": task.id, "descripcion": task.descripcion, "estado" : task.estado} for task in all_tasks]
        return jsonify({"tasks": tasks_list}), 200        