import os, json
from flask import Flask, send_file, render_template
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World from Flask"

@app.route("/")
# def main():
#     return send_file(app.static_folder + '/index.html')
def main():
    dir_list = os.listdir("/data")
    return render_template('index.html', text=dir_list)

@app.route("/api")
def api():
    return json.dumps(os.listdir("/data"))

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)