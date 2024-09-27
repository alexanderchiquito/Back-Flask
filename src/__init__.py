from flask import Flask, Response

# Routes
from .routes import IndexRoutes, AuthRoutes, StudentsRoutes, PorcentGeneralDesercionRoutes, ModeloRoute, DesercionRoutes

app = Flask(__name__)

def init_app(config):
    # Configuration
    app.config.from_object(config)
    
    # Blueprints
    app.register_blueprint(IndexRoutes.main, url_prefix='/')
    app.register_blueprint(AuthRoutes.main, url_prefix='/auth')
    app.register_blueprint(StudentsRoutes.main, url_prefix='/students')
    app.register_blueprint(PorcentGeneralDesercionRoutes.main, url_prefix='/porcentajeDesercion')
    app.register_blueprint(ModeloRoute.main, url_prefix='/entrenar_modelo')
    app.register_blueprint(DesercionRoutes.main, url_prefix='/desercion')


    @app.after_request
    def add_header(response: Response) -> Response:
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response

    return app
