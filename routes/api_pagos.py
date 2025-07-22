from flask import Blueprint, request, jsonify

from crud.personas.persona import menu_mostrar
from crud.pago_agua.menu import crear,mostrar, modificar

#Seguridad
#from routes.security import token_required


# Crear Blueprint para autenticación
api_pago_bp = Blueprint('api_pagos', __name__, url_prefix='/api')


@api_pago_bp.route("/buscar_us", methods=["GET"])

def busqueda_tiempo_real():
    search_term = request.args.get('q', '').lower().strip()
    if not search_term or len(search_term) < 3:
        return jsonify({'results': [], 'message': 'Ingrese mínimo 3 caracteres'}), 200
    try:
        
        todos_los_datos = menu_mostrar()
        
        resultados = []
        
        for registro in todos_los_datos:
            campos_relevantes = [
                registro['nombre_completo'].lower(),
                registro['id'].lower(),
                registro.get('manzana', '').lower()
            ]
            
            
            
            if any(search_term in campo for campo in campos_relevantes):
                es_activo = registro.get('activo', '').lower() == 'activo'
                
                resultados.append({
                    'id': registro['id'],
                    'text': f"{registro['nombre_completo']} ({registro['id']})" + 
                        (" ⚠ Inactivo" if not es_activo else ""),
                    'data': registro,
                    'selectable': es_activo,
                    'reason': '' if es_activo else 'Usuario inactivo'
                })
        return jsonify({
            'status': 'success',
            'count': len(resultados),
            'results': resultados
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f"Error en búsqueda: {str(e)}"
        }), 500
print("banpago1")

@api_pago_bp.route('/create_pay', methods=['POST'])

def registrar_pago():
    try:
        # Obtener los datos JSON enviados desde el frontend
        pago_json = request.get_json()
        
        #validacion visula de los datos 
        print(f"datos recibidos: {pago_json}")
        
        # Verificar si se recibieron datos
        if not pago_json:
            return jsonify({'error': 'No se recibieron datos JSON'}), 400
        
        resultado = crear(pago_json)
        
        if resultado:
            return jsonify({'Perfecto':"datos recibido correctamente"}), 200
        
    except Exception as e:
        print(e)
        # Manejar cualquier error inesperado
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500
        

@api_pago_bp.route('/read_pay', methods=['GET'])  # GET no debe llevar body

def mostrar_pagos():
    """
    Endpoint para obtener datos de pagos.
    No requiere JSON de entrada, solo devuelve datos.
    """
    try:
        datos = mostrar()  # Tu función que obtiene datos de la BD
        
        return jsonify({'Perfecto': datos}), 200
    
    except Exception as e:
        print(e)
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


#Se debate si este metodo al final si se implementara 
@api_pago_bp.route("/update_pay", methods=["POST"])

def actualizar_registro_pago():
    try:
        datos = request.get_json()
        
        if not datos:
            return jsonify({'error': 'No se recibieron datos JSON'}), 400
        
        print(f"nombre del los datos: {datos}")
        
        respuesta = modificar(datos)
        
        if respuesta:
            return jsonify({'Perfecto':"datos actualizados correctamente"}), 200
        
    except Exception as e:
                return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500