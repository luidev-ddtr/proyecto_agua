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