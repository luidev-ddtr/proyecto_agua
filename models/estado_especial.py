class TablaEstado:
    @staticmethod
    def obtener_estado(numero, conn):
        """
        Obtiene el nombre del estado especial según su ID.
        
        Args:
            numero (int/None): ID del estado especial (puede ser None)
            conn (Conexion): Objeto de conexión a la base de datos
            
        Returns:
            str: Nombre del estado o 'Ninguno' si no existe o es None
        """
        cursor = conn.conexion()[1]  # Obtiene el cursor
        query = "SELECT nombre FROM estados_especiales WHERE id = ?"
        cursor.execute(query, (numero,))
        
        resultado = cursor.fetchone()
        return resultado[0] if resultado else 'Ninguno'

