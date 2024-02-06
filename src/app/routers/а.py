from flask_restx import Resource, Namespace, fields
from flask import request, abort

# from src.app.models.query import query_model

from app.dao.db_bl import BlazegraphDB
from app.routers.shemas.base import BaseApiResponses, model_errors_data
from .handler import handler_request

router = Namespace("blazegraph", description="API for database interaction")


db_dal = BlazegraphDB()


query_model = router.model(
    "SelectQueryInDB",
    {
        "query": fields.String(
            example="SELECT ?class WHERE {?class a <http://src/rtw#Class>}",
            description="The query to be executed to retrieve data",
        ),
        "error_details": fields.List(fields.Nested(model_errors_data)),
    },
)


@router.route("/fetch")
@router.doc(
    responses=BaseApiResponses,
)
class InteractDB(Resource):

    def get(self):
        """Get data from db"""
        return {
            db_dal.get_all_classes(),
            db_dal.get_all_individual_iri_and_label(),
            db_dal.get_all_subject_and_predicate_and_object(),
        }

        # return BaseAPIResponse(status_code=200).model_dump_json()

    # @router.param('query', 'query for select')
    # @router.marshal_with(query_model, as_list=True)
    @router.expect(query_model)
    def post(self):
        """Get data from db"""
        handler_request(request)
        # json_data = request.json
        # return db_dal.get_query(json_data.get("query"))
        # return BaseAPIResponse(status_code=200).model_dump_json()
