#Logica para guardar un registro en memoria, el cual seria utilizado por el crud y la bd 
import uuid

class TarifaPago:
    """Clase para calcular cobros periódicos basados en un costo diario.
    
    Esta clase proporciona una forma flexible de calcular cobros anuales y mensuales
    a partir de un costo diario base. Fue diseñada pensando en la escalabilidad para
    futuros métodos de pago o cambios en la estructura de costos.
    
    Atributos:
        _cobro_diario (float): Costo base por día (default: 1)
        _costo_servicio (float): Costo total anual calculado
        _costo_servicio_mensual (float): Costo mensual calculado
    """
    
    def __init__(self):
        """Inicializa la instancia con el año para cálculos.
        
        Args:
            año (int): Año para el cual se realizarán los cálculos.
                       Nota: Actualmente el año no afecta el cálculo.
        """
        self._cobro_diario = 1  # Valor por defecto (1 peso por día)
        self._costo_servicio = self._calcular_costo_anual(0)
        self._calcular_costo_mensual()
    
    def _calcular_costo_anual(self, año):
        """Calcula el costo anual basado en el cobro diario.
        
        Args:
            año (int): Año de referencia (no utilizado actualmente)
            
        Returns:
            float: Costo anual (365 * cobro_diario)
        """
        # Actualmente el cálculo no considera años bisiestos
        # Se mantiene el parámetro año para futuras implementaciones
        return 365 * self._cobro_diario
    
    def _calcular_costo_mensual(self):
        """Calcula el costo mensual dividiendo el anual entre 12."""
        self._costo_servicio_mensual = self._costo_servicio / 12
    
    def get_costo_anual(self):
        """Obtiene el costo anual calculado.
        
        Returns:
            float: Costo anual del servicio
        """
        return self._costo_servicio
    
    def get_costo_mensual(self):
        """Obtiene el costo mensual calculado.
        
        Returns:
            float: Costo mensual del servicio
        """
        return self._costo_servicio_mensual
    
    def set_cobro_diario(self, nuevo_costo):
        """Actualiza el cobro diario y recalcula costos anual/mensual.
        
        Args:
            nuevo_costo (float): Nuevo valor para el cobro diario
        """
        self._cobro_diario = nuevo_costo
        self._costo_servicio = self._calcular_costo_anual()
        self._calcular_costo_mensual()

