from flask import Blueprint, render_template

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
@user_bp.route('/<int:page>')
@user_bp.route('/detail/<string:id>')
def user(page=1, id=None):
    return render_template('pages/user/user.html')