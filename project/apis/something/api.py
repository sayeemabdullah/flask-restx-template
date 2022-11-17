
from attr import validate
from flask import request, current_app as app
from project import bcrypt
from flask_restx import Namespace, Resource, fields
from werkzeug.utils import secure_filename
import requests

something_namespace = Namespace("something")


something_model = something_namespace.model(
    "something_model",
    {
        "something": fields.Boolean(required=True),
    },
)

something_response_model = something_namespace.model(
    "something_response_model",
    {
        "something": fields.Boolean(required=True),
        "message": fields.String(required=True),
    },
)


class PostSomething(Resource):
    @something_namespace.expect(something_model, validate=True)
    @something_namespace.response(200, "Something has been done successfully.")
    @something_namespace.response(404, "Something has not been done.")
    def post(self):
        data = request.get_json()
        something = data.get('something')
        if something:
            responseObject = {
                "something": something,
                "message": "Something has been done successfully!"
            }
            return responseObject, 200
        else:
            something_namespace.abort(
                404, f"Something has not been done.")


class GetSomething(Resource):
    @something_namespace.response(200, "You got something.")
    def get(self):
        return {"message": "You got something."}, 200


something_namespace.add_resource(
    GetSomething, "/get-something", endpoint="get-something")
something_namespace.add_resource(
    PostSomething, "/post-something", endpoint="post-something")
