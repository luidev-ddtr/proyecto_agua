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
  ├── /crud                  # Lógica CRUD separada
  │   └── /personas          
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
  ├── // .env                   # Variables de entorno LOCALES (NO subir a Git) No se ocupa
  ├── // .env.example           # Plantilla para variables (SÍ se sube) No sr ocupa
  ├── .gitignore             # Archivos a ignorar por Git
  ├── // config.py              # Configuración de la aplicación No se ocupa
  ├── // requirements.txt       # Dependencias No se ocupa
  └── app.py                 # Punto de entrada principal

