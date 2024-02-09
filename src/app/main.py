from app.models import router as bl_models
from app.routers import base_responses, router_a
from app.ui.k import router as router_ui
from flask import Flask, render_template
from flask_restx import Api, Resource, apidoc, fields

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>HELLOO DIMAAA I LOVE YOU AND I WANT YOU</h1>'


api = Api(
    app=app,
    doc="/docs",
    version="0.1.0",
    title="bl-selector",
    description="A service for interacting with the blazegraph database",
)
api.add_namespace(router_a)
api.add_namespace(base_responses)
api.add_namespace(bl_models)
api.add_namespace(router_ui)

# app = Flask(__name__)


if __name__ == "__main__":
    app.run()
