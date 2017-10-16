import os
from flask import Flask, send_file, render_template, request, jsonify
app = Flask(__name__)

@app.route("/")
# def main():
#     return send_file(app.static_folder + '/index.html')
def main():
    dir_list = os.listdir("/data")
    return \
    render_template('index.html', \
    title='afglab@Athlone', \
    text=dir_list, \
    url_root=request.url_root[:-1], \
    package_name=request.args.get('package_name'))

@app.route("/api")
def api():
    return jsonify(os.listdir("/data")), 200

@app.route("/ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr,'url_root': request.url_root}), 200

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)