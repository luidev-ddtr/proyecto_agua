#### ESTE ARCHIO ES PARA REDACTAR LOS REQUISITOS PARA PONER TU APLICACION FLASK EN PRODUCCION

### 1 Todo  lo previo

Primero tener todo configurado y funcionando correctamente en desarrollo

# 1.1  codigo vs configuracion

Recuerda aunque el codigo y la logica del negocio son muy importante incluso
son la base de la app, otra parte que es importante para que una aplicacion funcona y sea amntenible 
es tener una base solida y buena calidad del codigo ya que es leido y manipulado por personas (aun)

# 1.2 configuracion

Tener todas las configuraciones correctas 

tener git y tus ramas en un buen orden y con estructura (tener las nociones de git)

configurar y siempre trabajar en un venv (Entorno virtual)

tener tu requerimets .txt (si trabajars con mas desarrollares y los proyectos sean compartidos)

tener todo tu codigo en sus respectivas carpetas y que respetes las pocas reglas que ofrece el framework

No olvides ir llevando registro de los cambios que vas haciendo

## 1.3 Codigo

Hay recordar los pequeños detalles sobre el codigo para tener una buena base y codigo de buena calidad

Investigar si ya hay librerias que te ayudan a solucionar o almenos proporcionan algo de mejora al problema que te enfrentas

Recuerda debe ser modularizable, Dado que tu codigo lo escriben y leen personas tienes que escribirlo con clases pequeñas y que solo cumplan su funcionalidad y no se mezcen logicas (Si no despues debbuggearlo o siquiera refactorizarlo se hace muy dificil)

Poner tus archivos __init__.py para que tu codigo pueda importarse y usarse como modulo en otros ficheros

Usar POO es el mejor enfoque que conozco ordena el codigo de una manera muy uff !! increible

### Usar enfoque POO xd (seguimos)

Mantener tu app.py lo mas limpia posible, recuerda que pues poner los entpoins en otra carpeta llamada routes / tus-rutas-py

Esto asegurara un codigo de muy buena claidad y facil de trabajar para ti y tu equipo

No olvides harcodear tus url para que mientras tu codigo vaya creciendo y despues tengas que hacer cambios no tengas que estar chicero por fichero cambiando rutas manualmente (igual sirve en el front)

# 1.3 Usar git

ya existe un archivo llamado condigurar el env.md en el cual estan los comandos de git ademas de como instalar 
tener tu env

# base de datos

Trata de abstraer la logica de tu base de datos en otro fichero para hacer de tu codigo lo mas agnostico posible al gestor de bd (Agnostico que se pueda cambiar facilmente sin requerir modificaciones profundas)


Esto en mi opinion asegurara un buen codigo y proyecto en general de forma limpia y ordenada LEE el readme

# 1.4 NO OLVIDES LEER LA DOCUMENTACION 

Aunque ciertamente esta en ingles y es dificil encontrar el problema o la herramienta esperada esta es muy importante ya que te ayuda a poder resolver tus dudas y pues te ahorra estar con la ia peleando por qu eno funciona algo

## 1.9 ESTAS SERIAN LAS BUENAS PRACTICAS PARA TENER UN BUEN CODIGO LISTO PARA PRODUCCION 

### 2 Vamos a produccion !!

## Lo primero 

# Lee la documentacion y busca si tu proyecto es compatible con el servicio que se utilizara

Este paso es fundamental y te ahorrara horas y horas de no saber por que no funciona el archivo, verificalo 
y has caso a la siguiente, pregunta a la ia si tienes flojera solamente confirmalo

# Ramas de git

Recuerda la rama main en la mas importante lo ideal es hacer el deploy tanto de front como de back en ramas separadas mientras que la ramma main sea la que tiene el codigo fuente 

## Empezemos 

# despliegue de appliacion (backend con flask) en el servicio python anywhere

Lo primero leer un poco sobre el servicio que se contratara los servicios que ofrece y si es confiable (vamos investigar almenos un poco)

# Git (otra vez) 

Debido a que generalmente una persona desarrolla su proyecto en local cuando lo va adeployar ya tiene un proyecto funcional en desarrollo. pytho Anywhere (de ahora en adelante panywhare)  ofrece la opcion de clonar un repositiorio de git existente para desde ahi traer el codigo fuente del proyecto (src)

# iniciar

Debido al serivicio gratutito y a como funcionan los servicios proveedores de backend en general la consola (computadora proporcionda para tu programa) esta escrita en linux por lo que tienen que tener nociones basicas del funcionamiento, los paso a hacer son, inicializar tu repositorio local, clonar el remoto y traer el codigo
 
1. traer el codigo

2. crear tu env, Esto se puede hacer con el comando pip install python-dotenv mydotenv (la ultima palbra es como quieres que se llame), Es poisble gracias a la ayuda que proveen estos servicios, Se explica mejor al final de este punto.

3. Instalar las dependencias puedes tener un requeriments.txt el cual ya tiene todas las dependecias para que no tengas que hacerlo manuelamente 

