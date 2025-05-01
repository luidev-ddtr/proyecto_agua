from flask import Blueprint, request, jsonify
import json
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Crear Blueprint para autenticación
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        # Obtener credenciales
        credencials_json = os.getenv('CREDENCIALS').strip("'")
        credencials = json.loads(credencials_json)
        
        # Obtener datos del request
        data = request.get_json()
        user_data = data.get('user')
        password_data = data.get('password')
        
        # Validar datos recibidos
        if not password_data or not user_data:
            return jsonify({'error': 'No se recibió contraseña o usuario'}), 400
        
        if user_data in credencials and credencials[user_data] == password_data:
            return jsonify({
                'status': 'success',
                'message': 'Credenciales válidas'
            }), 200
        else:
            return jsonify({
                'status': 'error',
                'message': 'Usuario o contraseña incorrectos'
            }), 403

    except Exception as e:
        print("Error en login:", str(e))
        return jsonify({
            'status': 'error',
            'message': 'Error interno del servidor',
            'details': str(e)
        }), 500

# Aquí puedes añadir más endpoints de autenticación:
# @auth_bp.route('/register', methods=['POST'])
# @auth_bp.route('/logout', methods=['POST'])