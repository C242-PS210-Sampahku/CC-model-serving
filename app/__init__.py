from flask import Flask
from app.routes import prediction, healthcheck

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    # Register routes
    app.register_blueprint(prediction.bp)
    app.register_blueprint(healthcheck.bp)
    return app
