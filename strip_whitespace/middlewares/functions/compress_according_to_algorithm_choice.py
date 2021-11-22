from typing import Union


def compress(
    buffer: bytes,
    algorithm: Union[
        str("gzip"),
        str("br"),
        str("zstd"),
        str("plain"),
    ] = str("gzip"),
):

    return_buffer: bytes = b""

    if algorithm == str('plain'):
        return_buffer = content
        
    elif algorithm == str("gzip"):
        from python_strip_whitespace.functions.compressors.gzip import (
            compress as gz_compress,
        )

        return_buffer = gz_compress(buffer)

    elif algorithm == str("br"):
        from python_strip_whitespace.functions.compressors.brotli import (
            compress as br_compress,
        )

        return_buffer = br_compress(buffer)

    elif algorithm == str("zstd"):
        from python_strip_whitespace.functions.compressors.zstd import (
            compress as zstd_compress,
        )

        return_buffer = zstd_compress(buffer)
    else:
        raise AttributeError

    return return_buffer
