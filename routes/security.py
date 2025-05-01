from flask import request, jsonify
import os
from datetime import datetime, timedelta
from jwt import encode, decode, exceptions
from functools import wraps


#FUNCIONES PARA LA CREACION Y MONITORIZACION DEL JWT

#Configurar para que sean horas
def expire_date(hours:int):
    """
    Funcion que recibe parametros en y calcula el tiempo para que expire el token en este 
    """
    now = datetime.now()
    new_date = now + timedelta(hours)
    return new_date

def write_token(data: dict):
    token = encode(
        payload={**data, "exp": expire_date(2)}, 
        key=os.getenv("SECRET_KEY"),
        algorithm="HS256"
    )
    return token  # <- Quita el .encode("UTF-8")

def valide_token(token, output=False):
    try:
        decoded = decode(
            token, 
            key=os.getenv("SECRET_KEY"), 
            algorithms=["HS256"]
        )
        return decoded if output else True
    except exceptions.DecodeError:
        raise Exception("Token inválido")
    except exceptions.ExpiredSignatureError:
        raise Exception("Token expirado")


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        # 1. Buscar token en cookies (HTTP-only)
        token = request.cookies.get('auth_token')
        
        # 2. Opcional: Permitir también por headers (para APIs)
        if not token and 'Authorization' in request.headers:
            token = request.headers['Authorization'].split()[1]  # Bearer <token>
        
        if not token:
            return jsonify({'error': 'Token no proporcionado'}), 401
            
        try:
            # Validar token usando tu función existente
            decoded = valide_token(token, output=True)
            current_user = decoded['user']  # Asume que el token incluye 'user'
        except Exception as e:
            return jsonify({'error': 'Token inválido', 'details': str(e)}), 401
            
        return f(current_user, *args, **kwargs)
    return decorated