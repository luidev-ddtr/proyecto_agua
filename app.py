"""
Módulo de Inicialización de la Aplicación Flask

Este módulo crea y configura la instancia principal de la aplicación Flask, registra los blueprints
para diferentes grupos de rutas y configura las políticas CORS.

Configuración:
- Carga variables de entorno desde el archivo .env (crítico para despliegue en PythonAnywhere)
- Configura políticas CORS con reglas específicas para rutas API y de autenticación

Blueprints Registrados:
- auth_bp: Rutas de autenticación (login, logout, gestión de sesión)
- api_pago_bp: Rutas API de pagos (operaciones CRUD para pagos)
- api_persona_bp: Rutas API de personas (operaciones CRUD para datos de personas)

Configuración CORS:
- Rutas API (/api/*):
  - Orígenes permitidos: URL_FRONTEND del .env
  - Métodos: GET, POST, PUT, OPTIONS
  - Cabeceras: Content-Type
  - Credenciales: Soporte habilitado
- Rutas de autenticación (/auth/*):
  - Orígenes permitidos: URL_FRONTEND del .env
  - Métodos: GET, POST, OPTIONS
  - Cabeceras: Authorization, Content-Type
  - Credenciales: Soporte habilitado

Variables de Entorno Requeridas:
- URL_FRONTEND: URL de la aplicación frontend para políticas CORS

Uso:
    python app.py  # Ejecuta el servidor de desarrollo en modo debug

Nota: En entornos de producción, debe ejecutarse a través de un servidor WSGI como Gunicorn.
"""
#Fichero el cual creara la instancia de flask # 
from flask import Flask
from flask_cors import CORS  # Importa CORS
from dotenv import load_dotenv
#HARCODEAR LAS URL
import os

from routes.authentication import auth_bp
from routes.api_persona import api_persona_bp
from routes.api_pagos import api_pago_bp

# Carga el .env con ruta ABSOLUTA (crítico en PythonAnywhere)
load_dotenv('.env')

app = Flask(__name__)
app.register_blueprint(auth_bp)  # Ahora las rutas estarán bajo /auth
app.register_blueprint(api_pago_bp) #rutas para el crud y la 
app.register_blueprint(api_persona_bp)

#panel_de_control(True)

CORS(app, resources={
    r"/api/*": {
        "origins": os.getenv('URL_FRONTEND').strip('"'),
        "methods": ["GET", "POST", "PUT", "OPTIONS"],
        "allow_headers": ["Content-Type"],
        "supports_credentials": True  # ¡Nuevo!

    },
    r"/auth/*": {
        "origins":os.getenv('URL_FRONTEND').strip('"'),
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Authorization", "Content-Type"],
        "supports_credentials": True  # ¡Nuevo!
    }
})


if __name__ == '__main__':
    app.run(debug=True)
