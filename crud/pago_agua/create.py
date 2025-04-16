#Logica para crear un registro y meterlo a la bd
from models.pago_agua import Registro
from utils.nucleo import Conexion
class Create:
    def agregar_registro(self, registro, conexion_bd):
        """Metodo para introducir registros a la base de datos"""
        conexion, cursor = conexion_bd.conexion()
        
        query = """
        INSERT INTO pagos_agua 
        (id, persona_id, tomas_agua, año, fecha_pago, estado_pago, cantidad, tarifa_pendiente)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        valores = (
            registro.id_registro,
            registro.id_persona,
            registro.tomas_agua,
            registro.año,
            registro.fecha_pago,
            registro.estado_pago,
            registro.cantidad,
            registro.tarifa_pendiente
        )
        cursor.execute(query, valores)
        conexion_bd.guardar_cambios()
        print("✅ Datos insertados correctamente.")
        
    
if __name__ == "__main__":
    print("Menu de pagos agua")
    añadir = Create()
    conexion_bd = Conexion('base_datos/data_base.db')
    "Los datos ingresados desde el front son id_persona, tomas_agua, año, fecha de pago, cantidad"
    registro_pago = Registro("CER-24-34dr",5, "2024", "2024-01-24", 500) 
    
    
    conexion_bd.cerrar_conexion()



