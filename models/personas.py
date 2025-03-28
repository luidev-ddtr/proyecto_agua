#archivo el cual servida conexion con la bd
import sqlite3
from datetime import datetime
from clase_abstracta import BaseDatos
from utils.nucleo import Conexion, Formateo
class Persona:
    #LA CLASE PERSONA SE TENDRA QUE MODIFICAR DESPUES PARA QUE ACEPTE CORRECTAMENTE LOS DATOS
    def __init__(self, formateador):
        """
        Constructor de la clase Persona.

        :param formateador: Instancia de la clase Formateo (o cualquier clase que implemente el método formatear_fecha).
        :param datos_prueba: Si es True, inicializa la instancia con datos de prueba.
        """
        self.formateador = formateador  # Guardar el formateador como atributoç
        # Inicializar con valores None (datos se ingresarán luego)
        self.nombre = None
        self.apellidos = None
        self.estado_especial = None
        self.manzana = None
        self.estudia = None
        self.fecha_nac = None
        self.activo = None

    def crear_persona(self, nombre, apellidos, estado_especial, manzana, estudia, fecha_nac,id_persona=None):
        """
        Configura los datos de la persona en la instancia actual.
        
        Args:
            nombre (str): Nombre de la persona
            apellidos (str): Apellidos de la persona
            estado_especial (int/None): ID del estado especial
            manzana (str): Manzana/residencia
            estudia (bool/int): Si estudia (1/True o 0/False)
            fecha_nac (str): Fecha en formato YYYY-MM-DD
            id_persona (int/None): ID opcional para personas existentes
            
        Returns:
            self: Permite encadenamiento de métodos (opcional)
        """
                # Inicializar con valores None (datos se ingresarán luego)
        self.nombre = nombre
        self.apellidos = apellidos
        self.estado_especial = estado_especial
        self.manzana = manzana
        self.estudia = estudia
        self.fecha_nac = fecha_nac
        
        self.id_persona = id_persona
        
                # Calcular la edad y determinar si está activo
        edad = self.calculate_age()
        self.activo = self.is_active(edad)
        
        print("\nDatos cargados correctamente.")

    def solicitar_estudia(self):
        """
        Solicita si la persona estudia y convierte la respuesta a booleano.
        :return: True si estudia, False si no.
        """
        while True:
            respuesta = input("¿Estudias? (Si/No): ").strip().lower()
            if respuesta in ["si", "sí"]:
                return True
            elif respuesta in ["no"]:
                return False
            else:
                print("Respuesta inválida. Por favor, escribe 'Si' o 'No'.")

    def solicitar_fecha_nacimiento(self):
        """
        Solicita la fecha de nacimiento de la persona.
        :return: La fecha de nacimiento en formato 'YYYY-MM-DD'.
        """
        while True:
            fecha_nac = input("Escribe tu fecha de nacimiento en el formato AAAA-MM-DD: ")
            try:
                # Validar el formato de la fecha
                datetime.strptime(fecha_nac, '%Y-%m-%d')
                return fecha_nac
            except ValueError:
                print("Formato de fecha incorrecto. Intenta de nuevo.")

    def calculate_age(self):
        """
        Calcula la edad a partir de la fecha de nacimiento.
        :return: La edad en años.
        :raises ValueError: Si la fecha de nacimiento no tiene el formato correcto o es inválida.
        """
        try:
            # Verificar si self.fecha_nac es None o está vacío
            if not self.fecha_nac:
                raise ValueError("La fecha de nacimiento no puede estar vacía.")
            
            # Convertir la fecha de nacimiento a un objeto datetime
            fecha_nacimiento = datetime.strptime(self.fecha_nac, '%Y-%m-%d')
            
            # Calcular la edad
            hoy = datetime.today()
            edad = hoy.year - fecha_nacimiento.year
            if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
                edad -= 1
            
            return edad
        except ValueError as e:
            print(f"Error al calcular la edad: {e}")
            raise 
    
    def is_active(self, edad):
        """
        Determina si la persona está activa basándose en su edad, estado especial y si estudia.
        
        Args:
            edad (int): Edad de la persona
            
        Returns:
            int: 1 si la persona está activa, 0 en caso contrario
            
        Raises:
            TypeError: Si los tipos de datos no son los esperados
        """
        try:
            # Validaciones de datos antes de tratarlos
            if not isinstance(self.estado_especial, str):
                raise TypeError("El estado especial debe ser una cadena de texto.")
            
            # Convertir estudia a entero si no lo es (por si viene como booleano)
            estudia = int(self.estudia) if not isinstance(self.estudia, int) else self.estudia
            
            if estudia not in (0, 1):
                raise ValueError(f"El valor de 'estudia' debe ser 0 o 1. Valor actual: {self.estudia}")
            
            # Determinar si la persona está activa
            if (18 <= edad <= 65) and self.estado_especial.lower() == "ninguno" and (estudia == 0):
                return 1
            return 0
        except (AttributeError, TypeError, ValueError) as e:
            print(f"Error al determinar si la persona está activa: {e}")
            raise
