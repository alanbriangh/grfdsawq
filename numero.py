import base64
import zlib

def compress_and_encode(data):
    compressed_data = zlib.compress(data)
    encoded_data = base64.b64encode(compressed_data)
    return encoded_data

def decode_and_decompress(encoded_data):
    compressed_data = base64.b64decode(encoded_data)
    data = zlib.decompress(compressed_data)
    return data

encoded_data = "eJwFQLEJACAM+8jsfuAZIkUdSsQGxO/Lkk5UQG9LdsugI/iteZ9MpokLKA=="
data = decode_and_decompress(encoded_data)

print(data)
