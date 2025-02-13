from flask import session, redirect

class Middleware:
    @staticmethod
    def protect_route(func):
        def decorated_function(*args, **kwargs):
            if not session.get("user"):
                return redirect("/login")
            return func(*args, **kwargs)
        return decorated_function
