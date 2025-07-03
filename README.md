# proyecto_agua
This is my first project with new tecnologies and git !!

# Lee la documentacion para instalar el proyecto

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
  ├── Frontend               #Todo el front hecho con astro y alpine para js
  ├── .env                   # Plantilla para variables (SÍ se sube) No sr ocupa
  ├── .gitignore             # Archivos a ignorar por Git
  ├── requirements.txt       # Dependencias No se ocupa
  └── app.py                 # Punto de entrada principal


## Generar una clave secreta SECRET_KEY

### Reglas de oro

Nunca la compartas: No la subas a GitHub o chats públicos.
Usa una por proyecto: No reutilices claves.
En producción:
Génerala con openssl o secrets.
Almacénala en variables de entorno del servidor (no en el código).


# Descripcion

Este el el proyecto de Gestion comunal SG mandho el cual consta de 2 bases principales, backend y frontend
Tenemos por una parte python y flask para backend y astro, con alpine.js para frontend

El lenguaje estructurado a objetos es python, y la base de datos por el momento es SQLite

La estructuras de carpetas del backend se muestra aqui, sin embargo las estructura del front se muestra en su propio README.md (En la carpeta frontend).


## Documentacion backend
Aunque ya tenemos la estructura de carpetas tenemos los docstring los cuales docuemntan cada una de las funciones ejemplo

```python
    def funcion_de_prueba(self, parametro1, parametro2):
        """Descripción breve de lo que hace la función.

        Descripción más detallada de la función. Puede explicar el propósito,
        el algoritmo utilizado, o cualquier información relevante.

        Args:
            parametro1 (tipo): Descripción de qué es parametro1 y qué representa.
            parametro2 (tipo): Descripción de qué es parametro2 y qué representa.

        Returns:
            tipo: Descripción de lo que retorna la función. Si no retorna nada, se puede omitir
            o poner "None".

        Raises:
            TipoError: Descripción de bajo qué condiciones se lanza este error.

        Examples:
            >>> funcion_de_prueba(valor1, valor2)
            resultado_esperado
        """
        pass
```
y despues cuando mandas a llamar a esta funcion, se ve el docstring de esta forma:

![imagen inicio](documentacion_img/docstring.png)

Ademas cada fichero tendra una descripcion de que es lo que se hace en cada uno 

```python
class Hola Mundo
  """
  En esta clase se conecta con la base de datos mediante este metodo, utiliza estas propiedades,
  tiene estos atributos etc etc
  """
```