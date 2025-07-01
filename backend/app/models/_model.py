from app.db._conexion import get_connection

class MarcaModel:
    def __init__(self, id=None, nombre=None):
        self.id = id
        self.nombre = nombre

    def serializar(self):
        return {"id": self.id, "nombre": self.nombre}

    @staticmethod
    def deserializar(data):
        return MarcaModel(nombre=data["nombre"])

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM MARCAS")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_one(id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM MARCAS WHERE id = %s", (id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result

    def create(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO MARCAS (nombre) VALUES (%s)", (self.nombre,))
        conn.commit()
        self.id = cursor.lastrowid
        cursor.close()
        conn.close()
        return True

    def update(self, data):
        conn = get_connection()
        cursor = conn.cursor()
        self.nombre = data.get("nombre", self.nombre)
        cursor.execute("UPDATE MARCAS SET nombre = %s WHERE id = %s", (self.nombre, self.id))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    @staticmethod
    def delete(id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM MARCAS WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
