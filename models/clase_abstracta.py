#Fichero de la clase abstracta para las tablas
from abc import ABC, abstractmethod

class BaseDatos(ABC):
    @abstractmethod
    def agregar_dato(self, dato):
        """
        Agrega un nuevo registro a la base de datos.
        :param dato: El dato a agregar. Debe ser un objeto con los atributos necesarios.
        """
        pass

    @abstractmethod
    def modificar_dato(self, dato):
        """
        Modifica un registro existente en la base de datos.
        :param dato: El dato a modificar. Debe ser un objeto con los atributos necesarios.
        """
        pass

    @abstractmethod
    def eliminar_dato(self, dato):
        """
        Elimina un registro de la base de datos.
        :param dato: El dato a eliminar. Debe ser un objeto con los atributos necesarios.
        """
        pass
    def mostrar_datos(self):
        """
        Muestra todos los registros de la base de datos.
        """
        # Lógica para mostrar los datos
        pass

    def agregar_muchos_datos(self,lista):
        """Esta clase servira para agregar muchos datos a la bd,
        Principalmente servira para migraciones """
        pass