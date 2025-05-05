#Fichero el cual creara la instancia de flask # 
from flask import Flask
from flask_cors import CORS  # Importa CORS
#HARCODEAR LAS URL
import os

from routes.api_persona import api_persona_bp
from routes.api_pagos import api_pago_bp
#from routes.authentication import auth_bp

# Carga el .env con ruta ABSOLUTA (crítico en PythonAnywhere)
#load_dotenv('/home/Luidev/proyecto_agua/.env')


app = Flask(__name__)
#app.register_blueprint(auth_bp)  # Ahora las rutas estarán bajo /auth
app.register_blueprint(api_pago_bp) #rutas para el crud y la 
app.register_blueprint(api_persona_bp)

CORS(app, resources={
    r"/api/*": {
        "origins": [os.getenv('URL_FRONTEND')],
        "methods": ["GET", "POST", "PUT", "OPTIONS"],
        "allow_headers": ["Content-Type"],
        "supports_credentials": True  # ¡Nuevo!

    },
    r"/auth/*": {
        "origins": [os.getenv('URL_FRONTEND')],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Authorization", "Content-Type"],
        "supports_credentials": True  # ¡Nuevo!
    }
})

# Configuración de seguridad
app.config.update(
    SECRET_KEY=os.getenv('SECRET_KEY'),
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax'
)

# Debug: Verifica variables cargadas (aparecerá en los logs)
#print("=== Variables cargadas ===")
#print("BD:", os.getenv('DATABASE_PATH'))
#print("FRONTEND:", os.getenv('URL_FRONTEND'))

# Ruta de prueba
@app.route('/')
def home():
    return "API operativa", 200

# Manejo explícito de errores
@app.errorhandler(500)
def handle_500(error):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(error)
    }), 500


if __name__ == '__main__':
    app.run(debug=False)
