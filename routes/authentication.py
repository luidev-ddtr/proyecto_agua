from flask import Blueprint, request, jsonify
import json
import os
from dotenv import load_dotenv
from routes.security import write_token, valide_token
# Cargar variables de entorno
load_dotenv()

# Crear Blueprint para autenticación
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

#CamBios para produccion camviar las rutas de local a el servidor externo 
# 🔥🔥🔥 Añade este decorador JUSTO AQUÍ (después de crear el blueprint) 🔥🔥🔥
@auth_bp.after_request
def after_auth_request(response):
    """Añade headers CORS necesarios para todas las respuestas de /auth"""
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Origin', os.getenv('URL_FRONTEND')) #AQUI  
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    return response

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        # 1. Verifica credenciales .env
        credencials_json = os.getenv('CREDENCIALS')
        if not credencials_json:
            raise ValueError("CREDENCIALS no está definido en .env")
            
        credencials = json.loads(credencials_json.strip("'"))
        
        # 2. Verifica JSON recibido
        data = request.get_json()
        if not data:
            raise ValueError("No se recibió JSON")
            
        user_data = data.get('user')
        password_data = data.get('password')
        
        if not all([user_data, password_data]):
            return jsonify({'error': 'Usuario y contraseña requeridos'}), 400
        
        # 3. Validación
        if user_data in credencials and credencials[user_data] == password_data:
            token = write_token(data={'user': user_data})  # Asegúrate que write_token recibe dict
            
            response = jsonify({'status': 'success'})
            response.set_cookie(
                'auth_token',
                token,
                httponly=True,
                secure=False,
                samesite='Lax',
                max_age=7200
            )
            return response
            
        return jsonify({'error': 'Usuario o contraseña incorrectos'}), 401
#Configuracion de las cookies para produccion 
            # response.set_cookie(
            #     'auth_token',
            #         token,
            #         httponly=True,
            #         secure=True,                  # Solo HTTPS (obligatorio en producción)
            #         samesite='None',              # Permite cookies cross-origin
            #         max_age=7200,
            #         domain='.github.io'           # Dominio padre para GitHub Pages
            # )

# Para produccion 
#             response.set_cookie(
#                 'auth_token',
#                 token,
#                 httponly=True,
#                 secure=False,
#                 samesite='Lax',
#                 max_age=7200
#             )


    except json.JSONDecodeError as e:
        print(f"ERROR - Fallo al parsear CREDENCIALS: {str(e)}")
        return jsonify({'error': 'Configuración inválida (CREDENCIALS mal formateado)'}), 500
    except Exception as e:
        print(f"ERROR - Detalles: {str(e)}")
        return jsonify({'error': 'Error interno', 'details': str(e)}), 500



@auth_bp.route('/validate-token')
def validate_token():
    token = request.cookies.get('auth_token')
    if not token:
        return jsonify({'valid': False, 'error': 'No hay token'}), 401
    try:
        valide_token(token)  # Usa tu función existente
        return jsonify({'valid': True}), 200
    except Exception as e:
        return jsonify({'valid': False, 'error': str(e)}), 401


@auth_bp.route('/logout', methods=["POST"])
def cerrar_sesion(): 
    """
    Funcion para cerrar la sesion del usuario
    """
    response = jsonify({"estatus": "succes", "message": "Sesion cerrada correctamente"})
    
        # 2. Eliminar cookie (obligatorio)
    response.delete_cookie(
        'auth_token',
        path='/',  # Asegura que se elimine en todas las rutas
        domain= os.getenv('DOMAIN') #AQIII
    )
    return response
