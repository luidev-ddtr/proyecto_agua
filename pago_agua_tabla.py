#Logica para tratar los datos de la tabla pagos_agua
#Este se deja para otro dia xdxdd
from clase_abstracta import BaseDatos
from nucleo import Conexion, Formateo
from datetime import datetime


class Registro:
    """Clase la cual guardara los datos en memoria para que se trabajen con ellos, 
    es indispensable de la otra tabla ya que sirve para hacer el CRUD."""

    def __init__(self, id_persona=None, tomas_agua=None, año=None, fecha_pago=None, estado_pago=None, cantidad=None):
        """Método para formatear fechas."""
        formatear = Formateo()
        formatear.formatear_fecha()
        
        
        self.id_persona = id_persona  # ID de la persona asociada al pago
        self.tomas_agua = tomas_agua  # Número de tomas de agua
        self.año = año  # Año del pago
        self.fecha_pago = fecha_pago  # Fecha del pago (formato YYYY-MM-DD)
        self.estado_pago = estado_pago  # Estado del pago (Pagado, Pendiente, Parcial)
        self.cantidad = cantidad  # Cantidad pagada


class TablaPagoAgua(BaseDatos):
    def agregar_dato(self, dato):
        pass
    


if __name__ == "__main__":
    #casos de prueba
    conexion_tabla = Conexion('../repo/bd_mandho.db')