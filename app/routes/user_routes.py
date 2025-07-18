from flask import Blueprint, render_template

user_bp = Blueprint('user', __name__)
user_api_bp = Blueprint('user_api', __name__)

@user_bp.route('/')
def user():
    return render_template('pages/user/user.html')

@user_api_bp.route('/')
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])