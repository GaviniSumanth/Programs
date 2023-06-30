from flask_api import FlaskAPI
from flask_cors import CORS, cross_origin
from flask import request, jsonify
import src.db as db


def Server():
    app = FlaskAPI(__name__)
    # cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    CORS(app)

    @app.route("/result/", methods=["POST"])
    @cross_origin()
    def result():
        data = request.data
        model = db.Model().get_model(data.pop("form"))
        pred = model.predict(data)
        return jsonify({"result": pred})

    @app.route("/form", methods=["GET"])
    @cross_origin()
    def form():
        form_name = request.args["form"]
        info = db.ModelInfo()
        return info.get_fields(form_name)

    app.run()
