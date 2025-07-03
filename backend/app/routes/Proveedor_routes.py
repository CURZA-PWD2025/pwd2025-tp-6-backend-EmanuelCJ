from flask import Blueprint, request, jsonify
from app.controlllers.Proveedor_controller import ProveedorController

proveedor_bp = Blueprint("proveedor_bp", __name__)

@proveedor_bp.route("/", methods=["GET"])
def get_all():
    return jsonify(ProveedorController.get_all())

@proveedor_bp.route("/<int:id>", methods=["GET"])
def get_one(id):
    return jsonify(ProveedorController.get_one(id))

@proveedor_bp.route("/", methods=["POST"])
def create():
    data = request.json
    return jsonify(ProveedorController.create(data))

@proveedor_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    data = request.json
    return jsonify(ProveedorController.update(id, data))

@proveedor_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return jsonify(ProveedorController.delete(id))
