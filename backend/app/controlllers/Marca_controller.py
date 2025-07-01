from backend.app.models.Marca_model import MarcaModel

class MarcaController:

    @staticmethod
    def get_all():
        return MarcaModel.get_all()

    @staticmethod
    def get_one(id):
        return MarcaModel.get_one(id)

    @staticmethod
    def create(data):
        marca = MarcaModel.deserializar(data)
        marca.create()
        return marca.serializar()

    @staticmethod
    def update(id, data):
        marca_data = MarcaModel.get_one(id)
        if not marca_data:
            return {"error": "Marca no encontrada"}
        marca = MarcaModel(id=marca_data["id"], nombre=marca_data["nombre"])
        marca.update(data)
        return marca.serializar()

    @staticmethod
    def delete(id):
        return {"success": MarcaModel.delete(id)}
