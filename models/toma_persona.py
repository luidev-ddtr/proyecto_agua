class TomaAgua:
    """
    Esta clase sera el modelo de datos el cual estara mapeado con la base de datos y 
    servira para guardar la informacion de la toma de agua
    """
    def __init__(self, id_toma, ubicacion: str, usan_personas: int) -> None:
        self.id_toma = str(id_toma)
        self.ubicacion = str(ubicacion)
        self.usan_personas = int(usan_personas)

    def to_dict(self) -> dict[str]:
        """
        Convierte la instancia de TomaAgua en un diccionario.
 
        Returns:
            dict: Un diccionario con las claves 'id_toma', 'ubicacion', y 'usan_personas'
            correspondientes a los atributos de la instancia.
        """
        
        return {
            "id_toma": self.id_toma,
            "ubicacion": self.ubicacion,
            "usan_personas": self.usan_personas
        }

    def __str__(self) -> str:
        return f"TomaAgua(id_toma={self.id_toma}, ubicacion={self.ubicacion}, usan_personas={self.usan_personas})"