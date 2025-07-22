class TablaEstado:
    @staticmethod
    def obtener_estado(numero, conn):
        """
        Obtiene el nombre del estado especial según su ID.
        
        Args:
            numero (int): ID del estado especial (debe ser un ID válido existente).
            conn (Conexion): Objeto de conexión a la base de datos.
            
        Returns:
            str: Nombre del estado (ej. 'Madre soltera', 'Discapacitado').
            
        Raises:
            ValueError: Si el ID no existe en la tabla o es None.
        """
        if numero is None:
            raise ValueError("El ID del estado no puede ser None")
            
        cursor = conn.conexion()[1]  # Obtiene el cursor
        query = "SELECT NOMBRE FROM ESTADO_ESPECIAL WHERE ID_ESTADO = ?"
        cursor.execute(query, (numero,))
        
        resultado = cursor.fetchone()
        
        if not resultado:
            raise ValueError(f"No existe un estado especial con ID = {numero}")
        
        return resultado[0]  # Retorna el nombre del estado (ej. 'Discapacitado')