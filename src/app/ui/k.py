from app.routers.shemas.base import BaseApiResponse
from flask import abort, request
from flask_restx import Namespace, Resource

router = Namespace("blazegraph2", description="API for database interaction")
@router.route('/')
class K(Resource):
    def get(self):
        return '<h1>HELLOO DIMAAA I LOVE YOU AND I WANT YOU</h1>'