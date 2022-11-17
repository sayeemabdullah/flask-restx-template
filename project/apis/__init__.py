from flask_restx import Api

from project.apis.alive import alive_namespace
from project.apis.something.api import something_namespace

api = Api(version="1.0", title="Project Name", prefix="/api/v1", doc="/docs")

api.add_namespace(alive_namespace, path="/alive")
api.add_namespace(something_namespace, path="/something")
