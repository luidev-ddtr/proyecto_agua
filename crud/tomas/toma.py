# Este sera el archivo crud el cual manejara las coneciones con la base de datos
import uuid
from utils.nucleo import Conexion
from models.toma_persona import TomaAgua
from crud.tomas.create import insertar_toma
from crud.tomas.read import registros
class Toma:
    """
    Clase la cual se encargadara de manejar la informacion con los endpoint 
    """
    def create(self, registro_json: dict) -> bool:
        """
        Funcion la cual se encargara de crear un nuevo registro en la base de datos
        Debe de recibir un json con la informacion nesesaria para crear una toma

        Args:
            registro_json (dict): Diccionario con la informacion de la toma
        
            Ejemplo de diccionario:

            {
                "ubicacion": "ubicacion",
                "usan_personas": "usan_personas"
            }
        """
        conexion_db= Conexion()
        registro_json["id_toma"] = id_generador(registro_json["ubicacion"], registro_json["usan_personas"])
        #crear_registro = Create()
        registro = TomaAgua(**registro_json)
        
        
        resultado = insertar_toma(registro,conexion_db)
        
        conexion_db.cerrar_conexion()
        
        if resultado:
            return True
        else:
            return False


    def show(self) -> bool:
        """
        Funcion la cual se encargara de crear un nuevo registro en la base de datos
        Debe de recibir un json con la informacion nesesaria para crear una toma
        """
        conexion_db= Conexion()
        mostrar_datillos=registros()
        #crear_registro = Create()
        
        resultado = mostrar_datillos.mostrar_todos_los_datos(conexion_db)
        
        conexion_db.cerrar_conexion()
        
        if resultado:
            return True
        else:
            return False
        




def id_generador(ubicacion: str, persnas_usan: int) -> str:
        """Genera un ID único con formato simplificado: 3LETRASID-AÑO-CODIGO.
        Formato: YYYY-mm-dd
        Ejemplo: 'cer-24-9b4f'
        Requisitos:
        - self.id_persona (ej: 'CERR')
        - self.año (ej: 2024)

        Returns:
            str: ID generado en minúsculas
        """
        prefijo = ubicacion[:3].lower()
        
        año = persnas_usan 
        
        random_code = uuid.uuid4().hex[:4]
        
        return f"{prefijo}-{año}-{random_code}"
