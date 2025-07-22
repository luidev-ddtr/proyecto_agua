#archivo el cual servida conexion con la bd
import uuid
from datetime import datetime

class Persona:
    def __init__(self, nombre, apellidos, estado_especial, manzana, estudia, fecha_nac, id_persona=None):
        """
        Constructor de la clase Persona.
        Args:
            nombre (str): Nombre de la persona (mapeado a campo TEXT NOT NULL)
            apellidos (str): Apellidos completos (mapeado a campo TEXT NOT NULL)
            estado_especial (int): ID del estado especial (mapeado a INTEGER, puede ser NULL)
            manzana (str): Manzana donde reside (mapeado a TEXT, puede ser NULL)
            estudia (int): Indicador de estudios (0=False, 1=True, mapeado a INTEGER DEFAULT 0)
            fecha_nac (str/): Fecha de nacimiento (puede ser string 'YYYY-MM-DD' INTEGER)
            id_persona (str/None): ID único (mapeado a TEXT PRIMARY KEY). Si es None, se genera automáticamente.
        
        Notas de mapeo SQL-Python:
            - Los campos TEXT NOT NULL se validan como strings no vacíos
            - Los campos INTEGER para booleanos se convierten: 0=False, 1=True
            - fecha_nacimiento se almacena como INTEGER (timestamp) en DB pero se maneja como string en Python
            - estado_especial es clave foránea a estados_especiales(id)
        """
        self.nombre = nombre
        self.apellidos = apellidos
        self.estado_especial = int(estado_especial)
        self.manzana = manzana
        self.estudia = int(estudia)
        self.fecha_nac = fecha_nac
        edad = self.calculate_age()
        self.activo = self.is_active(edad)
        
        if id_persona is None:
            # Datos del frontend: generar ID
            self.id_persona = self.generar_id_aleatorio()
        else:
            # Datos de la base de datos: asignar ID
            self.id_persona = id_persona
        print("\nDatos cargados correctamente.")

    def generar_id_aleatorio(self):
        """Genera un ID legible compuesto por datos semánticos y un componente aleatorio.
        Formato: MANZANA-INICIALES-AÑO-CODIGO (ej: CER-JM-20-9b4f)
        """
        # 1. Obtener iniciales (primer letra del nombre + primer letra del primer apellido)
        iniciales = f"{self.nombre[0].upper()}{self.apellidos.split()[0][0].upper()}"
        
        # 2. Obtener código de manzana (3 primeras letras en mayúscula)
        manzana = self.manzana[:3].upper()
        
        # 3. Obtener año de nacimiento (2 últimos dígitos)
        año_nac = self.fecha_nac.split('-')[0][-2:]
        
        # 4. Parte aleatoria (4 caracteres hexadecimales en minúscula)
        random_part = uuid.uuid4().hex[:4]
        
        # Ensamblar el ID final
        return f"{manzana}-{iniciales}-{año_nac}-{random_part}"

    def calculate_age(self):
        """
        Calcula la edad a partir de la fecha de nacimiento.
        :return: La edad en años.
        :raises ValueError: Si la fecha de nacimiento no tiene el formato correcto o es inválida.
        """
        try:
            # Verificar si self.fecha_nac es None o está vacío
            if not self.fecha_nac:
                raise ValueError("La fecha de nacimiento no puede estar vacía.")
            
            # Convertir la fecha de nacimiento a un objeto datetime
            fecha_nacimiento = datetime.strptime(self.fecha_nac, '%Y-%m-%d')
            
            # Calcular la edad
            hoy = datetime.today()
            edad = hoy.year - fecha_nacimiento.year
            if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
                edad -= 1
            
            return edad
        except ValueError as e:
            print(f"Error al calcular la edad: {e}")
            raise 
    
    def is_active(self, edad):
        """
        Determina si la persona está activa basándose en su edad, estado especial y si estudia.
        
        Args:
            edad (int): Edad de la persona
            
        Returns:
            int: 1 si la persona está activa, 0 en caso contrario
            
        """
        # Determinar si la persona está activa
        if (18 <= edad <= 65) and (self.estado_especial == 1):
            return 1
        return 0
