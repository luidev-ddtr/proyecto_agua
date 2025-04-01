#Fichero el cual creara la instancia de flask #     Creara el servidor
from flask import Flask

app = Flask(__name__)

@app.route("/")
def prueba():
    return "<h1>Hola mundo con pyScript</h1>"

@app.route("/mostrar_personas")
def mostrar_datos():
    #Logica para manejar la petiicon que llega y mostrar las personas 
    return "<h1>Funcion que retorndara a las persona alv alv  pyScript</h1>"


if __name__ == '__main__':
    app.run(debug=True)
    