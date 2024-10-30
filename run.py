from app import create_app
from views.UserView import user_blueprint
from views.TaskView import task_blueprint

app = create_app()
app.register_blueprint(user_blueprint)
app.register_blueprint(task_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