class Registro:
    """Clase para gestionar registros de pagos de agua con estados específicos y generación de IDs.
    
    Diferenciación entre registros nuevos (sin ID) y cargados desde BD (con ID).
    Maneja 3 estados de pago: 0 (faltante), 1 (completo).
    
    Atributos:
        id_registro (str): Identificador único generado o cargado desde BD
        id_persona (str): ID de la persona asociada
        tomas_agua (int): Tomas de agua relacionadas
        año (str): Año de referencia
        fecha_pago (str): Fecha del último pago
        cantidad (int): Cantidad total a pagar
        estado_pago (int): Estado actual del pago (0, 1)
    """

    def __init__(self ,id_persona=None, tomas_agua=None, año=None, 
                    fecha_pago=None, cantidad=0, estado_pago=0, 
                    tarifa_pendiente = None, id_registro=None,recalcular = None):
        """Inicializa un registro de pago de agua.
        
        Args:
            id_registro (str, optional): ID existente. Si es None, se genera uno nuevo.
            id_persona (str, optional): Identificador de la persona asociada.
            tomas_agua (int): Lista de tomas de agua relacionadas.
            año (str, optional): Año del registro (formato YYYY-MMM-DD) iso.
            fecha_pago (str, optional): Fecha del último pago (formato YYYY-MM-DD).
            estado_pago (int, optional): Estado inicial del pago (0, 1). Si es None, se calcula.
            cantidad (int, optional): Cantidad total a pagar. Requerido para nuevos registros.
            
        Raises:
            ValueError: Si cantidad no es provista para un nuevo registro.
        """
        #Registro nuevo
        if id_registro is None and recalcular is None:
            self.id_persona = str(id_persona)
            self.tomas_agua = str(tomas_agua) 
            self.año = str(año) #Al inicio si ya que año se pasa como entero mas no str
            self.id_registro = str(self.generar_id())
            self.fecha_pago = str(fecha_pago)
            self.cantidad = int(cantidad)
            self.estado_pago, self.tarifa_pendiente = self.calcular_estado(estado_pago,tarifa_pendiente)
            print("Nuevo registro from models/pago_agua")
        #para diferenciar entre datos traidos de la bd y datos a modificar
        elif recalcular == True:
            self.id_registro = str(id_registro)
            self.id_persona = str(id_persona)
            self.tomas_agua = str(tomas_agua) 
            self.año = str(año)
            self.fecha_pago = str(fecha_pago)
            self.cantidad = int(cantidad)
            self.estado_pago, self.tarifa_pendiente = self.calcular_estado(estado_pago,tarifa_pendiente)
        else:
                #Datos cargados desde la bd
            self.id_registro = str(id_registro)
            self.id_persona = str(id_persona)
            self.tomas_agua = str(tomas_agua) 
            self.año = año
            self.fecha_pago = fecha_pago
            self.cantidad = int(cantidad)
            self.estado_pago = estado_pago
            self.tarifa_pendiente = tarifa_pendiente  
            print("registro editar from models/pago_agua")

    def generar_id(self):
        """Genera un ID único con formato simplificado: 3LETRASID-AÑO-CODIGO.
        Formato: YYYY-mm-dd
        Ejemplo: 'cer-24-9b4f'
        Requisitos:
        - self.id_persona (ej: 'CERR')
        - self.año (ej: 2024)

        Returns:
            str: ID generado en minúsculas
        """
        prefijo = self.id_persona[:3].lower()
        
        año = self.año[2:4] 
        
        random_code = uuid.uuid4().hex[:4]
        
        return f"{prefijo}-{año}-{random_code}"

    def calcular_estado(self,estado_pago, tarifa_pendiente):
        """Calcula el estado del pago basado en la fecha de pago y lógica de negocio.
        
        Estados:
            0: Faltante (sin fecha de pago)
            1: Parcial (lógica a implementar según requisitos)
            2: Completo (pago confirmado)
            
        Returns:
            int: Estado del pago (0, 1)
        """
        calcular = CalculadoraCobro()
        return calcular.calcular_pago_unitario(self.cantidad, self.tomas_agua,estado_pago,tarifa_pendiente)

    def ver_datos(self):
        """Muestra todos los datos del registro y su estado actual de forma legible.
        
        Returns:
            str: Cadena formateada con todos los atributos y cálculos importantes.
        """
        datos = f"""
        ╔═══════════════════════════════════════════
        ╟──📝 REGISTRO DE PAGO DE AGUA
        ╠═══════════════════════════════════════════
        ║ ID Registro: {self.id_registro}
        ║ ID Persona: {self.id_persona}
        ║ Año: {self.año}
        ╠═══════════════════════════════════════════
        ║ 🚰 Tomas de agua: {self.tomas_agua}
        ║ 💰 Cantidad abonada: {self.cantidad}
        ║ 📅 Fecha de pago: {self.fecha_pago}
        ╠═══════════════════════════════════════════
        ║ 🏷️ Estado actual: {self.estado_pago}
        ║ 🧾 Tarifa pendiente: {self.tarifa_pendiente}
        ╚═══════════════════════════════════════════
        """
        print(datos)
class CalculadoraCobro:
    """Clase especializada en calcular los cobros de agua según diferentes criterios.
    
    Responsabilidades:
    - Calcular el monto total a pagar según consumo y tarifas
    - Determinar pagos parciales o completos
    - Calcular posibles descuentos o recargos
    - Gestionar la lógica compleja de cálculo separada de la entidad Registro
    
    -Si el estado especial coincide con estos criterios
    ("usuario especial"), ("comercial/industrial")
    Se deben de tratar estos casos especiales
    """
    def calcular_pago_unitario(self, cantidad, tomas_agua, estado = 0, tarifa_pendiente=None,):
        """Calcula el pago unitario y devuelve el estado actualizado y el saldo pendiente.
        
        Args:
            cantidad (float): Monto abonado.
            tomas_agua (int): Número de tomas de agua.
            estado (int): Estado actual del pago (0: pendiente, 1: completo).
            tarifa_pendiente (float, optional): Saldo pendiente previo (para estado=0).
            
        Returns:
            tuple: (nuevo_estado, saldo_pendiente)
                - nuevo_estado (int): 0, 1.
                - saldo_pendiente (float): Cantidad restante a pagar.
                
        Raises:
            ValueError: Si los argumentos son inválidos.
        """
        pago_servicio = TarifaPago()
        pago_anual = pago_servicio.get_costo_anual()
        

        # if tomas_agua > 1 and tarifa_pendiente is None: #para validar los casos en que el registro ya viene con tarifa pendiente 
        #     pago_anual = pago_anual * tomas_agua
        pago_anual = 360
        # Lógica general
        if estado == 1:
            return 1, 0  # Pago ya completado
        
        elif estado == 0 and tarifa_pendiente is None: #Estado pendiente Si estado no existe se le asigna cero por defecto
            
            tarifa_pendiente = pago_anual
            
            tarifa_pendiente = tarifa_pendiente - cantidad
            
            if tarifa_pendiente <= 0:
                return 1, 0  # Pago completado
            else:
                return 0, tarifa_pendiente
            # Este se calcula cuando la tarifa pendiente ya existe para que no se tome el año
        else:
            tarifa_pendiente = tarifa_pendiente - cantidad
            
            if tarifa_pendiente <= 0:
                return 1, 0  # Pago completado
            else:
                return 0, tarifa_pendiente