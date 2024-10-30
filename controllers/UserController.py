from services.UserService import UserService

class UserController:    
    @staticmethod
    def create_user_controller(username):        
        return UserService.create_user(username)
            
    @staticmethod
    def get_users_controller():        
        return UserService.get_all_users()
    
    @staticmethod
    def get_user_by_id_controller(user_id):
        return UserService.get_user_by_id(user_id)
        