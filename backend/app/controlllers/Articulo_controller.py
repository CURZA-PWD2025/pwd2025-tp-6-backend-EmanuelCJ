from app.models.Articulo_model import ArticuloModel

class ArticuloController:

    @staticmethod
    def get_all():
        return ArticuloModel.get_all()

    @staticmethod
    def get_one(id):
        return ArticuloModel.get_one(id)

    @staticmethod
    def create(data):
        articulo = ArticuloModel.deserializar(data)
        articulo.create()
        return articulo.serializar()

    @staticmethod
    def update(id, data):
        art_data = ArticuloModel.get_one(id)
        if not art_data:
            return {"error": "Artículo no encontrado"}
        articulo = ArticuloModel(**art_data)
        articulo.update(data)
        return articulo.serializar()

    @staticmethod
    def delete(id):
        return {"success": ArticuloModel.delete(id)}
