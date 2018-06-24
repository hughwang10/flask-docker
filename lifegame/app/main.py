import os
from flask import Flask #, send_file, render_template, request, jsonify
app = Flask(__name__,static_url_path='')

@app.route("/")
def hello():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
