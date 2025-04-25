Estos son los pasos para poder configurar tu entorno virtual 

primero ejecuta este comando dentro de tu caprte principal (en este caso proyecto agua)


# Crea el entorno virtual (se creará la carpeta 'env')
python -m venv env //Esto Creara el entorno virtual 


# Ejecuta este comando CADA VEZ que trabajes en el proyecto:
.\env\Scripts\Activate.ps1

(Te debe de aparecer algo asi )
Eso signfica que se activo completamente 

(env) PS ruta\a\tu\proyecto>


# Instala Flask y paquetes esenciales
pip install flask python-dotenv flask-sqlalchemy

# Si tienes un requirements.txt (opcional)
pip install -r requirements.txt

Crear variables de entorno 
FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=sqlite:///base_datos/bd_mandho.db



PROBAR LA APLICACION 



# 1. Activar el entorno virtual (si usas uno)
.\env\Scripts\Activate.ps1

# 2. Ejecutar la aplicación
flask run
# O alternativamente:
python app.py


CON VARIABLES DE ENTORNO 

# Opción 1: Usando variables de entorno
$env:FLASK_ENV="development"
$env:FLASK_DEBUG="1"
flask run

# Opción 2: Directamente en código (añade esto a app.py)
if __name__ == '__main__':
    app.run(debug=True)


ADICIONALES

# Ver todas las rutas disponibles
flask routes

# Ejecutar pruebas unitarias (si tienes archivos test_*.py)
python -m pytest -v

# Monitorear logs en tiempo real
Get-Content -Path "logs/app.log" -Wait  # Si guardas logs en archivo


# COMO SUBIR TUS CAMBOS A GIT SIN MORIRI EN EL INTENTO  
Opción 1: Agregar archivos modificados manualmente (recomendado para precisión)


git add app.py
git add tu_archivo_a.subir

# Opción 2: Usar git add -u (agrega solo archivos rastreados modificados)

git add -u

# Después de ejecutar cualquiera de estos comandos, verifica con:

git status

# Hacer el commit en el cual describes los cambios 
git commit -m "Tu mensaje descriptivo del commit"


# por ultimo usas git push para subir los cambios 











# CREAR UNA NUEVA RAMA YA QUE SE ELIMINO LA REMOTA PERO SIGUE ESTANDO LA LOCAL 
ASEGURATE QUE ESTES EN LA RAMA DESEADA 

git branch
  main
* rama-core

# SI QUIERES CAMBIAR EL NOMBRE LO HACES ASI 
git branch -m rama-core (NOMBRE ANTIGUO) rama-core-fix (NUEVO NOMBRE)



#  Paso 3: Sube la nueva rama al repositorio remoto
Ahora puedes subir tu rama (ya sea con el nombre original o el nuevo) a GitHub/GitLab/Bitbucket:

git push origin nombre-de-tu-rama-local


# ACTUALIZAR TU RAMA LOCAL CON CAMBIOS DEL REPOSITORIO REMOTO 

# Asegúrate de estar en main
git checkout main

# Descarga los últimos cambios del remoto (sin mergear)
git fetch origin

# Sincroniza tu main local con el remoto (¡cuidado con cambios locales no guardados!)
git reset --hard origin/main




# CREAR LAS NUEVAS RAMAS Y SINCRONIZARLAS EN REMOTO 

# Primero se crea en local 
git checkout -b build  