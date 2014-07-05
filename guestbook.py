import time

from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///guestbook.db'

def now():
    return int(time.time())

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    message = db.Column(db.Text)
    created_at = db.Column(db.Integer, default=now)

@app.route('/')
def index():
    return render_template(
        'guestbook.html',
        entries=Entry
            .query
            .order_by(
                Entry.created_at.desc()
            ).all(),
    )

@app.route('/new', methods=['POST'])
def sign():
    entry = Entry()
    entry.name = request.form['name']
    entry.message = request.form['message']
    db.session.add(entry)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
