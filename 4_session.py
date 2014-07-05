from flask import (abort, flash, Flask, get_flashed_messages, redirect,
                   render_template, request, session)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'sssikreto'

@app.route('/')
def index():
    login_url = '/login'
    messages = get_flashed_messages()
    if request.args.get('better'):
        login_url = '/better_login'
    return render_template('session.html',
                           login_url=login_url,
                           messages=messages)

@app.route('/login', methods=['POST'])
def login():
    if request.form['password'] != 'armin':
        abort(401)
    session['user'] = request.form['user']
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/better_login', methods=['POST'])
def better_login():
    if request.form['password'] == 'armin':
        session['user'] = request.form['user']
    else:
        flash("Password is incorrect")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

