#archivo el cual servida conexion con la bd
import sqlite3
from datetime import datetime
from abc import ABC, abstractmethod

class Formtateo:
    def formatear_fecha(self,fecha_string):
        try:
            fecha = datetime.strptime(fecha_string, "%Y-%m-%d")
            return int(fecha.strftime("%Y%m%d"))  # Convertir a formato YYYYMMDD
        except ValueError:
            print("Formato de fecha incorrecto. Usa YYYY-MM-DD.")
            return None

class Persona:
    #LA CLASE PERSONA SE TENDRA QUE MODIFICAR DESPUES PARA QUE ACEPTE CORRECTAMENTE LOS DATOS
    def __init__(self, formateador, datos_prueba=True):
        """
        Constructor de la clase Persona.

        :param formateador: Instancia de la clase Formateo (o cualquier clase que implemente el método formatear_fecha).
        :param datos_prueba: Si es True, inicializa la instancia con datos de prueba.
        """
        self.formateador = formateador  # Guardar el formateador como atributoç
        
        if datos_prueba:
            # Inicializar con datos de prueba
            self.nombre = "Juan"
            self.apellidos = "Pérez González"
            self.estado_especial = "Ninguno"
            self.manzana = "A1"
            self.estudia = 1
            self.activo = 1
            self.fecha_nac = self.formateador.formatear_fecha("1990-05-15")
        else:
            # Inicializar con valores None (datos se ingresarán luego)
            self.nombre = None
            self.apellidos = None
            self.estado_especial = None
            self.manzana = None
            self.estudia = None
            self.fecha_nac = None
            self.activo = None

    def crear_persona(self):
        """
        Solicita los datos de la persona y los almacena en los atributos de la clase.
        """
        print("Ingresa tus datos:")
        self.nombre = input("Ingresa tu nombre: ")
        self.apellidos = input("Ingresa tus apellidos: ")
        self.estado_especial = input('Ingresa tu estado (si no tienes, escribe "ninguno"): ')
        self.manzana = input("Escribe tu manzana: ")
        self.estudia = self.solicitar_estudia()
        self.fecha_nac = self.solicitar_fecha_nacimiento()
        
        # Calcular la edad y determinar si está activo
        edad = self.calculate_age()
        self.activo = self.is_active(edad)

        print("\nDatos guardados correctamente.")

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
        :return: True si la persona está activa, False en caso contrario.
        :raises AttributeError: Si self.estado_especial no es una cadena.
        :raises TypeError: Si self.estudia no es un valor booleano o numérico.
        """
        try:
            #               Validaciones de datos antes de tratarlos
            if not isinstance(self.estado_especial, str):
                raise TypeError("El estado especial debe ser una cadena de texto.")

            
            if not isinstance(self.estudia, (int, bool)):
                raise TypeError("El valor de 'estudia' debe ser un número o un booleano.")

            
            estudia = bool(self.estudia) if isinstance(self.estudia, int) else self.estudia

            # Determinar si la persona está activa
            if (not (18 <= edad <= 65)) and self.estado_especial.lower() != "ninguno" and not estudia:
                return False
            return True
        except (AttributeError, TypeError) as e:
            print(f"Error al determinar si la persona está activa: {e}")
            raise  

    def mostrar_datos(self):
        """
        Muestra los datos de la persona.
        """
        print("\nDatos de la persona:")
        print(f"Nombre: {self.nombre} {self.apellidos}")
        print(f"Estado especial: {self.estado_especial}")
        print(f"Manzana: {self.manzana}")
        print(f"Estudia: {'Sí' if self.estudia else 'No'}")
        print(f"Fecha de nacimiento: {self.fecha_nac}")
        print(f"Edad: {self.calculate_age()}")
        print(f"Activo: {'Sí' if self.activo else 'No'}")

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
            raise  # Relanzar la excepción para que el caller pueda manejarla
        finally:
            # Asegurarse de que la conexión se cierre, incluso si hay un error
            self.cerrar_conexion()

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

class BaseDatos(ABC):
    @abstractmethod
    def agregar_dato(self, dato):
        """
        Agrega un nuevo registro a la base de datos.
        :param dato: El dato a agregar. Debe ser un objeto con los atributos necesarios.
        """
        pass

    @abstractmethod
    def modificar_dato(self, dato):
        """
        Modifica un registro existente en la base de datos.
        :param dato: El dato a modificar. Debe ser un objeto con los atributos necesarios.
        """
        pass

    @abstractmethod
    def eliminar_dato(self, dato):
        """
        Elimina un registro de la base de datos.
        :param dato: El dato a eliminar. Debe ser un objeto con los atributos necesarios.
        """
        pass
    def mostrar_datos(self):
        """
        Muestra todos los registros de la base de datos.
        """
        # Lógica para mostrar los datos
        pass

    def agregar_muchos_datos(self,lista):
        pass


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

            print("Datos insertados correctamente.")
        except sqlite3.Error as e:
            print(f"Error al insertar datos: {e}")
            raise  # Relanzar la excepción para que el caller pueda manejarla
        #No se cierra en metodos intermedios, solo hasta finalizar la consulta
        # finally:
        #     # Cerrar la conexión
        #     conexion_db.cerrar_conexion()

    def agregar_muchos_datos(self, lista_personas, conn):
        
        #ESTE METODO SE DEBE REVISAR EN EL FUTURO PARA INTEGRACIONES GRANDES DE DATOS
        """
        Agrega múltiples registros a la tabla 'persona' usando executemany.
        
        :param lista_personas: Lista de instancias de la clase Persona.
        :param conn: Instancia de la clase Conexion.
        :raises sqlite3.Error: Si ocurre un error durante la inserción.
        """
        try:
            conexion, cursor = conn.conexion()

            # Definir la consulta SQL
            query = """
            INSERT INTO persona (nombre, apellidos, estado_especial, manzana, estudia, activo)
            VALUES (?, ?, ?, ?, ?, ?)
            """

            # Preparar la lista de valores
            valores = [
                (
                    persona.nombre,
                    persona.apellidos,
                    persona.estado_especial,
                    persona.manzana,
                    persona.estudia,
                    persona.activo
                )
                for persona in lista_personas
            ]

            # Ejecutar la consulta con executemany
            cursor.executemany(query, valores)

            # Guardar los cambios
            conn.guardar_cambios()
            print(f"{len(lista_personas)} registros insertados correctamente.")
        except sqlite3.Error as e:
            print(f"Error al insertar datos: {e}")
            raise
        # finally:
        #     # Cerrar la conexión
        #     conn.cerrar_conexion()
    
    def modificar_dato(self,dato,conexion_db):
        pass
    
    def eliminar_dato(self,dato, conexion_db):
        pass
    
    def mostrar_datos(self, conexion_db):
        """
        Muestra los datos de la tabla 'persona' junto con el nombre del estado especial.

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
                nm_estado = fila[8]

                estudia_str = "Sí" if estudia else "No"
                activo_str = "Sí" if activo else "No"

                print(f"ID: {id}, Nombre: {nombre} {apellidos}, Manzana: {manzana}, Estado especial: {estado_especial}, Estudia: {estudia_str}, Activo: {activo_str}, Fecha de nacimiento: {fecha_nacimiento}")

        except sqlite3.Error as e:
            print(f"Error al mostrar datos: {e}")
            
