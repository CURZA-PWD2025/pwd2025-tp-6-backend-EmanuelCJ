from app.models.Proveedor_model import ProveedorModel

class ProveedorController:

    @staticmethod
    def get_all():
        return ProveedorModel.get_all()

    @staticmethod
    def get_one(id):
        return ProveedorModel.get_one(id)

    @staticmethod
    def create(data):
        proveedor = ProveedorModel.deserializar(data)
        proveedor.create()
        return proveedor.serializar()

    @staticmethod
    def update(id, data):
        proveedor_data = ProveedorModel.get_one(id)
        if not proveedor_data:
            return {"error": "Proveedor no encontrado"}

        proveedor = ProveedorModel(**proveedor_data)
        proveedor.update(data)
        return proveedor.serializar()

    @staticmethod
    def delete(id):
        return {"success": ProveedorModel.delete(id)}
