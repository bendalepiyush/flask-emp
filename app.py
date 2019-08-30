from flask import Flask, jsonify, request, make_response
from flask_cors import CORS, cross_origin
from match import match

app = Flask(__name__)
cors = CORS(app, resources={"/": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=["POST", "GET"])
@cross_origin()
def upload():
    if "id" in request.args:
        file = request.files["file"]
        file.save("uploads/tmp.jpg")

        if match(request.args.get("id")) == True:
            return jsonify({"auth": "true"}), 200
        else:
            return jsonify({"auth": "false"}), 200
    return jsonify({"status": "error"}), 400

if __name__ == "__main__":
    app.run(debug=True, host="192.168.0.20", port="5000")