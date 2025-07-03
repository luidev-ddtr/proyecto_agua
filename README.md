# proyecto_agua
This is my first project with new tecnologies and git !!

# Lee la documentacion para instalar el proyecto

# Before the create

You need create a virtual ent (env), for work with flask 

# Project structure 

```mermaid
%% Diagrama de estructura de directorios para proyecto_agua con Flask
graph TD
    root["/proyecto_agua # Proyecto hecho con Flask y Python"]
    
    %% Entorno y base de datos
    root --> env["/env # Entorno virtual (NO se sube a Git)"]
    root --> base_datos["/base_datos # (Carpeta con base de datos SQLite)"]
    base_datos --> bd_mandho["bd_mandho.db # Archivo SQLite (NO subir con datos sensibles)"]
    
    %% CRUD Operations
    root --> crud["/crud"]
    crud --> personas_crud["/personas/persona.py # Lógica CRUD separada"]
    crud --> pago_agua["/pago_agua"]
    pago_agua --> create["create.py"]
    pago_agua --> read["read.py"]
    pago_agua --> update["update.py"]
    pago_agua --> delete["delete.py"]
    
    %% Modelos y rutas
    root --> models["/models # Modelos de Datos"]
    models --> persona_model["persona.py # Clase Persona"]
    models --> pago_model["pago_agua.py # Clase PagoAgua"]
    
    root --> routes["/routes # Endpoints API"]
    routes --> api_persona["api_persona.py"]
    routes --> api_pagos["api_pagos.py"]
    routes --> otros_rutas["# otros archivos (no usados)"]
    
    %% Utils y tests
    root --> utils["/utils # Helpers"]
    utils --> nucleo["nucleo.py # Conexión a BD"]
    
    root --> tests["/tests # Pruebas unitarias"]
    tests --> test_personas["test_personas.py # (Vacío)"]
    
    %% Frontend y archivos raíz
    root --> frontend["Frontend # Astro + Alpine.js"]
    root --> env_file[".env # Plantilla para variables"]
    root --> gitignore[".gitignore"]
    root --> requirements["requirements.txt"]
    root --> docs_img["/documentacion_img # Imágenes documentación"]
    root --> app["app.py # Punto de entrada principal"]
    
    %% Relaciones clave
    persona_model -.->|Usa| nucleo
    pago_model -.->|Usa| nucleo
    api_persona -.->|Consume| persona_model
    api_pagos -.->|Consume| pago_model
    crud -.->|Operaciones| models
    app -->|Importa| routes
    routes -->|Usa| crud
```

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