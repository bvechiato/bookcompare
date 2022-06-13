import redis
from app.models import Book

r = redis.Redis(host='localhost', port=6379)

def check(key) -> bool:
    return r.exists(key)

def set(key, value: Book):
    value = str(value)
    r.setex(key, 172800, value)

def get(key) -> list[str]:
    decoded = r.get(key).decode('UTF-8')
    return decoded.split(", ")

def get_all() -> list[list[str]]:
    # get keys
    keys = r.keys()
    
    # get values
    values = []
    for key in keys:
        values.append(get(key))
    
    return values
