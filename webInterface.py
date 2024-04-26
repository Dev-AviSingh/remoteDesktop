from flask import Flask, request, jsonify, render_template
import os
from utilities import getFileInfo
from utilities import listDrives

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
# Dummy data to simulate history and control
history_data = []
control_data = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/ftp', methods=['GET', 'POST'])
def ftp():
    if request.method == 'POST':
        # Handle POST request data
        data = request.json
        # Dummy action, you can replace it with your actual FTP logic
        action = data.get('action')
        return jsonify({'message': f'Performed FTP action: {action}'})
    else:
        return 'FTP Endpoint'

@app.route('/terminal', methods=['GET', 'POST'])
def terminal():
    if request.method == 'POST':
        # Handle POST request data
        data = request.json
        # Dummy command execution, you can replace it with your actual terminal logic
        command = data.get('command')
        return jsonify({'message': f'Executed command: {command}'})
    else:
        return 'Terminal Endpoint'

@app.route('/filequery', methods=['GET'])
def file_query():
    path = request.args.get('path', '/')

    if os.path.isfile(path):
        return jsonify(getFileInfo(path))
    elif os.path.isdir(path):
        result = {}
        result['type'] = 'directory'
        result['isDirectory'] = True
        if path == "/":
            result["children"] = listDrives()
            result['type'] = "root"
        else:
            result['children'] = os.listdir(path)
        return jsonify(result)
    else:
        return "Invalid path or file not found."



@app.route('/history', methods=['GET'])
def history():
    return jsonify(history_data)

@app.route('/control', methods=['GET', 'POST'])
def control():
    if request.method == 'POST':
        # Handle POST request data
        data = request.json
        # Dummy action, you can replace it with your actual control logic
        action = data.get('action')
        control_data.append(action)
        return jsonify({'message': f'Performed control action: {action}'})
    else:
        return jsonify(control_data)

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000, debug=True)
