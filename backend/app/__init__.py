from flask import Flask
from flask_cors import CORS 

from app.routes.Marca_routes import marca_bp
from app.routes.Categoria_routes import categoria_bp
from app.routes.Proveedor_routes import proveedor_bp
from app.routes.Articulo_routes import articulo_bp

def create_app():
    app = Flask(__name__)
    CORS(app)  # Habilitar CORS para todas las rutas

    app.register_blueprint(marca_bp, url_prefix="/marcas")
    app.register_blueprint(proveedor_bp, url_prefix="/proveedores")
    app.register_blueprint(categoria_bp, url_prefix="/categorias")
    app.register_blueprint(articulo_bp, url_prefix="/articulos")

    @app.route("/")
    def home():
        return "API Flask funcionando correctamente"

    return app

