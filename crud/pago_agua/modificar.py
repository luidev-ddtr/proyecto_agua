#clase para modificar a los registros de pago 
import datetime
class Modificate_register:
    def modificar_dato(self, ojeto, conexion_db):
        """Modifica los datos de una persona con validación de entradas.
        
        params
        :param dato Instancia de persona la cual tiene la informacion
        :param conexion_db Instancia de la clase Conexion.
        """
        conexion, cursor = conexion_db.conexion()
        
        campos_modificables = {
            3: ('tomas_agua', int),             # Tomas de Agua
            5: ('fecha_pago', 'date'),          # Fecha de Pago
            7: ('cantidad', float)              # Cantidad
        }

        campos_no_modificables = {
            1: ('id', str),                     # ID (no modificable)
            2: ('id_persona', str),             # ID Persona (no modificable)
            4: ('año', str),                    # Año (aunque es str, lo mantienes modificable?)
            6: ('estado_pago', str),            # Estado de Pago (calculado, no modificable)
            8: ('tarifa_pendiente', str)        # Tarifa Pendiente (calculada, no modificable)
        }

        while True:
            print(f"""\nMENU DE MODIFICAR REGISTRO
            Datos actuales:
            ----------------------
            1) ID: {ojeto.id_registro} [NO MODIFICABLE]
            2) ID Persona: {ojeto.id_persona} [NO MODIFICABLE]
            3) Tomas de Agua: {ojeto.tomas_agua}
            4) Año: {ojeto.año} [NO MODIFICABLE]
            5) Fecha de Pago: {ojeto.fecha_pago}
            6) Estado de Pago: {ojeto.estado_pago} [NO MODIFICABLE]
            7) Cantidad: {ojeto.cantidad}
            8) Tarifa Pendiente: {ojeto.tarifa_pendiente} [NO MODIFICABLE]
            ----------------------
            Opciones:
            3,4,5,7. Modificar campo correspondiente
            9. Guardar y salir""")
            
            opcion = input("Seleccione una opción: ").strip()
            
            if opcion == '9':
                # Guardar todos los cambios y salir
                conexion_db.guardar_cambios()
                print("✓ Todos los cambios guardados correctamente")
                break
                
            if not opcion.isdigit() or int(opcion) not in campos_modificables:
                print("¡Opción no válida! Solo puede modificar los campos 3,4,5,7")
                continue
                
            opcion = int(opcion)
            campo, tipo = campos_modificables[opcion]
            
            if tipo == int:  # Campo Tomas de agua
                while True:
                    valor = input("Ingrese la nueva cantidad de tomas de agua: ")
                    if valor.isdigit():
                        nuevo_valor = int(valor)
                        break
                    print("Error: Debe ingresar un número entero")
                    
            elif tipo == 'date':  # Fecha de pago
                while True:
                    valor = input("Ingrese la nueva fecha de pago (YYYY-MM-DD): ").strip()
                    try:
                        datetime.strptime(valor, '%Y-%m-%d')
                        nuevo_valor = valor
                        break
                    except ValueError:
                        print("Formato incorrecto. Use AAAA-MM-DD (ej. 2000-05-15)")
                        
            elif tipo == float:  # Cantidad
                while True:
                    valor = input("Ingrese la cantidad recibida: ").strip()
                    try:
                        nuevo_valor = float(valor)
                        break
                    except ValueError:
                        print("Error: Debe ingresar un número válido (ej. 150.50)")
                        
            setattr(ojeto, campo, nuevo_valor)
            
            # Actualizar la base de datos
            try:
                cursor.execute(f"UPDATE registros SET {campo} = ? WHERE id_registro = ?", 
                            (nuevo_valor, ojeto.id_registro))
                conexion_db.guardar_cambios()
                print("✓ Cambio guardado")
            except Exception as e:
                print(f"× Error al actualizar en BD: {str(e)}")
                continue