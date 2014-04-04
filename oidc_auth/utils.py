import json
from base64 import b64decode as python_b64decode

from .settings import oidc_settings


def scopes():
    scopes = set(oidc_settings.SCOPES)
    scopes.update({'openid', 'profile', 'email'})

    return ' '.join(scopes)


def b64decode(token):
    token += ('=' * (len(token) % 4))
    decoded = python_b64decode(token)
    return json.loads(decoded)
