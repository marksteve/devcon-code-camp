from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/args')
def args():
    return jsonify(**request.args)

@app.route('/form', methods=['POST'])
def form():
    return jsonify(**request.form)

@app.route('/json', methods=['POST'])
def _json():
    return jsonify(**request.json)

@app.route('/error_handling', methods=['POST'])
def error_handling():
    return request.form['name']

if __name__ == '__main__':
    app.run(debug=True)

