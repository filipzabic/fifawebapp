from flask import Flask, request, abort, redirect, url_for, make_response
from flask import render_template as template
import jwt
import base64
import json
import os
import redis
from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder='templates', static_folder='static')
route = app.route


@route('/')
def main():
    return template('index.html', filip=int(r.get('filip')), nikola=int(r.get('nikola')))


@route('/logout')
def logout():
    resp = make_response()
    resp.set_cookie('access.5nx86dyn', '', expires=0)

    return resp

@route('/test')
def login():
    return template('login.html')


@route('/_operate')
def operate():
    id = request.args.get('id', 0, type=str)

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


host = os.environ.get('REDISCLOUD_URL')
password = os.environ.get('REDIS_PASSWORD')
port = os.environ.get('PORT')

r = redis.Redis(host=host, port=port, password=password)

if r.exists('set'):
    pass
else:
    r.set('set', 1)
    r.set('filip', 47)
    r.set('nikola', 65)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
