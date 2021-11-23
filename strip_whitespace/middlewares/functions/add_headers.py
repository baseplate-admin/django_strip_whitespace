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

    if algorithm == str("plain"):
        # If algorithm is text/plain rdon't do anything
        response.headers["Content-Encoding"] = "text/plain; charset:utf-8"

    elif algorithm != str("plain") and algorithm in accepted_encodings:
        response.headers["Content-Encoding"] = algorithm

    else:
        raise ValueError(
            f"""
                'algorithm' in 'strip_whitespace.add_header' must be one of these four.
                    1. gzip
                    2. br ( Brotli )
                    3. zstd ( ZStandard )
                    4. plain ( Decompressed HTML )

                Currently algorithm is: { algorithm }
            """
        )
