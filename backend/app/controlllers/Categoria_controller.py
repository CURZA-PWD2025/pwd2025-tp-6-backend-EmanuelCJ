from app.models.Categoria_model import CategoriaModel

class CategoriaController:

    @staticmethod
    def get_all():
        return CategoriaModel.get_all()

    @staticmethod
    def get_one(id):
        return CategoriaModel.get_one(id)

    @staticmethod
    def create(data):
        categoria = CategoriaModel.deserializar(data)
        categoria.create()
        return categoria.serializar()

    @staticmethod
    def update(id, data):
        cat_data = CategoriaModel.get_one(id)
        if not cat_data:
            return {"error": "Categoría no encontrada"}
        categoria = CategoriaModel(id=cat_data["id"], nombre=cat_data["nombre"])
        categoria.update(data)
        return categoria.serializar()

    @staticmethod
    def delete(id):
        return {"success": CategoriaModel.delete(id)}
