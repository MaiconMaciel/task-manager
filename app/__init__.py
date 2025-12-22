# app/__init__.py

from flask import Flask
from app.extensions import db, login_manager
from app.models import Task
from dotenv import load_dotenv
import os

load_dotenv()  # carrega arquivo .env
secret_key = os.getenv('SECRET_KEY') #crie uma key e a coloque em um .env: python -c "import secrets; print(secrets.token_hex(32))"
db_conn = os.getenv('DB_CONN') #no .env crie sua string de conexão com o mySQL: 'mysql+pymysql://user:senha@localhost:3306/schema'

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = secret_key # .env 
    app.config['SQLALCHEMY_DATABASE_URI'] = db_conn # .env
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

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
