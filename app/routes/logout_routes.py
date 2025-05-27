
from flask import session, redirect, url_for, Blueprint, render_template
from flask_login import logout_user, current_user


bp = Blueprint('auth', __name__)


@app.route('/logout')
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('main.home'))
