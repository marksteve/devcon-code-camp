from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, world"

@app.route('/<name>')
def hello_with_name(name="world"):
    return "Hello, {}".format(name)

@app.route('/<int:post_id>')
def posts(post_id):
    return "Post: {}".format(post_id)

if __name__ == '__main__':
    app.run(debug=True)