class TablaPagoAgua(BaseDatos):
    def agregar_dato(self, dato):
        
        return super().agregar_dato(dato)
    

#Esta se deja en duda si se implementa 
class TablaEstadoEspecial:
    def __init__(self, conexion):
        """
        Inicializa la tabla de estados especiales.

        :param conexion: Instancia de la clase Conexion para manejar la conexión a la base de datos.
        """
        self.conexion = conexion

    def obtener_estados(self):
        """
        Obtiene todos los estados especiales de la base de datos.

        :return: Lista de estados especiales.
        :raises sqlite3.Error: Si ocurre un error durante la consulta.
        """
        try:
            conn, cursor = self.conexion.conexion()
            cursor.execute("SELECT nombre FROM estado_esp")
            estados = [fila[0] for fila in cursor.fetchall()]
            return estados
        except sqlite3.Error as e:
            print(f"Error al obtener estados especiales: {e}")
            raise
        finally:
            self.conexion.cerrar_conexion()

if __name__ == "__main__":
    
    personas_tabla = TablaPersona()
    formatear_en_persona = Formtateo()
    persona = Persona(formatear_en_persona,True)
    bd_conexion = Conexion('../repo/bd_mandho.db')
    
    personas_tabla.agregar_dato(persona,bd_conexion)

    
    personas_tabla.mostrar_datos(bd_conexion)
    
    bd_conexion.cerrar_conexion()

"""
Puntos faltantes /Ya
Crear la coneccion bien /ya
crear clase donde interactuaran o si sera en el main /Falta
corregir errores  /falta
agregar opcion para que se visualizen los datos  /falta
creo que ya 
"""