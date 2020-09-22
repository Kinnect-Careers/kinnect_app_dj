from .base import *

DEBUG = ENV.bool("DEBUG", default=True)

ALLOWED_HOSTS += [
    "localhost",
    "127.0.0.1",
    ENV("PUBLIC_IP"),
    ENV("PRIVATE_IP"),
]
