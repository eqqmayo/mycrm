import os
from flask import Blueprint, render_template, redirect, url_for, request

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        admin_id = os.getenv('ADMIN_ID')
        admin_pw = os.getenv('ADMIN_PW') 
        
        if (request.form['username'] == admin_id and 
            request.form['password'] == admin_pw):
            return redirect(url_for('user.user'))
        return render_template('pages/auth/login.html', success=False)
        
    return render_template('pages/auth/login.html', success=True)