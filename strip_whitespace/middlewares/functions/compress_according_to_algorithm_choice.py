def compress(
    buffer: bytes,
    algorithm: str("gzip") | str("br") | str("zstd") | str("plain") = str("gzip"),
) -> bytes:
    # HTML should always be sent in bytes 🔢
    return_buffer: bytes = b""

    if algorithm == str("gzip"):
        try:
            from python_strip_whitespace.functions.compressors.gzip import (
                compress as gz_compress,
            )

        except ImportError:
            raise ImportError(
                """
                'gz_compress' function is missing

                    Did you install the latest python_strip_whitespace?
                    
                    If not install it by:
                        python -m pip install python_strip_whitespace
                """
            )

        return_buffer = gz_compress(buffer)

    elif algorithm == str("br"):
        try:
            from python_strip_whitespace.functions.compressors.brotli import (
                compress as br_compress,
            )

        except ImportError:
            raise ImportError(
                """
                'br_compress' function is missing

                    Did you install the latest python_strip_whitespace?
                    
                    If not install it by:
                        python -m pip install python_strip_whitespace
                """
            )

        return_buffer = br_compress(buffer)

    elif algorithm == str("zstd"):
        try:
            from python_strip_whitespace.functions.compressors.zstd import (
                compress as zstd_compress,
            )

        except ImportError:
            raise ImportError(
                """
                'zstd_compress' function is missing

                    Did you install the latest python_strip_whitespace?
                    
                    If not install it by:
                        python -m pip install python_strip_whitespace
                """
            )

        return_buffer = zstd_compress(buffer)
    else:
        raise AttributeError(
            f"""
            
            Error in 'strip_whitespace.middlewares.functions.compress_according_to_algorithm_choice'
                    Compression algorithm not any of these:
                        |> str("gzip")
                        |> str("br")
                        |> str("zstd")
                        |> str("plain")

                    Currently the Algorithm is : { algorithm }
            """
        )

    return return_buffer
