from flask import Flask, render_template, request, redirect, url_for

# from app.pages.auth.auth_routes import auth_bp

app = Flask(__name__)

# app.register_blueprint(auth_bp, url_prefix='/auth')

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         if request.form['username'] == 'sesac' and request.form['password'] == 'sesac':
#             return redirect(url_for('user'))
#         return render_template('login.html', success=False)
        
#     return render_template('login.html', success=True)

@app.route('/')
def order():
    return render_template('base.html')

@app.route('/user')
def user():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
