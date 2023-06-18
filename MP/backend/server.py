from flask_api import FlaskAPI
from flask_cors import CORS, cross_origin
from flask import request, jsonify


def Server():
    app = FlaskAPI(__name__)
    # cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    CORS(app)

    @app.route("/model/", methods=["POST"])
    @cross_origin()
    def steam():
        data = request.data
        return jsonify({"result": data})

    @app.route("/info/", methods=["GET"])
    @cross_origin()
    def steams():
        return jsonify({"result": "Success"})

    app.run()
