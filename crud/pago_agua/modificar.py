#clase para modificar a los registros de pago 
import datetime
class Modificate_register:
    def modificar_dato(self, objeto, conexion_db):
        """
        Modifica los datos editables de una persona en la base de datos.
        
        Args:
            objeto (Persona): Instancia de Persona con la información actualizada
            conexion_db (Conexion): Instancia de la clase Conexion
        
        Returns:
            bool: True si la actualización fue exitosa, False si hubo error
        """
        try:
            conexion, cursor = conexion_db.conexion()
            
            
            # Consulta SQL con campos editables
            consulta_sql = """
                UPDATE pagos_agua 
                SET fecha_pago = ?, 
                    estado_pago = ?,
                    cantidad = ?,
                    tarifa_pendiente = ?
                WHERE id = ?
            """
            # Valores para la consulta
            valores = (
                objeto.fecha_pago,
                objeto.estado_pago,
                objeto.cantidad,
                objeto.tarifa_pendiente,
                objeto.id_registro
            )
            # Ejecutar la consulta
            cursor.execute(consulta_sql, valores)
            
            # Verificar si se actualizó algún registro
            if cursor.rowcount == 0:
                print(f"⚠️ Advertencia: No se actualizó el registro ID: {objeto.id_registro}")
                return False
            
            # Confirmar cambios
            conexion_db.guardar_cambios()
            print(f"✅ Éxito: Registro ID: {objeto.id_registro} actualizado correctamente")
            return True
            
        except Exception as e:
            print(f"❌ Error crítico al actualizar registro ID {objeto.id_registro}:")
            print(f"Tipo de error: {type(e).__name__}")
            print(f"Mensaje: {str(e)}")
            
            # Intentar hacer rollback si la conexión sigue activa
            try:
                if 'conexion' in locals() and conexion:
                    conexion.rollback()
                    print("↩️ Se realizó rollback de la transacción")
            except Exception as rollback_error:
                print("⚠️ Error al intentar hacer rollback:", str(rollback_error))
            
            return False