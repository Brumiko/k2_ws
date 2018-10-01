from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework.response import Response


def handle_exception(exc, context):
    # pass
    response = exception_handler(exc=exc, context=context)
    # TODO!
    if response is None:
        response = Response()
        data = {'detail': str(exc)}
        response.data = data
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return response
