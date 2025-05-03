# proyecto_agua
This is my first project with new tecnologies and git !!


# Before the create

You need create a virtual ent (env), for work with flask 

# Project structure 

/proyecto_agua
  │
  ├── /env                   # Entorno virtual (NO se sube a Git)
  │
  ├── /base_datos            # (Existente)
  │   └── bd_mandho.db       # Archivo SQLite (NO subir si tiene datos sensibles)
  │
  ├── /crud 
  |   |___/personas/ persona.py               # Lógica CRUD separada
  │   └── /pago_agua          
  │       ├── create.py
  │       ├── read.py
  │       ├── update.py
  │       └── delete.py
  │
  ├── /models                # Modelos de datos
  │   ├── persona.py         # Clase Persona
  │   └── pago_agua.py       # Clase PagoAgua
  │
  ├── /services              # Lógica de negocio
  │   └── persona_service.py 
  │
  │
  ├── /utils                 # Helpers
  │   ├── nucleo.py        # Conexión a BD
  │   └── config_manager.py  # Manejo de configuraciones
  │
  ├── /tests                 # Pruebas unitarias
  │   └── test_personas.py
  │
  ├── Frontend                #Todo el front hecho con astro y alpine para js
  ├── // .env.example           # Plantilla para variables (SÍ se sube) No sr ocupa
  ├── .gitignore             # Archivos a ignorar por Git
  ├── // config.py              # Configuración de la aplicación No se ocupa
  ├── // requirements.txt       # Dependencias No se ocupa
  └── app.py                 # Punto de entrada principal


## Generar una clave secreta SECRET_KEY

### Reglas de oro

Nunca la compartas: No la subas a GitHub o chats públicos.

Usa una por proyecto: No reutilices claves.

En producción:

Génerala con openssl o secrets.

Almacénala en variables de entorno del servidor (no en el código).


## Paginas para cuando se haga build

gpt
https://chatgpt.com/c/68118209-0aa8-8002-9755-edb8e7ce9f1b

flaks como construir - avazar siguiente apartado 
https://flask-es.readthedocs.io/quickstart/#sessions

instalacion 
https://werkzeug.palletsprojects.com/en/stable/installation/#install-werkzeug



## Funciones asincronas con python 

https://flask-es.readthedocs.io/async-await/
