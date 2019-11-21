from flask import Flask, jsonify, request, make_response
from flask_cors import CORS, cross_origin
from match import match, encode
import requests

app = Flask(__name__)
cors = CORS(app, resources={"/": {"origins": "*"}, "/employee/register": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/employee/register", methods=["POST", "GET"])
@cross_origin()
def encodeImg():
    if "profileId" in request.form:
        file = request.files["file"]
        file.save("tmp/tmp.jpg")
        if encode(request.form["profileId"]) == True:
            return jsonify({"status": "ok"}), 200
    return jsonify({"status": "error"}), 400

@app.route("/", methods=["POST", "GET"])
@cross_origin()
def upload():
    if "id" in request.args:
        file = base64.b64decode(request.form["file"])
        with open("uploads/tmp.jpg", "wb") as fp:
            fp.write(file)
        fp.close()
        if match(request.args.get("id")) == True:
            return jsonify({"auth": "true"}), 200
        else:
            return jsonify({"auth": "false"}), 200
    return jsonify({"status": "error"}), 400


if __name__ == "__main__":
    app.run()
