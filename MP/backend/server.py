from flask_api import FlaskAPI
from flask_cors import CORS, cross_origin
from flask import request, jsonify


def Server():
    app = FlaskAPI(__name__)
    # cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    CORS(app)

    @app.route("/result", methods=["POST"])
    @cross_origin()
    def result():
        data = request.data
        print(data)
        return jsonify({"result": "data"})

    @app.route("/form", methods=["GET"])
    @cross_origin()
    def form():
        args = request.args
        print(args)
        return jsonify(
            [
                {
                    "identifier": "username",
                    "label": "Enter Name:",
                    "type": "text",
                },
                {
                    "identifier": "gender",
                    "label": "Select Gender:",
                    "type": "select",
                    "options": ["Male", "Female", "Other"],
                },
            ]
        )

    app.run()
