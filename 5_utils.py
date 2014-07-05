from flask import Flask, make_response, safe_join, send_file, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, world"

@app.route('/url_for')
def with_index_url():
    return url_for('index')

@app.route('/abs_url_for')
def with_abs_index_url():
    return url_for('index', _external=True)

@app.route('/param/<param>')
def with_param(param):
    return param

@app.route('/param_url_for')
def with_param_url():
    return url_for('with_param', param='ita')

@app.route('/download')
def download():
    return send_file(
        safe_join(app.static_folder, 'pythonph.png')
    )

@app.route('/attachment')
def attachment():
    return send_file(
        safe_join(app.static_folder, 'pythonph.png'),
        as_attachment=True,
    )

if __name__ == '__main__':
    app.run(debug=True)

