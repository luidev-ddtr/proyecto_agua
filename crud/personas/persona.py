#Crud unificado de persona
import sqlite3
from models.clase_abstracta import BaseDatos
from models.personas import Persona
from models.estado_especial import TablaEstado
from utils.nucleo import Conexion
class TablaPersona(BaseDatos):
    def cantidad_registros(self,conexion_db):
        """
        Retorna el número total de registros en la tabla 'persona'

        Args:
            conexion_db: Objeto de conexión a la base de datos

        Returns:
            int: Cantidad de registros
            None: Si ocurre un error
        """
        conexion, cursor = conexion_db.conexion()
        # Consulta optimizada para contar registros
        cursor.execute("SELECT COUNT(*) FROM persona")
        cantidad = cursor.fetchone()[0]
        return cantidad

    def agregar_dato(self, persona, conexion_db):
        """
        Agrega un nuevo registro a la tabla 'persona' en la base de datos.

        Args:
            persona (Persona): Instancia de la clase Persona con los datos a insertar.
            conexion_db (Conexion): Instancia para manejar la conexión a la base de datos.

        Raises:
            sqlite3.Error: Si ocurre un error durante la inserción.

        Notas:
            - La tabla persona espera 8 columnas (id, nombre, apellidos, estado_especial,
            manzana, estudia, activo, fecha_nacimiento)
            - Todos los valores se pasan como parámetros para prevenir inyección SQL
        """
        try:
            conexion, cursor = conexion_db.conexion()
            query = """
            INSERT INTO persona
            (id, nombre, apellidos, estado_especial, manzana, estudia, activo, fecha_nacimiento)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """

            valores = (
                persona.id_persona,
                persona.nombre,
                persona.apellidos,
                persona.estado_especial,
                persona.manzana,
                persona.estudia,
                persona.activo,
                persona.fecha_nac
            )

            cursor.execute(query, valores)
            conexion_db.guardar_cambios()
            print("✅ Datos insertados correctamente.")

        except sqlite3.Error as e:
            print(f"❌ Error al insertar datos: {e}")
            # Rollback automático ocurre al salir del bloque try
            raise

    def obtener_datos(self, indice,persona, conexion_db):
        """
        Hidrata un objeto Persona con datos desde la base de datos.

        Args:
            persona (Persona): Instancia vacía/parcial a hidratar
            indice (str): ID de la persona a buscar
            conexion_db (Conexion): Objeto para manejar la conexión

        Returns:
            Persona: La misma instancia recibida, ahora con datos cargados
            None: Si no se encontró el registro

        Raises:
            ValueError: Si el objeto persona es None
            sqlite3.Error: Para errores de base de datos
        """

        if not isinstance(indice, int):
            raise TypeError("El valor de 'indice' debe ser un número entero.")
        try:

            # Obtener la conexión y el cursor
            conexion, cursor = conexion_db.conexion()

            # Consulta SQL parametrizada
            query = "SELECT nombre, apellidos, estado_especial, manzana, estudia, fecha_nacimiento FROM persona WHERE id = ?"

            # Ejecutar la consulta
            cursor.execute(query, (indice,))

            # Obtener los datos
            datos = cursor.fetchone()

            if not datos:
                return None
            # Llamar a crear_persona con los datos obtenidos
            return persona(
                nombre=datos[0],
                apellidos=datos[1],
                estado_especial=datos[2],
                manzana=datos[3],
                estudia=datos[4],
                fecha_nac=datos[5],
                id_persona = indice
            )

        except sqlite3.Error as e:
            print(f"Error al obtener datos: {e}")
            raise

    def agregar_muchos_datos(self, lista_personas, clase_persona, conn):
        """
        Agrega múltiples registros a la tabla 'persona' recibiendo datos en formato JSON/diccionario.

        :param lista_personas: Lista de diccionarios con los datos de las personas.
                Formato esperado:
                {
                    'nombre': str,
                    'apellidos': str,
                    'estado_especial': int,
                    'manzana': str,
                    'estudia': int (0/1),
                    'fecha_nac': str (formato yyyy-mm-dd)
                }
        :param clase_persona: Instancia de la clase Persona que contiene la lógica de formateo.
        :param conn: Instancia de la clase Conexion.
        :raises sqlite3.Error: Si ocurre un error durante la inserción.
        """
        conexion, cursor = conn.conexion()
        # Definir la consulta SQL
        query = """
        INSERT INTO persona (
            id,
            nombre,
            apellidos,
            estado_especial,
            manzana,
            estudia,
            activo,
            fecha_nacimiento
        ) VALUES (?,?, ?, ?, ?, ?, ?, ?)
        """
        valores = []
        for persona_data in lista_personas:
            # Configurar los datos usando el método de la clase Persona
            persona = clase_persona(persona_data['nombre'],persona_data['apellidos'],persona_data["estado_especial"],
                            persona_data['manzana'],persona_data['estudia'],persona_data['fecha_nacimiento']
            )
            # Preparar tupla de valores para la inserción
            valores.append((
                persona.id_persona,
                persona.nombre,
                persona.apellidos,
                int(persona.estado_especial),
                persona.manzana,
                int(persona.estudia),  # Aseguramos que sea 0 o 1
                int(persona.activo),   # Aseguramos que sea 0 o 1
                persona.fecha_nac
            ))
        # Ejecutar la consulta con executemany
        cursor.executemany(query, valores)
        # Guardar los cambios
        conn.guardar_cambios()

    def modificar_dato(self, objeto, conexion_db):
        """
        Modifica los datos editables de una persona en la base de datos.
        
        Args:
            objeto (Persona): Instancia de Persona con la información actualizada
            conexion_db (Conexion): Instancia de la clase Conexion
        
        Returns:
            bool: True si la actualización fue exitosa, False si hubo error
        """
        conexion, cursor = conexion_db.conexion()
        
        print("Imprimiendo valor persona")
        print(objeto.nombre)
        print(objeto.apellidos)
        print(objeto.estado_especial)
        print(objeto.estudia)
        print(objeto.activo)
        print(objeto.id_persona)
        
        # Consulta SQL con campos editables (incluyendo activo)
        consulta_sql = """
            UPDATE persona 
            SET nombre = ?, 
                apellidos = ?, 
                estado_especial = ?, 
                estudia = ?,
                activo = ?
            WHERE id = ?
        """
        
        # Valores para la consulta (campos editables + ID para WHERE)
        valores = (
            objeto.nombre,
            objeto.apellidos,
            objeto.estado_especial,
            objeto.estudia,
            objeto.activo,  # Incluido según tu comentario
            objeto.id_persona      # Solo para identificar el registro a actualizar
        )
        
        # Ejecutar la consulta
        cursor.execute(consulta_sql, valores)
        
        # Verificar si se actualizó algún registro
        if cursor.rowcount == 0:
            print(f"⚠️ No se actualizó el registro ID: {objeto.id_persona}. Verifica si existe.")
            return False
        
        conexion_db.guardar_cambios()
        print(f"✅ Registro ID: {objeto.id_persona} actualizado correctamente.")
        return True
    

    def eliminar_dato(self, id_persona, conexion_db):
        """
        Elimina un registro de persona de la base de datos.

        Parámetros:
        :param id_persona: ID del registro a eliminar (int)
        :param conexion_db: Instancia de la clase Conexion

        Returns:
        int: Número de registros eliminados (0 si no existía, 1 si se eliminó)
        """
        conexion, cursor = conexion_db.conexion()
        query = "DELETE FROM persona WHERE id = ?"
        cursor.execute(query, (id_persona,))
        registros_eliminados = cursor.rowcount
        conexion_db.guardar_cambios()
        return registros_eliminados
    
    def buscar_nombre(self, busqueda, conexion_bd):
        """
        Método que ejecuta la consulta SQL real
        
        Args:
            busqueda (str): Término a buscar
            conexion_bd (Conexion): Objeto de conexión
            
        Returns:
            list: Resultados formateados
        """
        conn, cursor = conexion_bd.conectar()
        
        # Dividir términos de búsqueda
        terminos = [t.strip() for t in busqueda.split() if t.strip()]
        
        if not terminos:
            return []
        
        # Construir consulta segura
        query = """
            SELECT id, nombre 
            FROM personas 
            WHERE {}
            LIMIT 20
        """.format(" OR ".join(["nombre LIKE ?"] * len(terminos)))
        
        # Parámetros con comodines para cada término
        params = [f"%{t}%" for t in terminos]
        
        cursor.execute(query, params)
        rows = cursor.fetchall()
        
        # Formatear resultados
        return [{"id": row[0], "nombre": row[1]} for row in rows]

