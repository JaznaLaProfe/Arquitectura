from models.TaskModel import db, Task

class TaskService:
    @staticmethod
    def create_task(user_id, description):
        # Crea el objeto
        task = Task(descripcion=description, user_id=user_id)
        # Agrega el objeto a la bd relacional (usando ORM)
        db.session.add(task)
        db.session.commit()
        return task

    @staticmethod
    def get_all_tasks():
        return Task.query.all()     
    
    @staticmethod
    def mark_task_as_done(task_id):
        task = Task.query.get(task_id)
        # Verifica que la tarea exista
        if task:
            # Cambia estado
            task.estado = 'terminada'
            db.session.commit()
            return task
        return None
    
    @staticmethod
    def get_tasks_done():
        # Filtra las tareas terminadas
        all_tasks = db.session.query(Task).filter_by(estado = "terminada").all()
        return all_tasks