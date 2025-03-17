from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__, template_folder=os.path.abspath('app/views'))
    app.config.from_object(Config)
    
    #Aqui se debe inicializar la base de datos
    db.init_app(app)
    migrate.init_app(app,db)
    
    from app.models.ingrediente import Ingrediente, Base, Complemento
    from app.models.heladeria import Heladeria
    from app.models.producto import Producto
    
    #Aqui registramos el controlador
    from app.routes.productos import productos_bp
    from app.routes.heladeria_routes import heladeria_bp
    app.register_blueprint(heladeria_bp, url_prefix='/heladeria')
    app.register_blueprint(productos_bp, url_prefix='/productos')
    
    return app