class MostrarDatos:
    """Estra clase es especifica para la tabla y objeto persona por lo que se tiene que hacer mas general
    Se busca que  cada clase que la utilize tenga un objeto para que pueda mostrarse el nombre correctamente,
    Se debe verificar si es nesesario buscar el nombre o solo las columnas

    Se tienen que obtener las columas y tambien para mostrarlas dinamicamente
    """
    def mostrar_registro_persona(self, indice, conexion_db):
        """
        Muestra un registro completo de persona con formato legible.

        Args:
            indice (str): ID de la persona a buscar
            conexion_db (object): Instancia de conexión a la base de datos

        Returns:
            dict/None: Diccionario con datos formateados o None si no existe

        Raises:
            DatabaseError: Si ocurre error en la consulta
            ValueError: Si el formato de fecha es inválido
        """
        # 1. Conexión, consulta e inicializacion de clases
        estado = TablaEstado()
        conexion, cursor = conexion_db.conexion()

        query = """
        SELECT
            id, nombre, apellidos, estado_especial,
            manzana, estudia, activo, fecha_nacimiento
        FROM persona
        WHERE id = ?
        """
        cursor.execute(query, (indice,))
        registro = cursor.fetchone()

        if not registro:
            print(f"\n⚠️ No se encontró persona con ID {indice}\n")
            return None
        nombre_estado = estado.obtener_estado(registro[3], conexion_db)  # índice 3 para estado_especial

        datos = {
            'id': registro[0],
            'nombre_completo': f"{registro[1]} {registro[2]}",
            'manzana': registro[4] or "No especificada",
            'estado_especial': nombre_estado,
            'estudia': "Sí" if registro[5] == 1 else "No",
            'activo': "Activo" if registro[6] == 1 else "Inactivo",
            'fecha_nacimiento': registro[7]
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
        # 1. Obtener conexión y ejecutar consulta
        conexion, cursor = conexion_db.conexion()
        cursor.execute("""
            SELECT id, nombre, apellidos, estado_especial,
                manzana, estudia, activo, fecha_nacimiento
            FROM persona
        """)

        registros = cursor.fetchall()
        if not registros:
            print("No se encontraron registros en la tabla persona")
            return []

        # 2. Procesar cada registro
        estado = TablaEstado()
        resultados = []

        for registro in registros:
            # Obtener estado especial para cada registro
            nombre_estado = estado.obtener_estado(registro[3], conexion_db)
            
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
        return resultados

    def mostrar_datos(self, objeto):
        """
        Muestra los datos de la persona.

        :param objeto es el objeto persona que se quiere mostrar, sirve mas de testeo
        """
        print("\nDatos de la persona:")
        print(f"ID: {objeto.id_persona}")
        print(f"Nombre: {objeto.nombre} {objeto.apellidos}")
        print(f"Estado especial: {objeto.estado_especial}")
        print(f"Manzana: {objeto.manzana}")
        print(f"Estudia: {objeto.estudia}")
        print(f"Fecha de nacimiento: {objeto.fecha_nac}")
        print(f"Edad: {objeto.calculate_age()}")
        print(f"Activo: {objeto.activo}")

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

def menu_mostrar():
    conexion_bd = Conexion('base_datos/data_base.db') #Modificar las clases de persona para el id
    visualizador = MostrarDatos()
    
    datos_bd = visualizador.mostrar_todos_los_datos(conexion_bd)
    
    conexion_bd.cerrar_conexion()
    
    return datos_bd

def obtener_registro(indice):
    conexion_bd = Conexion('base_datos/data_base.db') #Modificar las clases de persona para el id
    tabla_personas = TablaPersona()
    
    persona = tabla_personas.obtener_datos(indice,Persona,conexion_bd)
    
    conexion_bd.cerrar_conexion()
    return persona


def menu_modificar(datos):
    """
    Función que se encarga de modificar un registro.
    
    Args:
        datos (dict): JSON que viene desde el frontend con los datos nuevos y el ID
    
    Returns:
        bool: True si la actualización fue exitosa, False si hubo error
"""
    # Conexión a la base de datos
    conexion_bd = Conexion('base_datos/data_base.db')
    tabla_personas = TablaPersona()
    # Procesamiento de nombre y apellidos
    partes_nombre = datos["nombre_completo"].split()
    
    # Crear objeto Persona con los datos actualizados
    persona = Persona(
        nombre=partes_nombre[0],
        apellidos=' '.join(partes_nombre[1:]),
        estado_especial=asignar_estado(datos['estado_especial']),
        manzana=datos['manzana'],
        estudia=datos['estudia'],
        fecha_nac=datos['fecha_nacimiento'],
        id_persona=datos['id']
    )
    
    # Modificar el dato en la base de datos
    resultado = tabla_personas.modificar_dato(persona, conexion_bd)
    
    conexion_bd.cerrar_conexion()
    
    return resultado

#fUNCION PARA PARCHAR LAS PERRADAS QUE SE HICIERON DESDE EL FRONT 
def asignar_estado(estado):
    if estado == "Ninguno" or estado == "1":
        numero = 1
    elif estado == "Madre soltera" or estado == "2":
        numero = 2
    elif estado == "Discapacitado" or estado == "3":
        numero = 3
    elif estado == "Enfermo" or estado == "4":
        numero = 4
    
    return numero

def menu_crear(lista_datos):
    print("Inicializando componentes...")
    conexion_bd = Conexion('base_datos/data_base.db') #Modificar las clases de persona para el id
    tabla_personas = TablaPersona()
    visualizador = MostrarDatos()
    #persona = Persona("juan", "Torres Morales", 2, "Centro", 0, "2002-02-19")

    persona = Persona(lista_datos["nombre"],lista_datos["apellidos"]
                    ,lista_datos['estado_especial'],lista_datos['manzana'],
                    lista_datos['estudia'],lista_datos['fecha_nac'])

    tabla_personas.agregar_dato(persona,conexion_bd)

    conexion_bd.cerrar_conexion()
    return True

if __name__ == "__main__":
    """Este es el menu de prueba donde se prueba el funcionamiento del crud de la clase
    Se crean las instancia de de la clase,

    el indice es un numero que se debera obtener de una busqueda previa, la logica para obtenerlo se debe manejar en otro fichero
    Con el indice se pueden obtener los datos de la persona para el funcionamiento del crud

    clase persona es la que sirve como estructura de almacenamiento de los datos
    tiene metodos como

    crear_persona
    is_valid (para verificar si es valido)
    calculate_age (no es posible utilizarla por el usuario)


    La clase tabla persona es la que tiene los metodos nesesarios
    para poder crear un curd los metodos de esta son:

    agregar_dato
    obtener_datos (sirve para los otros metodos del crud)
    obtener columnas (no se usa)
    agregar_muchos_datos (Agregar muchos datos al mismo tiempo)
    modicicar_dato (modifica un registro de la bd)
    eliminar dato

    La clase mostrar datos agrupa metodos para que los datos
    se puedan mostrar de manera correcta metodos:

    mostrar_registro_persona
    mostrar_todos_los_datos
    mostrar_datos (Muestra los datos que esten en una instancia de persona)


    Se tendra que cerrar siempre la conexion

    OrgAnizar el main para que el codigo funcione correctamente
    en modificar datos, los datos no se actulizan visulamente
    """
    # --------------------------
    # 1. INICIALIZACIÓN DE COMPONENTES
    # EL METODO MODIFICAR NO FUNCIONA
    # --------------------------
    print("Inicializando componentes...")
    conexion_bd = Conexion('base_datos/data_base.db') #Modificar las clases de persona para el id
    tabla_personas = TablaPersona()
    visualizador = MostrarDatos()
    persona = Persona("juan", "Torres Morales", 2, "Centro", 0, "2002-02-19")

    tabla_personas.agregar_dato(persona,conexion_bd)

    visualizador.mostrar_todos_los_datos(conexion_bd)

    conexion_bd.cerrar_conexion()
