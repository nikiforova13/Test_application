from app.models import router as bl_models
from app.routers import base_responses, router_a
from flask import Flask, render_template
from flask_restx import Api, Resource, apidoc, fields

app = Flask(__name__)
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
if __name__ == "__main__":
    app.run()
