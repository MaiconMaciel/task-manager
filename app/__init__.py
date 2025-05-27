# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.extensions import db, login_manager
from app.models import Task
from .routes.auth_routes import bp as auth_bp



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'u213y4c09u123y4npo21x837n' # voce pode trocar por outra coisa aleatória

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://usuario:senha@localhost:3306/taskdb' # configure sua db
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # Nome da função na rota de login

    from .models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .routes.main_routes import bp as main_bp
    from .routes.auth_routes import bp as auth_bp
    from .routes.tasks_routes import bp as tasks_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    print("Rotas registradas:")
    for rule in app.url_map.iter_rules():
        print(f"{rule.endpoint}: {rule.rule}")

    return app

