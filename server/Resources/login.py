from flask import request, jsonify, session
from flask_restful import Resource
from models import User  # Import your User model here

class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')

        if not username:
            return {'message': 'Username is required'}, 400

        user = User.query.filter_by(username=username).first()

        if not user:
            return {'message': 'User not found'}, 404

        session['user_id'] = user.id

        return jsonify(user.serialize()), 200
