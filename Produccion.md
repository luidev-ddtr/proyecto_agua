#### ESTE ARCHIO ES PARA REDACTAR LOS REQUISITOS PARA PONER TU APLICACION FLASK EN PRODUCCION

## 1 Todo  lo previo

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

Recuerda debe ser modularizable, Dado que tu codigo lo escriben personas tienes que escribirlo con clases pequeñs y que solo cumplan su funcionalidad y no se mezcen logicas (Si no despues debbuggearlo o siquiera refactorizarlo se hace muy dificil)

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

## 2 Vamos a produccion !!

