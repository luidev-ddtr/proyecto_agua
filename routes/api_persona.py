from flask import Blueprint, request, jsonify

#Seccion para recibir datos del formulario crear personas 
from crud.personas.persona import menu_crear, menu_mostrar,menu_modificar
from utils.nucleo import Conexion


from crud.personas.panel_control import PanelControl

#Seguridad
#from routes.security import token_required 


# Crear Blueprint para autenticación
api_persona_bp = Blueprint('api_personas', __name__, url_prefix='/api')
@api_persona_bp.route('/create_us', methods=['POST'])
def registrar_persona():
    try:
        print("band1")
        # Obtener los datos JSON enviados desde el frontend
        persona_json = request.get_json()
    
        # Verificar si se recibieron datos
        print("band2")
        if not persona_json:
            return jsonify({'error': 'No se recibieron datos JSON'}), 400
        print("band5")
        
        resultado = menu_crear(persona_json)
        print("band6")
        
        if resultado:
            return jsonify({'Perfecto':"datos recibido correctamente"}), 200
    except Exception as e:
        # Manejar cualquier error inesperado
        print(e)
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@api_persona_bp.route('/read_us', methods=['GET'])  # GET no debe llevar body
def mostrar_persona():
    """
    Endpoint para obtener datos de personas.
    No requiere JSON de entrada, solo devuelve datos.
    """
    try:
        datos = menu_mostrar()  # Tu función que obtiene datos de la BD
        return jsonify({'Perfecto': datos}), 200
    except Exception as e:
        print(e)
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500
"""Ejemplo de como se ve un registro que se envia al front 
{'id': 'CEN-JT-02-3465', 'nombre': 'juan', 'apellidos': 'Torres Morales',
'nombre_completo': 'juan Torres Morales', 'manzana': 'Centro', 'estado_especial':'Madre soltera',
'estudia': 'No', 'activo': 'Inactivo', 'fecha_nacimiento': '2002-02-19'}
"""


@api_persona_bp.route('/update_us', methods=['POST'])
def actualizar_registro():
    datos = request.get_json()
    
    if not datos:
        return jsonify({'error': 'No se recibieron datos JSON'}), 400
    
    print(f"nombre del los datos: {datos}")
    
    respuesta = menu_modificar(datos)
    
    if respuesta:
        return jsonify({'Perfecto':"datos actualizados correctamente"}), 200
    else:
        print(str(Exception))
        return jsonify({
            'status': 'error',
            'message': str(Exception)
        }), 500
"""
ESTOS SON LOS DATOS RECIBIDOS DESDE EL FRONT 
lo demas paree estar bien 
ERRORES estado_especial DEBE SER UN NUMERO AL IGUAL QUE estudia
{'id': 'CEN-JT-02-3465', 'nombre_completo': 'juan Joel', 'estado_especial': 'Madre soltera',
'manzana': 'Centro', 'estudia': 'No', 'fecha_nacimiento': '2002-02-19'}
"""

panel = PanelControl(Conexion)
@api_persona_bp.route('/dashboard')
def panel_de_control(debugg):
    if debugg:
        #Cuando solo se van a mostrar datos de los usuarios 
        try:
            registros_totales =panel.cantidad_registros()
            registros_validos, tamaño = panel.registros_validos()
            #edad_prom = panel.promedio_edad()
            
            print( (
                {'datosTotales': registros_totales,
                    "registrosValidos": tamaño,
                    "datos": registros_validos,
                    #"edadPromedio": edad_prom
                    }
                        ), 200)
            
        except Exception as e:
            print( ({
                'status': 'error',
                'message': str(e)
            }), 500)