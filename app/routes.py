from app import app
from flask import make_response, request

IP_LIMIT = 10


@app.route('/greet/<string:name>', methods=['GET'])
def greet(name):
    ip = request.remote_addr
    print(ip)
    reqs = requests_done(ip)
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


def requests_done(ip_address):
    return 1