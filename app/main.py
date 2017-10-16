import os
from flask import Flask, send_file, render_template, request, jsonify
app = Flask(__name__)

@app.route("/")
# def main():
#     return send_file(app.static_folder + '/index.html')
def main():
    dir_list = os.listdir("/data")

    package_name=request.args.get('package_name')
    package_list = None
    if package_name:
        package_list = os.listdir("/data/" + package_name)

    return \
    render_template('index.html', \
    title='afglab@Athlone', \
    text=dir_list, \
    url_root=request.url_root[:-1], \
    package_name=package_name, \
    package_list=package_list)

@app.route("/api")
def api():
    package_name=request.args.get('package_name')
    if package_name:
        return jsonify(os.listdir("/data/" + package_name)), 200
    else:    
        return jsonify(os.listdir("/data")), 200

@app.route("/ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr,'url_root': request.url_root}), 200

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)