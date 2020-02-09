from app import app
from flask import make_response, request
import redis
import time
import json

r = redis.Redis(host='redis', port=6379, db=0)

IP_LIMIT = 10
TIME_WINDOW = 60


@app.route('/greet/<string:name>', methods=['GET'])
def greet(name):
    ip = request.remote_addr
    print(ip)
    reqs = __requests_done(ip)
    if reqs <= IP_LIMIT:
        resp = app.make_response(f'Hi {name}!')
        resp.headers["X-RateLimit-Limit"] = IP_LIMIT
        resp.headers["X-RateLimit-Remaining"] = (IP_LIMIT - reqs)
        return resp, 200
    else:
        resp = app.make_response("Rate limit exceeded.")
        resp.headers["X-RateLimit-Limit"] = IP_LIMIT
        resp.headers["X-RateLimit-Remaining"] = 0
        return resp, 429


def __requests_done(ip_address):
    now = time.time()
    l = r.get(ip_address)
    if l != None:
        l = [t for t in json.loads(l) if now - t < TIME_WINDOW]
    else:
        l = []

    l.append(now)
    r.set(ip_address, json.dumps(l), ex=TIME_WINDOW)
    return len(l)