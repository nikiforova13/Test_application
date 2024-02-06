from enum import IntEnum
from starlette import status
import typing
from pydantic import BaseModel, Field

class APIResponseStatusCode(IntEnum):
    ok = status.HTTP_200_OK
    nok = 467
    unauthenticated = status.HTTP_401_UNAUTHORIZED
    access_denied = status.HTTP_403_FORBIDDEN
    not_found = status.HTTP_404_NOT_FOUND

STATUS_CODE_AND_MESSAGE_MAP = {
    APIResponseStatusCode.ok.value:"Operation is successful",
    APIResponseStatusCode.nok.value: "Operation is not successful",
    APIResponseStatusCode.unauthenticated.value: "Invalid credentials",
    APIResponseStatusCode.access_denied.value: "Access Denied",
    APIResponseStatusCode.not_found.value: "Not found",
}


# class BaseAPIResponse(BaseModel):
#     """
#     Base API response model
#     """
#
#     status_code: int = Field(default=APIResponseStatusCode.ok, description="HTTP status code")
#     status_message: str = Field(
#         default=_STATUS_CODE2MESSAGE_MAP[APIResponseStatusCode.ok],
#         description="Overall operation status description; " "can be used 'as is' in API client",
#         examples=[_STATUS_CODE2MESSAGE_MAP[APIResponseStatusCode.ok]],
#     )
#
#     # TODO: Improve error schema in OpenAPI
#     error_details: list[dict[str, typing.Any]] | None = Field(
#         default=None, description="Error details; empty for successful operations"
#     )