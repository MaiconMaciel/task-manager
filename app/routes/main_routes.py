# rota da homepage

from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from app.models import Task

bp = Blueprint('main', __name__)

@bp.route("/")
def home():
    if current_user.is_authenticated:
        tasks = Task.query.filter_by(user_id=current_user.id).all()
        return redirect(url_for('tasks.tasks_view', tasks=tasks))

    return render_template("home.html")

