# rota do login/cadastro
from flask import Blueprint, request, redirect, url_for, flash, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user
from app import db

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'], endpoint='login')
def login():
    from app.models.user import User
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Identificar qual botão foi clicado
        if 'btn-login' in request.form:
            # Login
            user = User.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('tasks.tasks_view'))
            else:
                flash('Email ou senha incorretos.')
                return redirect(url_for('auth.login'))

        elif 'btn-registrar' in request.form:
            # Registro
            user = User.query.filter_by(email=email).first()
            if user:
                flash('Usuário já existe. Faça login.')
                return redirect(url_for('auth.login'))

            new_user = User(email=email, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            flash('Registrado com sucesso! Faça login agora.')
            return redirect(url_for('auth.login'))

    # GET request
    return render_template('login.html')



@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))
