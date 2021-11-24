from typing import Union

# Django import
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
    accepted_encodings = request.META.get("HTTP_ACCEPT_ENCODING", "")

    if algorithm == str("plain"):
        """
        If algorithm is text/plain don't do anything 🤷‍♂️
        """

        response.headers["Content-Encoding"] = "text/plain; charset:utf-8"

    elif algorithm != str("plain") and algorithm in accepted_encodings:
        """
        Developer has chosen an algorithm that's not accepted by the browser.
            So do as the developer says 😄
        """

        response.headers["Content-Encoding"] = algorithm

    elif algorithm != str("plain") and algorithm not in accepted_encodings:
        """
        Developer has chosen an algorithm that's not accepted by the browser. 🤦‍♂️
            So raise an error and explain the error.
        """

        raise ValueError(
            f"""
            Error in 'strip_whitespace.middlewares.functions.add_headers'

                Accepted HTTP ENCODING = { accepted_encodings }

                    Please switch { algorithm } to any of these : { accepted_encodings } in settings.py
        """
        )

    else:
        # Something crazy is going on here. 😱 ( There might be ghosts lurking around here 👀 )

        raise ValueError(
            f"""
                'algorithm' in 'strip_whitespace.add_header' must be one of these:
                    |> gzip
                    |> br ( Brotli )
                    |> zstd ( ZStandard )
                    |> plain ( Decompressed HTML )

                Currently the algorithm is: { algorithm }
            """
        )
