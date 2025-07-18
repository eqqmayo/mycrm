from flask import Blueprint, render_template, redirect, url_for, request

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'sesac' and request.form['password'] == 'sesac':
            return redirect(url_for('user.user'))
        return render_template('pages/auth/login.html', success=False)
        
    return render_template('pages/auth/login.html', success=True)