from flask import Blueprint, render_template

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def user():
    return render_template('pages/user/user.html')

@user_bp.route('/detail/<string:id>')
def user_detail(id):
    return render_template('pages/user/user_detail.html')