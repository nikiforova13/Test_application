from flask import abort, request
from flask_restx import Namespace, Resource  # type: ignore

from app.dao.db_bl import BlazegraphDB
from app.routers.shemas.base import BaseApiResponse
from app.routers.shemas.query import query_model

router = Namespace("blazegraph", description="API for database interaction")


db_dal = BlazegraphDB()


@router.route("/fetch")
@router.doc(
    responses=BaseApiResponse,
)
class InteractDB(Resource):
    @router.expect(query_model)
    def post(self):
        """Get data from db"""
        json_data = request.json
        if not json_data:
            abort(404)
        return db_dal.get_query(json_data.get("query"))["results"]["bindings"], 200
