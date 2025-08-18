from flask import Blueprint, render_template

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
@user_bp.route('/<int:page>')
def user(page=1):
    return render_template('pages/user/user.html', route={'type': 'user', 'param': page})

@user_bp.route('/detail/<string:id>')
def user(id=None):
    return render_template('pages/user/user.html', route={'type': 'userDetail', 'param': id})