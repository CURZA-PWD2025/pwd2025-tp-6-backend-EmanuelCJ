from flask import Blueprint, request, jsonify
from app.controlllers.Articulo_controller import ArticuloController

articulo_bp = Blueprint("articulo_bp", __name__)

@articulo_bp.route("/", methods=["GET"])
def get_all():
    return jsonify(ArticuloController.get_all())

@articulo_bp.route("/<int:id>", methods=["GET"])
def get_one(id):
    return jsonify(ArticuloController.get_one(id))

@articulo_bp.route("/", methods=["POST"])
def create():
    data = request.json
    return jsonify(ArticuloController.create(data))

@articulo_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    data = request.json
    return jsonify(ArticuloController.update(id, data))

@articulo_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return jsonify(ArticuloController.delete(id))
