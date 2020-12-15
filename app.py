from bottle import route, run, debug, template, request, static_file, app, auth_basic, abort
import json
import os

with open("results.json", 'r') as file:
    results = json.load(file)


def is_authenticated(user, password):
    return user == "admin" and password == "fifa"


@route('/')
@auth_basic(is_authenticated)
def main():
    return template('web/index.tpl', filip=results['filip'], nikola=results['nikola'])


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
        results['filip'] = results['filip'] + 1
        element = 'filip'
        value = results['filip']
        print(value)

    elif id == "subtract_filip":
        results['filip'] = results['filip'] - 1
        element = 'filip'
        value = results['filip']

    elif id == "add_nikola":
        results['nikola'] = results['nikola'] + 1
        element = 'nikola'
        value = results['nikola']

    elif id == "subtract_nikola":
        results['nikola'] = results['nikola'] - 1
        element = 'nikola'
        value = results['nikola']

    with open('results.json', 'w') as file:
        json.dump(results, file)

    return json.dumps({'result': value, 'element': '#' + element})


run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
