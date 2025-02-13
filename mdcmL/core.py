from flask import Flask, request, session, redirect, url_for, jsonify, render_template

class MdcmL:
    def __init__(self, name):
        self.app = Flask(name)
        self.app.secret_key = "mdcmL_secret_key"
        self.routes = {}

    def route(self, path, methods=["GET"]):
        def decorator(func):
            self.routes[path] = func
            self.app.route(path, methods=methods)(func)
            return func
        return decorator

    def run(self, host="127.0.0.1", port=5000, debug=True):
        self.app.run(host=host, port=port, debug=debug)

    def render(self, template, **kwargs):
        return render_template(template, **kwargs)

    def redirect(self, endpoint):
        return redirect(url_for(endpoint))

    def json_response(self, data, status=200):
        return jsonify(data), status