3. 99999 ¿Por que tan facil?, Debido a que panywhare ya hace todo el trabajo sucion, por ejemplo configura waitress (herramienta para produccion que hace la misma chamba que wzeug pero para deploy), ademas de que ya condigura un proxi inverso (servidor web para que flask se puede comunicar sin problemas), Aqui la verdad no se que herramienta utilize, lo mas probable es que sea apache http, Sim embargo panywhare ya te abstrae toda esa configuracion y solo te deja con lo que vendria siendo la configuracion final para deployar

## Aviso para esto ya tienes que tener nocion de como utilizar las herrmaientas provistas por panywhare 

# Buscar tu framework !! 

Panywhare ofrece soporte para distintos frameworks escritos en python por ejemplo: django, flask, web2py (buscar si hay soporte para fast api), por lo que solo tienes que elegir tu framework y su version, la version de python.

# Web app

Una vez configurado esto se te mostrara en pantalla el prebuild de tu app aunque tecnicamente ya esta lista aun faltan algunos detalles

# Configurar rutas 

Aunqeu tu ya elegiste que flask y te version de python aun tiene que hacer algunas rutas, la mas importante, conectar a la carpeta la cual tiene tu env (Entorno virtual)

para que tu proyecto se puede levantar sin problemas, Ademas si (Eres retrasado) y tiene archivos estaticos desplegados por tu app tienes que condigurar la ruta

# app.py

Esto no lo recuerdo bien pero en algun punto poner el inicio de tu app como app.py (o el nombre que hayas elegido)
por lo que tienes que ir a files y copiar nuevamente el codigo que tuvieses ahi ya que panywhare le da por cambiarlo por un hola mundo 

ejemplo de como se ve app.py antes y despues de cargar 


```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hola desde Flask"  # ← Plataforma lo sobreescribe

if __name__ == '__main__':
    app.run()
```

```python
import os
from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_cors import CORS

# Carga el .env con ruta ABSOLUTA (crítico en PythonAnywhere)
load_dotenv('/home/Luidev/proyecto_agua/.env') #cargar el entorno virtual con una ruta absoluta

app = Flask(__name__)


# Configura CORS (usa .strip('"') para eliminar comillas del .env)
CORS(app, resources={
    r"/api/*": {
        "origins": os.getenv('URL_FRONTEND').strip('"'),  # ¡Sin comillas!
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"],
        "supports_credentials": True
    }
 } ## Mas codigo...
)  
```

# .env

Este es un paso importantisimo ya que si es mi caso y tu .env es importante (ya sea para el uso de jtk o harcodear url), tienes que configurarlo de una forma  manual ya que en caso contrario tu app no funcionara, 

Se configura de la siguiente forma, primero, al ser un archivo especial le tienes que quitar permiso (que solo sea de uso expclusivo de la app y que nadie mas pueda lerlo)

```bash
(myvenv) 02:40 ~/proyecto_agua (main)$hmod 600 /home/Luidev/proyecto_agua/.envnv
(myvenv) 02:42 ~/proyecto_agua (main)$ ls -la /home/Luidev/proyecto_agua/.env
-rw------- 1 Luidev registered_users 653 May  4 02:37 /home/Luidev/proyecto_agua/.env
```

```python
#en el .env tener esto 
URL_FRONTEND="https://luidev-ddtr.github.io"

#en tus ficheros tener esto 
"origins": [os.getenv('URL_FRONTEND')], ##Asi la url esta hardcoreada
```


# Base de datos 

En el ejemplo anterior se tuilizo sqlite para para base de datos, sin embargo panywhare ofrece servicios para base de datos como lo es posgre y mysql, En este ejemplo se habla de la experiencia de usar sqlite,

primero utilizas tu squema (previamente creado de tu base real), y crear tu base de datos, ademas le tienes que agregar permisos (ya que al ser un archio interno Es una BD pero no es como posgre que esta a parte),  esto lo haces desde consola, ejemplo tiene que verse algo asi los permisos 

```bash
(myvenv) 02:41 ~/proyecto_agua (main)$hmod 664 /home/Luidev/proyecto_agua/base_datos/data_base.dbdb
(myvenv) 02:42 ~/proyecto_agua (main)$ ls -la /home/Luidev/proyecto_agua/.env
-rw------- //este permiso representa que solo el programa lo puede modificar 
```

# Log`s de panywhare 

Una mierda !! Pero sirven 

## Hacer pruebas

Aunque por lo que recuerdo ya esta seria toda la configurarion, Es recomendable hacer pruebas de tu programa Debido a que los log`s no funcionan lo mejor (para probar la api), es mandandole los mensajes a travez de terminal
en formato json (Lo mas facil de configurar son las tipo  GET), ya que el programa (si ya esta configurado), te respondera.
```bash
(myvenv) 02:43 ~/proyecto_agua (main)$url -X GET "https://luidev.pythonanywhere.com/api/read_pay" -H "Origin: https://luidev-ddtr.github.io"o"
{"Perfecto":[]}
```

## Refrescar

No olvides que depues de cada cambio tienes que refrescar el contenido servido, para que los cambios se vean reflejados, sim embargo se recomienda hacer la mayor cantidad de condiguraciones antes de siquiera subir la app

## Con esto ya se tendria una configuracion muy buena para el programa, se haria mas facil de recordar
