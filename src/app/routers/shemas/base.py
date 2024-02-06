from enum import IntEnum
from starlette import status
from flask_restx import Namespace, fields

responses = Namespace("responses", description="API for database interaction")


class APIResponseStatusCode(IntEnum):
    ok = status.HTTP_200_OK
    nok = 467
    unauthenticated = status.HTTP_401_UNAUTHORIZED
    access_denied = status.HTTP_403_FORBIDDEN
    not_found = status.HTTP_404_NOT_FOUND


STATUS_CODE_AND_MESSAGE_MAP = {
    APIResponseStatusCode.ok: "Operation is successful",
    APIResponseStatusCode.nok: "Operation is not successful",
    APIResponseStatusCode.unauthenticated: "Invalid credentials",
    APIResponseStatusCode.access_denied: "Access Denied",
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

model_unauthenticated = responses.model(
    "ModelResponseUnauthenticated",
    {
        "status_code": fields.Integer(default=APIResponseStatusCode.unauthenticated),
        "status_message": fields.String(
            default=STATUS_CODE_AND_MESSAGE_MAP[APIResponseStatusCode.unauthenticated]
        ),
        "error_details": fields.List(fields.Nested(model_errors_data)),
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
model_access_denied = responses.model(
    "ModelResponseAccessDenied",
    {
        "status_code": fields.Integer(
            default=APIResponseStatusCode.access_denied,
            description="The query to be executed to retrieve data",
        ),
        "status_message": fields.String(
            default=STATUS_CODE_AND_MESSAGE_MAP[APIResponseStatusCode.access_denied]
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
BaseApiResponses = {
    APIResponseStatusCode.ok: STATUS_CODE_AND_MESSAGE_MAP[APIResponseStatusCode.ok],
    APIResponseStatusCode.nok: (
        STATUS_CODE_AND_MESSAGE_MAP[APIResponseStatusCode.nok],
        model_nok,
    ),
    APIResponseStatusCode.unauthenticated: (
        STATUS_CODE_AND_MESSAGE_MAP[APIResponseStatusCode.unauthenticated],
        model_unauthenticated,
    ),
    APIResponseStatusCode.access_denied: (
        STATUS_CODE_AND_MESSAGE_MAP[APIResponseStatusCode.access_denied],
        model_access_denied,
    ),
    APIResponseStatusCode.not_found: (
        STATUS_CODE_AND_MESSAGE_MAP[APIResponseStatusCode.not_found],
        model_not_found,
    ),
}
