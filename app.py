#Fichero el cual creara la instancia de flask #     Creara el servidor
from flask import Flask, request, jsonify
from flask_cors import CORS  # Importa CORS

app = Flask(__name__)
# Permite solo tu dominio frontend (http://localhost:4321)
CORS(app, resources={
    r"/app": {"origins": "http://localhost:4321"} })

#Seccion para recibir datos del formulario crear personas 
from crud.personas.persona import menu
@app.route('/app/create_us', methods=['POST'])
def registrar_persona():
    try:
        # Obtener los datos JSON enviados desde el frontend
        persona_json = request.get_json()
        
        # Verificar si se recibieron datos
        if not persona_json:
            return jsonify({'error': 'No se recibieron datos JSON'}), 400
        
        resultado = menu(persona_json)
        
        if resultado:
            return jsonify({'Perfecto': 'Comunicacion efectiva de datos JSON'}), 200
    except Exception as e:
        # Manejar cualquier error inesperado
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500




if __name__ == '__main__':
    app.run(debug=True)
