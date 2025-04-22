import sqlite3
from utils.nucleo import Conexion
from models.pago_agua import Registro
from crud.pago_agua.create import Create
from crud.pago_agua.modificar import Modificate_register
from crud.pago_agua.show import MostrarDatos


def crear(datos): #Se trae un diccionario
    """Funcion la cual es encarga de manejar todas las intancias correctas para introducir datos de pago de agua
    a la bd, ademas de que introduce y recibe el resultado de hacer la consulta a la bd para crear datos"""
    
    conexion_db= Conexion('base_datos/data_base.db')
    crear_registro = Create()
    visualizador = MostrarDatos()
   
    registro = Registro(datos["id_persona"],datos["tomas"], datos["anio"], datos["fecha_pago"], datos["cantidad"])
    
    #     # 3. Verificación completa de atributos
    # print("\n🔍 Atributos del registro creado:")
    # print(f"id_registro: {registro.id_registro} ({type(registro.id_registro)})")
    # print(f"id_persona: {registro.id_persona} ({type(registro.id_persona)})")
    # print(f"tomas_agua: {registro.tomas_agua} ({type(registro.tomas_agua)})")
    # print(f"año: {registro.año} ({type(registro.año)})")
    # print(f"fecha_pago: {registro.fecha_pago} ({type(registro.fecha_pago)})")
    # print(f"cantidad: {registro.cantidad} ({type(registro.cantidad)})")
    # print(f"estado_pago: {registro.estado_pago} ({type(registro.estado_pago)})")
    # print(f"tarifa_pendiente: {registro.tarifa_pendiente} ({type(registro.tarifa_pendiente)})")
    resultado = crear_registro.agregar_registro(registro,conexion_db)
    
    conexion_db.cerrar_conexion()
    
    if resultado:
        return True
    else:
        return False


def mostrar():
    """Funcion intermedia la cual se comunica con as clases de mostrar y trae los 
    datos al edpoint"""
    
    print("Bandera 0 \n")
    
    visualizador = MostrarDatos()
    conexion_db= Conexion('base_datos/data_base.db')
    
    datos = visualizador.mostrar_todos_los_datos(conexion_db)
    
    print("Bandera last \n")
    if datos:
        return datos
    else:
        return []
