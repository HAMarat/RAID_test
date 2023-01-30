from flask_restx import Resource, Namespace

from dao.model.framework import FrameworkSchema
from implemented import framework_service

framework_ns = Namespace('frameworks')


@framework_ns.route('/')
class FrameworkView(Resource):
    def get(self):
        frameworks = framework_service.get_all()
        return FrameworkSchema(many=True).dump(frameworks), 200


@framework_ns.route('/<language>')
class FrameworksView(Resource):
    def get(self, language):
        framework = framework_service.get_filter_by_language(language)
        return FrameworkSchema().dump(framework), 200
