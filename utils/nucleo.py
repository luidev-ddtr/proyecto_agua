import sqlite3
from datetime import datetime

class Conexion:
    """
    Clase la cual servira de conexión para que los datos puedan ser enviados a la bd.
    Se encarga de abrir, cerrar y manejar errores en la conexión.
    """

    def __init__(self, ruta):
        self.conn = sqlite3.connect(ruta)
        self.cursor = self.conn.cursor()

    def guardar_cambios(self):
        """
        Método que guarda los cambios en la base de datos y cierra la conexión.
        Si ocurre un error durante el commit o el cierre, se captura y se lanza una excepción.
        """
        try:
            # Intentar guardar los cambios
            self.conn.commit()
            print("Cambios guardados correctamente.")
        except sqlite3.Error as e:
            # Capturar errores durante el commit
            print(f"Error al guardar los cambios: {e}")
            raise
            
    def conexion(self):
        """
        Devuelve una tupla con las variables para la conexión.
        Si la conexión o el cursor no están inicializados, lanza una excepción.
        """
        try:
            if self.conn is None or self.cursor is None:
                raise sqlite3.Error("La conexión o el cursor no están inicializados.")
            print("Conexión enviada correctamente.")
            return self.conn, self.cursor
        except sqlite3.Error as e:
            print(f"Error al enviar conexiones: {e}")
            raise

    def cerrar_conexion(self):
        """
        Cierra la conexión y el cursor.
        Si ocurre un error, se captura y se lanza una excepción.
        """
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
            print("Conexión cerrada correctamente. (desde método cerrar_conexion)")
        except sqlite3.Error as e:
            print(f"Error al cerrar la conexión: {e}")
            raise

class Formateo:
    def formatear_fecha(self,fecha_string):
        try:
            fecha = datetime.strptime(fecha_string, "%Y-%m-%d")
            return int(fecha.strftime("%Y%m%d"))  # Convertir a formato YYYYMMDD
        except ValueError:
            print("Formato de fecha incorrecto. Usa YYYY-MM-DD.")
            return None
