from flask import Flask
from flask_restx import Api

from app.routers import router_base_responses, router_bl, router_models
from app.ui import ui_router

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret key"
app.register_blueprint(ui_router)

api = Api(
    app=app,
    doc="/docs",
    version="0.1.0",
    title="bl-selector",
    description="A service for interacting with the blazegraph database",
)

api.add_namespace(router_bl)
api.add_namespace(router_base_responses)
api.add_namespace(router_models)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
