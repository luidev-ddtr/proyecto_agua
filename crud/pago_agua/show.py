#Logica para todos los metodos de mostrar datos al usuario
from crud.personas.persona import MostrarDatos as mostrar_persona
class MostrarDatos:
    def mostrar_registro(self, conexion_db):# -> None | dict[str, Any | set]:
        """
        Muestra un registro completo del pago de agua con formato legible.
        
        Args:
            indice (str): ID del registro a buscar
            conexion_db (object): Instancia de conexión a la base de datos
        Returns:
            dict/None: Diccionario con datos formateados o None si no existe
            
        Raises:
            DatabaseError: Si ocurre error en la consulta
            ValueError: Si el formato de fecha es inválido
        """
        conexion, cursor = conexion_db.conexion()
        
        query = """
        SELECT 
            ID_PAGO, ID_PERSONA, ID_TOMA, ESTADO_PAGO, CANTIDAD, ANIO, FECHA, TARIFA_PENDIENTE
        FROM PAGO_AGUA
        WHERE id = ?
        """
        cursor.execute(query, (indice,))
        registro = cursor.fetchone()
        
        if not registro:
            print(f"\n⚠️ No se encontró persona con ID {indice}\n")
            return None
        
        datos = {
            'id': registro[0],
            'id_persona': registro[1],
            'tomas_agua': {registro[2]},
            'año': registro[3],
            'fecha_pago': registro[4],
            'estado_pago': registro[5] ,#Logica para que muestre pendiente, pagado, parcial
            'cantidad': registro[6],
            'tarifa_pendiente': registro[7]
        }
        return datos
    
    def mostrar_todos_los_datos(self, conexion_db):
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
            SELECT * FROM PAGO_AGUA
        """)
        print("BANDERAMOSTAR4")
        registros = cursor.fetchall()
        if not registros:
            print("No se encontraron registros en la tabla persona")
            return []
        print("BANDERAMOSTAR5")
        resultados = []
        nombre_persona = mostrar_persona()
        for registro in registros:
            print(registro)
            "Se obtiene el nombre completo de la persona"
            datos  = nombre_persona.mostrar_registro_persona(registro[1],conexion_db)
            print("BANDERAMOSTAR6")
            # Estructurar datos
            datos_registro = {
                'id': registro[0],
                'id_persona': registro[1],
                ##Aqui cambia para meter el nombre de la persona y no solo datos como id
                # los cuales no le interesan al usuario 
                'nombre_completo': datos['nombre_completo'],
                'activo': datos['activo'],
                'tomas_agua': registro[2],
                'año': registro[3],
                'fecha_pago': registro[4],
                'estado_pago': registro[5] ,#Logica para que muestre pendiente, pagado, parcial
                'cantidad': registro[6],
                'tarifa_pendiente': registro[7]
                
            }
            resultados.append(datos_registro)
            print("BANDERAMOSTAR7")
        
        return resultados
    
    def mostrar_datos(self, registro):
        """
        Muestra los datos de un objeto Registro en formato crudo para testing
        
        Args:
            registro: Instancia de la clase Registro con los atributos:
                - id_persona
                - tomas_agua
                - año
                - fecha_pago
                - estado_pago (0=pendiente, 1=parcial, 2=completo)
                - cantidad
                - tarifa_pendiente
        """
        print("\nDatos del registro (formato crudo):")
        print(f"id_registrp: {registro.id}")
        print(f"id_persona: {registro.id_persona}")
        print(f"tomas_agua: {registro.tomas_agua}")
        print(f"año: {registro.año}")
        print(f"fecha_pago: {registro.fecha_pago}")
        print(f"estado_pago: {registro.estado_pago}")  # 0, 1 o 2
        print(f"cantidad: {registro.cantidad}")
        print(f"tarifa_pendiente: {registro.tarifa_pendiente}")
            
    def obtener_registro(self, indice,conn):
        """Metodo de testeo para verificar valores"""
        conexion, cursor = conn.conexion()
        query = """
        SELECT 
            id, nombre, apellidos, estado_especial,
            manzana, estudia, activo, fecha_nacimiento
        FROM persona
        WHERE id = ?
        """
        
        cursor.execute(query, (indice,))
        tabla = cursor.fetchall()
        
        print("Registro de la bd")
        for dato in tabla:
            print(dato)

if __name__ == '__main__':
    print("Menu de pagos agua")
    # conexion_bd = Conexion('base_datos/data_base.db')
    # visualizador = MostrarDatos()
    # indice = "cer-24-3321"
    # registro = visualizador.mostrar_registro(indice, conexion_bd)
    
    # for dato in registro:
    #     print(f"{dato}     {registro[dato]}")
    
    #conexion_bd.cerrar_conexion()