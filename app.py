#Fichero el cual creara la instancia de flask #     Creara el servidor
from flask import Flask, request, jsonify
from flask_cors import CORS  # Importa CORS

#Seccion para recibir datos del formulario crear personas 
from crud.personas.persona import menu_crear, menu_mostrar,menu_modificar
from crud.pago_agua.menu import crear,mostrar 

app = Flask(__name__)
# Permite solo tu dominio frontend (http://localhost:4321)
CORS(app, resources={
    r"/app/*": {  # Permite TODAS las rutas que empiecen con /app/
        "origins": "http://localhost:4321",
        "methods": ["GET", "POST", "PUT", "OPTIONS"],  # Todos los métodos necesarios
        "allow_headers": ["Content-Type"]
    }
})


@app.route('/app/create_us', methods=['POST'])
def registrar_persona():
    try:
        # Obtener los datos JSON enviados desde el frontend
        persona_json = request.get_json()
        
        # Verificar si se recibieron datos
        if not persona_json:
            return jsonify({'error': 'No se recibieron datos JSON'}), 400
        
        resultado = menu_crear(persona_json)
        
        if resultado:
            return jsonify({'Perfecto':"datos recibido correctamente"}), 200
    except Exception as e:
        # Manejar cualquier error inesperado
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/app/read_us', methods=['GET'])  # GET no debe llevar body
def mostrar_persona():
    """
    Endpoint para obtener datos de personas.
    No requiere JSON de entrada, solo devuelve datos.
    """
    try:
        datos = menu_mostrar()  # Tu función que obtiene datos de la BD
        return jsonify({'Perfecto': datos}), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500
"""Ejemplo de como se ve un registro que se envia al front 
{'id': 'CEN-JT-02-3465', 'nombre': 'juan', 'apellidos': 'Torres Morales',
'nombre_completo': 'juan Torres Morales', 'manzana': 'Centro', 'estado_especial':'Madre soltera',
'estudia': 'No', 'activo': 'Inactivo', 'fecha_nacimiento': '2002-02-19'}
"""


@app.route('/app/update_us', methods=['POST'])
def actualizar_registro():
    datos = request.get_json()
    
    if not datos:
        return jsonify({'error': 'No se recibieron datos JSON'}), 400
    
    print(f"nombre del los datos: {datos}")
    
    respuesta = menu_modificar(datos)
    
    if respuesta:
        return jsonify({'Perfecto':"datos actualizados correctamente"}), 200
    else:
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

@app.route("/app/buscar_us", methods=["GET"])
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


@app.route('/app/create_pay', methods=['POST'])
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
        # Manejar cualquier error inesperado
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500
        

@app.route('/app/read_pay', methods=['GET'])  # GET no debe llevar body
def mostrar_pagos():
    """
    Endpoint para obtener datos de pagos.
    No requiere JSON de entrada, solo devuelve datos.
    """
    try:
        datos = mostrar()  # Tu función que obtiene datos de la BD
        
        return jsonify({'Perfecto': datos}), 200
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


#Se debate si este metodo al final si se implementara 
@app.route("/app/buscar_pay", methods=["GET"])
def busqueda_pagos():
    search_term = request.args.get('q', '').lower().strip()
    
    if not search_term or len(search_term) < 3:
        return jsonify({'results': [], 'message': 'Ingrese mínimo 3 caracteres'}), 200
    try:
        
        todos_los_datos = mostrar()
        
        resultados = []
        
        for registro in todos_los_datos:
            campos_relevantes = [
                registro['nombre_completo'].lower(),
                registro.get('año', '').lower(),
                registro['monto'].lower()
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


if __name__ == '__main__':
    app.run(debug=True)
