import hmac
from hashlib import sha1
import uuid


def generate_random_key():
    unique = uuid.uuid4()
    return hmac.new(unique.bytes, digestmod=sha1).hexdigest()