from bottle import route, run, debug, template, request, static_file, app, auth_basic, abort
import json
import os
import redis
from urllib.parse import urlparse


def is_authenticated(user, password):
    return user == "admin" and password == "fifa"


@route('/')
@auth_basic(is_authenticated)
def main():
    return template('web/index.tpl', filip=r.get('filip'), nikola=r.get('nikola'))


@route('/assets/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./web/assets')


@route('/logout', method=["GET", "POST"])
def logout():
    abort(401, "You have been logged out")


@route('/_operate')
def operate():
    id = request.params.get('id', 0, type=str)

    if id == "add_filip":
        previous = int(r.get('filip'))
        r.set('filip', previous + 1)
        element = 'filip'
        value = int(r.get('filip'))

    elif id == "subtract_filip":
        previous = int(r.get('filip'))
        r.set('filip', previous - 1)
        element = 'filip'
        value = int(r.get('filip'))

    elif id == "add_nikola":
        previous = int(r.get('nikola'))
        r.set('nikola', previous + 1)
        element = 'nikola'
        value = int(r.get('nikola'))

    elif id == "subtract_nikola":
        previous = int(r.get('nikola'))
        r.set('nikola', previous - 1)
        element = 'nikola'
        value = int(r.get('nikola'))

    return json.dumps({'result': value, 'element': '#' + element})


url = urlparse(os.environ.get('REDISCLOUD_URL'))
r = redis.Redis(host=url.hostname, port=url.port, password=url.password)
r.set('filip', 65)
r.set('nikola', 47)

# host="0.0.0.0"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
