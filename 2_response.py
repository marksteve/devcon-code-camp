from flask import abort, Flask, jsonify, redirect, render_template

app = Flask(__name__)

@app.route('/text')
def text():
    return "text"

@app.route('/html')
def html():
    return render_template('template.html',
                           title="muchquee")

@app.route('/headers')
def headers():
    return "NOT FOUND!!!", 404

@app.route('/json')
def json():
    return (
        '{"name": "value"}',
        200,
        {
            'Content-Type': 'application/json',
        }
    )

@app.route('/jsonify')
def with_jsonify():
    return jsonify(name='value')

@app.route('/redirect')
def do_redirect():
    return redirect('/')

@app.route('/error_400')
def error_400():
    abort(400)

if __name__ == '__main__':
    app.run(debug=True)

