#from crud.personas.persona import MostrarDatos
from models.estado_especial import TablaEstado
import time

class PanelControl:
    def __init__(self,conexion_db):
        self.conexion_db = conexion_db
        self.datos = []
    
    def cantidad_registros(self):
            """
            Retorna el número total de registros en la tabla 'persona'

            Args:
                conexion_db: Objeto de conexión a la base de datos

            Returns:
                int: Cantidad de registros
                None: Si ocurre un error
            """
            conexion, cursor = self.conexion_db.conexion()
            # Consulta optimizada para contar registros
            cursor.execute("SELECT COUNT(*) FROM persona")
            cantidad = cursor.fetchone()[0]
            return cantidad
        
    def registros_validos(self):
            """
            Retorna el número total de registros en la tabla 'persona' que cumplen con ser activos ademas de una lista
            
            Args:
            Returns:
                int: Cantidad de registros,
                list: registros
                None: Si ocurre un error
            """
            conexion, cursor = self.conexion_db.conexion()
            
            cursor.execute("SELECT * FROM PERSONA WHERE activo == 1")
            datos_validos = cursor.fetchall()
            
            
            # 2. Procesar cada registro
            estado = TablaEstado()
            resultados = []

            for registro in datos_validos:
                # Obtener estado especial para cada registro
                nombre_estado = estado.obtener_estado(registro[3], self.conexion_db)
                
                # Estructurar datos
                datos_persona = {
                    'id': registro[0],
                    'nombre': registro[1],
                    'apellidos': registro[2],
                    'nombre_completo': f"{registro[1]} {registro[2]}",
                    'manzana': registro[4],
                    'estado_especial': nombre_estado,
                    'estudia': "Sí" if registro[5] == 1 else "No",
                    'activo': "Activo" if registro[6] == 1 else "Inactivo",
                    'fecha_nacimiento': registro[7]
                }
                resultados.append(datos_persona)
                
            tamaño = len(resultados)
            self.datos = resultados
            return resultados, tamaño
        
    def promedio_edad(self):
        if not self.datos:
            return "No hay informacion cargada"
        año_actual =  time.now()       # Cambiar el time .now por el metodo correcto
        edades = [año_actual - registro[7] for registro in self.datos ]
        
        promedio = len(edades) / sum(edades)
        
        return promedio