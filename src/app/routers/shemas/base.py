from enum import IntEnum

from flask_restx import Namespace, fields  # type: ignore
from starlette import status

responses = Namespace("responses", description="API for database interaction")


class APIResponseStatusCode(IntEnum):
    ok = status.HTTP_200_OK
    nok = 467
    not_found = status.HTTP_404_NOT_FOUND


STATUS_CODE_AND_MESSAGE_MAP = {
    APIResponseStatusCode.ok: "Operation is successful",
    APIResponseStatusCode.nok: "Operation is not successful",
    APIResponseStatusCode.not_found: "Not found",
}


model_errors_data = responses.model(
    "Errors",
    {
        "Error": fields.String(
            default=None, description="Error details; empty for successful operations"
        )
    },
)


model_nok = responses.model(
    "ModelResponseNok",
    {
        "status_code": fields.Integer(
            default=APIResponseStatusCode.nok,
            description="The query to be executed to retrieve data",
        ),
        "status_message": fields.String(
            default=STATUS_CODE_AND_MESSAGE_MAP[APIResponseStatusCode.nok]
        ),
        "error_details": fields.List(fields.Nested(model_errors_data)),
    },
)


model_not_found = responses.model(
    "ModelResponseNotFound",
    {
        "status_code": fields.Integer(
            default=APIResponseStatusCode.not_found,
            description="The query to be executed to retrieve data",
        ),
        "status_message": fields.String(
            default=STATUS_CODE_AND_MESSAGE_MAP[APIResponseStatusCode.not_found]
        ),
        "error_details": fields.List(fields.Nested(model_errors_data)),
    },
)
BaseApiResponse = {
    APIResponseStatusCode.ok: STATUS_CODE_AND_MESSAGE_MAP[APIResponseStatusCode.ok],
    APIResponseStatusCode.nok: (
        STATUS_CODE_AND_MESSAGE_MAP[APIResponseStatusCode.nok],
        model_nok,
    ),
    APIResponseStatusCode.not_found: (
        STATUS_CODE_AND_MESSAGE_MAP[APIResponseStatusCode.not_found],
        model_not_found,
    ),
}
