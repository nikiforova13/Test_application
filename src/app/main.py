from flask import Flask, render_template
from flask_restx import Resource, Api, apidoc, fields
from src.app.routers import router_a
app = Flask(__name__)
api = Api(app=app, doc='/docs', version="0.1.0", title='bl-selector',
          description='A service for interacting with the blazegraph database')
api.add_namespace(router_a)




