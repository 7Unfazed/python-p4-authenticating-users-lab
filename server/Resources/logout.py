from flask import session
from flask_restful import Resource

class LogoutResource(Resource):
    def delete(self):
        # Remove user_id from session to logout the user
        session.pop('user_id', None)
        return '', 204
