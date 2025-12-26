# toda a funcionalidade das tarefas (CRUD)


from flask import request, jsonify, Blueprint, render_template
from app.extensions import db
from app.models import Task
from flask_login import login_required, current_user

bp = Blueprint('tasks', __name__)


@bp.route('/api/tasks', methods=['POST'])
@login_required
def create_task():
    data = request.get_json()
    title = data.get('title')

    if not title:
        return jsonify({'error': 'Título é obrigatório'}), 400

    task = Task(title=title, done=False, user_id=current_user.id)
    db.session.add(task)
    db.session.commit()

    return jsonify({
        'id': task.id,
        'title': task.title, # TITLE SE REFERE AO TITULO DA TAREFA EX. GRAVAR DEMONSTRAÇÂO KUMULUS
        'done': task.done
    }), 201


@bp.route('/tasks')
@login_required
def tasks_view():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('tasks.html', tasks=tasks)

# STATUS
@bp.route('/tasks/<int:task_id>/toggle', methods=['POST'])
@login_required
def toggle_task(task_id):
    from app.models.task import Task
    task = Task.query.get_or_404(task_id)

    # Garante que só o dono pode alterar
    if task.user_id != current_user.id:
        return {'error': 'Unauthorized'}, 403

    # Alterna o status
    task.done = not task.done
    db.session.commit()
    return jsonify(success=True, done=task.done)

# REMOVER

@bp.route('/api/tasks/<int:task_id>', methods=['DELETE'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)

    # Verifica se o usuário logado é o dono
    if task.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403

    db.session.delete(task)
    db.session.commit()
    return jsonify({'success': True})


# EDITAR

@bp.route('/api/tasks/<int:task_id>', methods=['PUT'])
@login_required
def update_task(task_id):
    data = request.get_json()
    task = Task.query.get_or_404(task_id)

    if task.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403

    task.title = data.get('title', task.title)
    db.session.commit()
    return jsonify({'success': True})