#Fichero el cual creara la instancia de flask # 
from flask import Flask
from flask_cors import CORS  # Importa CORS
#HARCODEAR LAS URL
import os

#from routes.authentication import auth_bp
from routes.api_persona import api_persona_bp
from routes.api_pagos import api_pago_bp

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

if __name__ == '__main__':
    app.run(debug=False)
