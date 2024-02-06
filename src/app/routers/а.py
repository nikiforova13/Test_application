from flask_restx import Resource, Api, apidoc, fields, Namespace
from flask import blueprints

router = Namespace('blazegraph', description='API for database interaction')
from .shema import STATUS_CODE_AND_MESSAGE_MAP
# a = router.model("sf", BaseAPIResponse)


@router.route("/fetch")
# @router.doc(BaseAPIResponse)
@router.doc(responses=STATUS_CODE_AND_MESSAGE_MAP)
# @router.param('id', 'The task identifier')
class InteractDB(Resource):

    @router.doc('kkkkkkkk')
    def get(self):
        """Get data from db"""
        return '<h1>Hello</h1>'
        # return BaseAPIResponse(status_code=200).model_dump_json()

    @router.doc('kkkkkkkk')
    def post(self):
        """Get data from db"""
        return '<h1>Hello</h1>'
        # return BaseAPIResponse(status_code=200).model_dump_json()