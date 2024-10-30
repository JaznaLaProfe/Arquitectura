from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True)
    
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'tasks': [task.to_dict() for task in self.tasks]
        }