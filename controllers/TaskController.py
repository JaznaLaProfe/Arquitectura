from services.TaskService import TaskService

class TaskController:
    @staticmethod
    def create_task_controller(user_id, description):
        return TaskService.create_task(user_id, description)        

    @staticmethod
    def mark_task_done_controller(task_id):
        return TaskService.mark_task_as_done(task_id)
    
    @staticmethod
    def get_tasks_controller():        
        return TaskService.get_all_tasks()
    
    @staticmethod
    def get_tasks_done_controller():
        return TaskService.get_tasks_done()
