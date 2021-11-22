from typing import Union
from django.http.request import HttpRequest
from django.http.response import HttpResponse


def add(
    request: HttpRequest,
    response: HttpResponse,
    algorithm: Union[
        str("gzip"),
        str("br"),
        str("zstd"),
        str("plain"),
    ] = str("gz"),
):
    accepted_encodings = request.META.get(
        "HTTP_ACCEPT_ENCODING", ""  # Has gzip, deflate by default
    )

    if algorithm in accepted_encodings:
        response.headers["Content-Encoding"] = algorithm
