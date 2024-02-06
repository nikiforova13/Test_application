from flask_restx import Resource, Namespace, fields
from flask import request, abort, Response

def handler_request(requests: request):
    print(request.json)
    json_data = request.json
    print(f'sljfdkjfkdjf {json_data}')
    if not json_data:
        abort(Response('Not found', status=404))

