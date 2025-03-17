from flask import Blueprint, request, jsonify
from app.controllers.heladeria_controller import HeladeriaController

heladeria_bp = Blueprint('heladeria', __name__)
controller = HeladeriaController()

@heladeria_bp.route("/")
def home():
    return "Bienvenida a la heladeria web"

@heladeria_bp.route('/agregar_producto', methods=['POST'])
def agregar_producto():
    data = request.json
    controller.agregar_producto(data['nombre'], data['precio'], data['tipo'], data['extra'])
    return jsonify({"mensaje": "Producto agreagado"}) , 200


@heladeria_bp.route('/vender', methods = ['POST'])
def vender():
    data = request.json
    vendido = controller.realizar_venta(data['nombre'])
    return jsonify({"vendido": vendido})