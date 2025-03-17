from flask import Blueprint, request, jsonify, render_template
from app.controllers.heladeria_controller import HeladeriaController
from app.models.producto import Producto

productos_bp = Blueprint("productos", __name__)
heladeria_controller = HeladeriaController()


#esta es la ruta para listar todos los productos
@productos_bp.route("/", methods=["GET"])
def listar_productos():
    productos = Producto.query.all()
    productos_json = [
        {"id": p.id, "nombre": p.nombre, "precio": p.precio_publico}
        for p in productos
    ]
    
    return render_template("index.html", productos = productos)

# ruta pra agregar un nuevo producto
@productos_bp.route("/", methods=["POST"])
def agregar_producto():
    data = request.get_json()
    nombre = data.get("nombre")
    precio = data.get("precio")
    tipo = data.get("tipo")
    extra = data.get("extra")
    
    if not nombre or not precio or not tipo or not extra:
        return jsonify({"error": "Faltan datos obligatorios"}), 400
    
    try:
        heladeria_controller.agregar_producto(nombre, precio, tipo, extra)
        return jsonify({"mensaje": "Producto agregado exitosamente"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
#ruta para vender los produtos
@productos_bp.route("/vender", methods=["POST"])
def vender_producto():
    data = request.get_json()
    nombre = data.get("nombre")
    
    if not nombre:
        return jsonify({"error" : "Obligatorio el nombre del producto"}), 400
    
    resultado = heladeria_controller.realizar_venta(nombre)
    
    if resultado:
        return jsonify({"mensaje": "Venta realizada con exito"})
    else:
        return jsonify({"error": "producto no encontrado o sin stock"}), 400