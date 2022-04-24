from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def retrieve():
        return "Seja bem vinde!!!!!",200
    return app




