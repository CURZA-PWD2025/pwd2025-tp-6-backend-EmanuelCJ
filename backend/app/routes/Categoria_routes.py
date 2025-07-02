from flask import Blueprint, request, jsonify
from app.controlllers.Categoria_controller import CategoriaController

categoria_bp = Blueprint("categoria_bp", __name__)

@categoria_bp.route("/", methods=["GET"])
def get_all():
    return jsonify(CategoriaController.get_all())

@categoria_bp.route("/<int:id>", methods=["GET"])
def get_one(id):
    return jsonify(CategoriaController.get_one(id))

@categoria_bp.route("/", methods=["POST"])
def create():
    data = request.json
    return jsonify(CategoriaController.create(data))

@categoria_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    data = request.json
    return jsonify(CategoriaController.update(id, data))

@categoria_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return jsonify(CategoriaController.delete(id))
