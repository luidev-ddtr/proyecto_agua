import os
from dotenv import load_dotenv
from utils.nucleo import Conexion
from models.pago_agua import Registro
from crud.pago_agua.create import Create
from crud.pago_agua.modificar import Modificate_register
from crud.pago_agua.show import MostrarDatos

#SE CARGAN LAS VARIABLES DE ENTORNO PARA SER USADAS
load_dotenv()  # Carga las variables del .env


def crear(datos): #Se trae un diccionario
    """Funcion la cual es encarga de manejar todas las intancias correctas para introducir datos de pago de agua
    a la bd, ademas de que introduce y recibe el resultado de hacer la consulta a la bd para crear datos"""
    conexion_db= Conexion(os.getenv('DATABASE_PATH'))
    crear_registro = Create()
    visualizador = MostrarDatos()
    registro = Registro(datos["id_persona"],datos["tomas"], datos["anio"], datos["fecha_pago"], datos["cantidad"])
    
    # Validacion para saber si no hay algun registro que se 
    # repite mas de una vez por año
    # VALIDACION LA CUAL IMPIDE QUE SE CREE MAS DE UN REGISTRO POR PERSONA AL AÑO
    # NO AGREGADA AUN POR CONSIDERACIONES 
    # lista_registros = visualizador.mostrar_todos_los_datos(conexion_db)
    # cont = 0
    # for dato in lista_registros:
    #     if dato['id_persona'] == registro.id_persona and dato['año'] == registro.año:
    #         cont += 1
    #     if cont >= 2:
    #         return False
        
    resultado = crear_registro.agregar_registro(registro,conexion_db)
    
    conexion_db.cerrar_conexion()
    
    if resultado:
        return True
    else:
        return False


def mostrar():
    """Funcion intermedia la cual se comunica con as clases de mostrar y trae los 
    datos al edpoint"""
    
    visualizador = MostrarDatos()
    conexion_db= Conexion(os.getenv('DATABASE_PATH'))
    
    datos = visualizador.mostrar_todos_los_datos(conexion_db)
    
    print("Bandera last \n")
    if datos:
        return datos
    else:
        return []
    
def modificar(datos):
    
    #Funcion aun no funciona bien 
    conexion_db= Conexion(os.getenv('DATABASE_PATH'))
    md_registro = Modificate_register()
    visuali = MostrarDatos()
    print("Banderas 1")
    
    
    registro = Registro(datos["id_persona"],datos["tomas"], 
                        datos["anio"], datos["fecha_pago"], 
                        datos["cantidad"], datos["estado_pago"], 
                        datos["tarifa_pendiente"], datos["id_registro"], True)
    
    print("Si hizo registro")
    resultado = md_registro.modificar_dato(registro,conexion_db) 
    
    print("mostrarando datos reados")
    visuali.mostrar_registro(datos["id_registro"],conexion_db)
    
    conexion_db.cerrar_conexion()
    if resultado:
        return True
    else:
        return False
