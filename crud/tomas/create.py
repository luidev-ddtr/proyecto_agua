def insertar_toma(objeto_toma: object ,conexion_bd: object):
    """
    Funcion que ingresara la informacion a la base de datos en la tabl atoma de agua 
    Args:
        objeto_toma (object): Objeto de la clase toma de agua
        conexion_db (object): Objeto de la clase conexion a la base de datos

    Returns:
        bool: True si la actualizacion fue exitosa, False si hubo error


    anotaciones: La tabla es la siguiente:
        id_toma
        ubicacion
        usan_personas
    """
    conexion, cursor = conexion_bd.conexion()
    
    query = """
    INSERT INTO TOMA_AGUA 
    (ID_TOMA, UBICACION, PERSONAS_USAN)
    VALUES (?, ?, ?)
    """
    print("bander1")
    valores = (
        objeto_toma.id_toma,
        objeto_toma.ubicacion,
        objeto_toma.usan_personas
    )
    cursor.execute(query, valores)
    conexion_bd.guardar_cambios()
    print("bander2")
    if cursor.rowcount > 0:
        print("✅ Datos insertados correctamente.")
        return True
    print("⚠️ No se insertaron datos (posiblemente hubo un error o las condiciones no se cumplieron).")
    return False