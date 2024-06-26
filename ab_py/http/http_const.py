from enum import Enum


class RequestType(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


class HTTPConst:
    APPLICATION_JSON = "application/json"
    SUCCESS = "success"
    ERROR = "error"
    UTF8_ENCODING = "utf-8"
