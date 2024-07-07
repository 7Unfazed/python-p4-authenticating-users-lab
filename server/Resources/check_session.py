from flask import jsonify, session
from flask_restful import Resource
from models import User  # Import your User model here

class CheckSessionResource(Resource):
    def get(self):
        user_id = session.get('user_id')

        if user_id:
            # Assuming User model has a method to retrieve user by user_id
            user = User.query.get(user_id)
            if user:
                return jsonify(user.serialize()), 200
            else:
                return {'message': 'User not found'}, 404
        else:
            return '', 401
