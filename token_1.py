from itsdangerous import URLSafeTimedSerializer
from key import salt
def encode(data):
    serializer=URLSafeTimedSerializer('Yamini@123')
    return serializer.dumps(data,salt=salt)
def decode(data):
    serializer=URLSafeTimedSerializer('Yamini@123')
    return serializer.loads(data,salt=salt)