class TablaPersona(BaseDatos):
    def agregar_dato(self, persona, conexion_db):
        """
        Agrega un nuevo registro a la tabla 'persona' en la base de datos.
                        ARGS:
        :persona: Instancia de la clase Persona con los datos a insertar.
        :conexion_db: Instancia de la clase Conexion para manejar la conexión a la base de datos.
        :raises sqlite3.Error: Si ocurre un error durante la inserción.
        """
        try:
            # Obtener la conexión y el cursor
            conexion, cursor = conexion_db.conexion()
            
            # Definir la consulta SQL correcta
            query = """
            INSERT INTO persona (nombre, apellidos, estado_especial, manzana, estudia, activo, fecha_nacimiento)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """

            # Obtener los valores desde el objeto `persona`
            valores = (
                persona.nombre,
                persona.apellidos,
                persona.estado_especial,
                persona.manzana,
                persona.estudia,
                persona.activo,
                persona.fecha_nac
            )

            # Ejecutar la consulta SQL
            cursor.execute(query, valores)
            
            conexion_db.guardar_cambios()

            print("Datos insertados correctamente.")
        except sqlite3.Error as e:
            print(f"Error al insertar datos: {e}")
            raise  # Relanzar la excepción para que el caller pueda manejarla
        #No se cierra en metodos intermedios, solo hasta finalizar la consulta
        # finally:
        #     # Cerrar la conexión
        #     conexion_db.cerrar_conexion()
        
    def obtener_datos(self, indice,persona, conexion_db):
        """
        Obtiene los datos de una persona desde la base de datos y crea un objeto Persona.
        Args:
        indic e (int): ID de la persona a buscar
        conexion_db: Objeto que gestiona la conexión a la base de datos
        
        Returns:
            Persona: Objeto Persona con los datos cargados o None si no se encuentra
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
            #Se puede mejorar solo que es menos legible y mas eficiente 
            
            persona.crear_persona(
                nombre=datos[0],
                apellidos=datos[1],
                estado_especial=datos[2],
                manzana=datos[3],
                estudia=datos[4],
                fecha_nac=datos[5],
                id_persona = indice
            )
            return persona
            
        except sqlite3.Error as e:
            print(f"Error al obtener datos: {e}")
            raise
        
    def obtener_columnas(self):
        """
        Obtiene los datos de la columna persona desde la base de datos y crea un objeto con estos elementos.
        Args:
        Returns:
            columnas_db: Objeto columnas con los datos cargados o None si no se encuentra
            """
        
        columnas_db = list("id","nombre","apellidos","estado_especial","manzana","estudia","activo","fecha_nacimiento","persona")
        return columnas_db
        
#Este metodo no funciona aun
    def agregar_muchos_datos(self, lista_personas_json, clase_persona, conn):
        """
        Agrega múltiples registros a la tabla 'persona' recibiendo datos en formato JSON/diccionario.
        
        :param lista_personas_json: Lista de diccionarios con los datos de las personas.
                Formato esperado:
                {
                    'nombre': str,
                    'apellidos': str,
                    'estado_especial': int o None,
                    'manzana': str,
                    'estudia': int (0/1),
                    'fecha_nac': str (formato yyyy-mm-dd)
                }
        :param clase_persona: Instancia de la clase Persona que contiene la lógica de formateo.
        :param conn: Instancia de la clase Conexion.
        :raises sqlite3.Error: Si ocurre un error durante la inserción.
        """
        try:
            conexion, cursor = conn.conexion()

            # Definir la consulta SQL
            query = """
            INSERT INTO persona (
                nombre, 
                apellidos, 
                estado_especial, 
                manzana, 
                estudia, 
                activo,
                fecha_nacimiento
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """

            valores = []
            for persona_data in lista_personas_json:
                # Configurar los datos usando el método de la clase Persona
                clase_persona.crear_persona(
                    nombre=persona_data['nombre'],
                    apellidos=persona_data['apellidos'],
                    estado_especial=persona_data["estado_especial"],
                    manzana=persona_data['manzana'],
                    estudia=persona_data['estudia'],
                    fecha_nac=persona_data['fecha_nac']
                )
                
                # Preparar tupla de valores para la inserción
                valores.append((
                    clase_persona.nombre,
                    clase_persona.apellidos,
                    clase_persona.estado_especial,
                    clase_persona.manzana,
                    int(clase_persona.estudia),  # Aseguramos que sea 0 o 1
                    int(clase_persona.activo),   # Aseguramos que sea 0 o 1
                    clase_persona.fecha_nac  # Ya formateada por crear_persona
                ))

            # Ejecutar la consulta con executemany
            cursor.executemany(query, valores)

            # Guardar los cambios
            conn.guardar_cambios()
            print(f"{len(lista_personas_json)} registros insertados correctamente.")
            return True
        except sqlite3.Error as e:
            print(f"Error al insertar datos en la base de datos: {e}")
            raise
        except KeyError as e:
            print(f"Falta campo obligatorio en los datos: {e}")
            raise ValueError(f"El campo {e} es requerido")
        except Exception as e:
            print(f"Error inesperado al procesar los datos: {e}")
            raise
            
    def modificar_dato(self, dato, conexion_db):
        """Modifica los datos de una persona con validación de entradas.
        
        params
        :param dato Instancia de persona la cual tiene la informacion
        :param conexion_db Instancia de la clase Conexion.
        """
        conexion, cursor = conexion_db.conexion()
        
        campos = {
            1: ('nombre', str),
            2: ('apellidos', str),
            3: ('estado_especial', str),
            4: ('manzana', str),
            5: ('estudia', int),
            6: ('fecha_nacimiento', 'date')
        }
        
        while True:
            # Manejo seguro de la fecha para mostrar
            fecha_mostrar = (
                datetime.strptime(dato.fecha_nac, '%Y-%m-%d').strftime('%Y-%m-%d') 
                if dato.fecha_nac and isinstance(dato.fecha_nac, str) 
                else 'No especificada'
            )
            
            print(f"""\nMENU DE MODIFICAR PERSONA
            Datos actuales:
            ----------------------
            1) Nombre: {dato.nombre}
            2) Apellidos: {dato.apellidos}
            3) Estado Especial: {dato.estado_especial}
            4) Manzana: {dato.manzana}
            5) Estudia: {'Sí' if dato.estudia == 1 else 'No'}
            6) Fecha Nacimiento: {fecha_mostrar}
            7) Activo: {'Activo' if dato.activo == 1 else 'Inactivo'}  (No modificable diractamente)
            ----------------------
            Opciones:
            1-6. Modificar campo correspondiente
            7. Guardar y salir
            """)

            opcion = input("Seleccione una opción (1-7): ").strip()
            
            if opcion == '7':
                break
                
            if not opcion.isdigit() or int(opcion) not in campos:
                print("¡Opción no válida! Debe ser un número entre 1 y 7")
                continue
                
            opcion = int(opcion)
            campo, tipo = campos[opcion]
            
            if tipo == int:  # Campo estudia (Sí/No)
                while True:
                    valor = input("¿Estudia actualmente? (Sí/No): ").strip().lower()
                    if valor in ('sí', 'si', 's', '1'):
                        nuevo_valor = 1
                        break
                    elif valor in ('no', 'n', '0'):
                        nuevo_valor = 0
                        break
                    else:
                        print("Por favor ingrese sólo 'Sí' o 'No'")
                        
            elif tipo == 'date':  # Fecha de nacimiento
                while True:
                    valor = input("Ingrese fecha (YYYY-MM-DD): ").strip()
                    try:
                        # Validamos pero guardamos como string
                        datetime.strptime(valor, '%Y-%m-%d')
                        nuevo_valor = valor  # Guardamos como string
                        break
                    except ValueError:
                        print("Formato incorrecto. Use AAAA-MM-DD (ej. 2000-05-15)")
                        
            else:  # Campos de texto
                valor = input(f"Ingrese nuevo valor para {campo}: ").strip()
                if not valor:
                    print("El campo no puede estar vacío")
                    continue
                nuevo_valor = str(valor) if tipo == str else valor
                
            # Actualizar objeto y base de datos
            setattr(dato, campo, nuevo_valor)
            cursor.execute(f"UPDATE persona SET {campo} = ? WHERE id = ?", 
                        (nuevo_valor, dato.id_persona))
            conexion_db.guardar_cambios()
            print("✓ Cambio guardado correctamente")
    

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
class MostrarDatos:
    """Estra clase es especifica para la tabla y objeto persona por lo que se tiene que hacer mas general
    Se busca que  cada clase que la utilize tenga un objeto para que pueda mostrarse el nombre correctamente, 
    Se debe verificar si es nesesario buscar el nombre o solo las columnas
    
    Se tienen que obtener las columas y tambien para mostrarlas dinamicamente
    """
    def mostrar_registro_persona(self, indice, conexion_db):
        """
        Muestra un registro de la tabla persona buscándolo por índice.
        
        Args:
            indice (int): ID del registro en la base de datos
            columas_bd: Instancia de la clase esta guarda los nombres de la base de datos
            conexion_db (object): Instancia de la clase Conexion para manejar la conexión
        Raises:
            DatabaseError: Si ocurre un error al interactuar con la base de datos
            
            Se busca que esta clase sea dinamica es decir que diferentes clases sean capaz de utilizarla y mostrar ahi los datos
        """
        if conexion_db is None:
            raise ValueError("Se requiere una conexión a la base de datos")
        
        conexion, cursor = conexion_db.conexion()
        
        query = """
        SELECT 
            p.id, 
            p.nombre, 
            p.apellidos, 
            p.estado_especial, 
            p.manzana, 
            p.estudia, 
            p.activo, 
            p.fecha_nacimiento, 
            e.nombre AS nombre_estado
        FROM persona p
        LEFT JOIN estados_especiales e ON p.estado_especial = e.id
        WHERE p.id = ?
        """
        cursor.execute(query, (indice,))
        registro = cursor.fetchone()
        
        if registro is None:
            print(f"\n⚠️ No se encontró persona con ID {indice}\n")
            return
        
        # Manejo seguro de la fecha
        fecha_nac = registro[7]
        if fecha_nac and isinstance(fecha_nac, str):
            try:
                # Si es string, convertir a datetime y luego formatear
                fecha_formateada = datetime.strptime(fecha_nac, '%Y-%m-%d').strftime("%d/%m/%Y")
            except ValueError:
                fecha_formateada = "Formato inválido"
        elif fecha_nac and hasattr(fecha_nac, 'strftime'):
            # Si ya es objeto fecha (datetime/date)
            fecha_formateada = fecha_nac.strftime("%d/%m/%Y")
        else:
            fecha_formateada = "No especificada"

        # Construir diccionario con los datos CORREGIDO (comparar con 1)
        datos = {
            'id': registro[0],
            'nombre_completo': f"{registro[1]} {registro[2]}",
            'manzana': registro[4],
            'estado_especial': registro[8] or 'Ninguno',
            'estudia': "Sí" if registro[5] == 1 else "No",  # Comparación explícita con 1
            'activo': "Activo" if registro[6] == 1 else "Inactivo",  # Comparación explícita con 1
            'fecha_nacimiento': fecha_formateada
        }
        
        # Mostrar los datos
        plantilla = """
        📋 Datos de la persona:
        ----------------------------
        🔹 ID: {id}
        🔹 Nombre completo: {nombre_completo}
        🔹 Manzana: {manzana}
        🔹 Estado especial: {estado_especial}
        🔹 Estudia: {estudia}
        🔹 Estado: {activo}
        🔹 Fecha de nacimiento: {fecha_nacimiento}
        ----------------------------
        """
        print(plantilla.format(**datos))
    
    def mostrar_todos_los_datos(self, conexion_db):
        """
        Muestra los datos de la tabla 'que llame al metodo' junto con el nombre del estado especial.

        :param conexion_db: Instancia de la clase Conexion para manejar la conexión a la base de datos.
        """
        try:
            conexion, cursor = conexion_db.conexion()

            print("Mostrando datos de la tabla personas")

            query = """
            SELECT p.id, p.nombre, p.apellidos, p.estado_especial, p.manzana, p.estudia, p.activo, p.fecha_nacimiento, e.nombre AS nm_estado
            FROM persona p
            LEFT JOIN estados_especiales e ON p.estado_especial = e.id
            """

            cursor.execute(query)
            tabla = cursor.fetchall()

            for fila in tabla:
                id = fila[0]
                nombre = fila[1]
                apellidos = fila[2]
                estado_especial = fila[3]
                manzana = fila[4]
                estudia = fila[5]
                activo = fila[6]
                fecha_nacimiento = fila[7]

                estudia_str = "Sí" if estudia == 1 else "No"
                activo_str = "Sí" if activo == 1 else "No"

                print(f"ID: {id}, Nombre: {nombre} {apellidos}, Manzana: {manzana}, Estado especial: {estado_especial}, Estudia: {estudia_str}, Activo: {activo_str}, Fecha de nacimiento: {fecha_nacimiento}")

        except sqlite3.Error as e:
            print(f"Error al mostrar datos: {e}")
    
    def mostrar_datos(self, objeto):
        """
        Muestra los datos de la persona.
        
        :param objeto es el objeto persona que se quiere mostrar, sirve mas de testeo 
        """
        print("\nDatos de la persona:")
        print(f"Nombre: {objeto.nombre} {objeto.apellidos}")
        print(f"Estado especial: {objeto.estado_especial}")
        print(f"Manzana: {objeto.manzana}")
        print(f"Estudia: {'Sí' if objeto.estudia else 'No'}")
        print(f"Fecha de nacimiento: {objeto.fecha_nac}")
        print(f"Edad: {objeto.calculate_age()}")
        print(f"Activo: {'Sí' if objeto.activo == 1 else 'No'}")
        
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
    # --------------------------
    print("Inicializando componentes...")
    formateador = Formateo()
    bd_conexion = Conexion('base_datos/bd_mandho.db')
    tabla_personas = TablaPersona()
    visualizador = MostrarDatos()
    persona = Persona(bd_conexion)
    #Siempre se cierra la conexion 
    bd_conexion.cerrar_conexion()
