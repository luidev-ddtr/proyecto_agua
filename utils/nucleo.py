# conexion_sqlserver.py
import pyodbc
from datetime import datetime

class Conexion:
    """
    Clase para manejar conexiones a SQL Server.
    Centraliza todas las operaciones de base de datos.
    """
    
    def __init__(self):
        """
        Inicializa la conexión a SQL Server usando los parámetros centralizados.
        """
        self.server = "ANGEL\\SQLEXPRESS"  # Cada quien debe configurar su servidor
        self.database = "GESTION_AGUA"
        self.conn = None
        self.cursor = None
        self._conectar()  # Serian un private de C#

    def _conectar(self):
        """
        Establece la conexión con la base de datos.
        """
        try:
            self.conn = pyodbc.connect(
                'DRIVER={SQL Server};'
                f'SERVER={self.server};'
                f'DATABASE={self.database};'
                'Trusted_Connection=yes;'
            )
            self.cursor = self.conn.cursor()
            print("Conexión establecida correctamente")
        except pyodbc.Error as e:
            print(f"Error al conectar a SQL Server: {e}")
            raise

    def guardar_cambios(self):
        """
        Guarda los cambios pendientes en la base de datos.
        """
        try:
            self.conn.commit()
        except pyodbc.Error as e:
            print(f"Error al guardar cambios: {e}")
            raise

    def conexion(self):
        """
        Devuelve la conexión y cursor activos.
        """
        if not self.conn or not self.cursor:
            raise pyodbc.Error("Conexión no está activa")
        return self.conn, self.cursor

    def cerrar_conexion(self):
        """
        Cierra la conexión de manera segura.
        """
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
            print("Conexión cerrada correctamente")
        except pyodbc.Error as e:
            print(f"Error al cerrar conexión: {e}")
            raise

    def ejecutar(self, consulta, parametros=None):
        """
        Ejecuta una consulta SQL con parámetros opcionales.
        
        Args:
            consulta (str): Consulta SQL a ejecutar
            parametros (tuple, optional): Parámetros para la consulta
            
        Returns:
            list: Resultados para consultas SELECT, None para otras
        """
        try:
            if parametros:
                self.cursor.execute(consulta, parametros)
            else:
                self.cursor.execute(consulta)
                
            if consulta.strip().upper().startswith('SELECT'):
                return self.cursor.fetchall()
            return None
        except pyodbc.Error as e:
            print(f"Error al ejecutar consulta: {e}")
            raise


class Formateo:
    def formatear_fecha(self,fecha_string):
        try:
            fecha = datetime.strptime(fecha_string, "%Y-%m-%d")
            return int(fecha.strftime("%Y%m%d"))  # Convertir a formato YYYYMMDD
        except ValueError:
            print("Formato de fecha incorrecto. Usa YYYY-MM-DD.")
            return None
        

if __name__ == "__main__":
    # Ejemplo de uso
    conexion = Conexion()
    
    conexion.conexion()
