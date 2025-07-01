from flask import Flask
from backend.app.routes.Marca_routes import marca_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(marca_bp, url_prefix="/marcas")
    return app
