
class  registros ():
    def mostrar_todos_los_datos(self, conexion_db):# -> list:
        """
        Obtiene y muestra todos los registros de personas con sus estados especiales.
        
        Args:
            conexion_db: Objeto de conexión a la base de datos
            
        Returns:
            list: Lista de diccionarios con los datos formateados de todas las personas
        """
        print("BANDERAMOSTAR1")
        # 1. Obtener conexión y ejecutar consulta
        conexion, cursor = conexion_db.conexion()
        print("BANDERAMOSTAR2")

        cursor.execute("""
            SELECT * FROM TOMA_AGUA
        """)

        print("BANDERAMOSTAR4")
        registros = cursor.fetchall()

        if not registros:
            print("No se encontraron registros en la tabla persona")
            return []
        print("BANDERAMOSTAR5")
        resultados = []

        for registro in registros:
            print(registro)
            print("BANDERAMOSTAR6")
            # Estructurar datos
            datos_registro = {
                'id_tomas': registro[0],
                'ubicacion': registro[1],
                'personas_usan': registro[2],
            }
            resultados.append(datos_registro)
            print("BANDERAMOSTAR7")
        
        return resultados
    