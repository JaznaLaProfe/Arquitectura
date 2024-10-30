from models.UserModel import db, User

class UserService: 
    @staticmethod   
    def create_user(username):
        user = User(username=username)
        db.session.add(user)
        db.session.commit()
        return user        
        
    @staticmethod
    def get_all_users():
        return User.query.all()        
    
    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)