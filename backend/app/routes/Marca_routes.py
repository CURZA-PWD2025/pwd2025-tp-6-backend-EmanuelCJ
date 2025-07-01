from flask import Blueprint, request, jsonify
from backend.app.controlllers.Marca_controller import MarcaController

marca_bp = Blueprint("marca_bp", __name__)

@marca_bp.route("/", methods=["GET"])
def get_all():
    return jsonify(MarcaController.get_all())

@marca_bp.route("/<int:id>", methods=["GET"])
def get_one(id):
    return jsonify(MarcaController.get_one(id))

@marca_bp.route("/", methods=["POST"])
def create():
    data = request.json
    return jsonify(MarcaController.create(data))

@marca_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    data = request.json
    return jsonify(MarcaController.update(id, data))

@marca_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    return jsonify(MarcaController.delete(id))
