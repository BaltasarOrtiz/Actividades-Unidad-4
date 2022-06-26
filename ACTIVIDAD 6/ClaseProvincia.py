

class Provincia:
    __nombre : str
    __capital : str
    __cantidadHabitantes : int
    __cantidadDepartamentos: int
    __temperatura : float
    __humedad : float
    __sensacionTermica : float


    def __init__(self, nombre, capital, cantidadHabitantes, cantidadDepartamentos, temperatura="", humedad="", sensacionTermica=""):
        self.__nombre = self.requerido(nombre, 'Apellido es un valor requerido')
        self.__capital = self.requerido(capital, 'Capital es un valor requerido')
        self.__cantidadHabitantes = self.requerido(int(cantidadHabitantes), 'Cantidad de habitantes es un valor requerido')
        self.__cantidadDepartamentos = self.requerido(int(cantidadDepartamentos), 'Cantidad de departamentos es un valor requerido')
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__sensacionTermica = sensacionTermica
    
    #Provincia
    def getNombre(self):
        return self.__nombre

    def getCapital(self):
        return self.__capital
    
    def getCantidadHabitantes(self):
        return self.__cantidadHabitantes
    
    def getCantidadDepartamentos(self):
        return self.__cantidadDepartamentos

    #Clima
    def getTemperatura(self):
        return self.__temperatura
    
    def getHumedad(self):
        return self.__humedad

    def getFeelLike(self):
        return self.__sensacionTermica
    
    #sets 
    def setTemperatura(self, temperatura):
        self.__temperatura = temperatura
    
    def setHumedad(self, humedad):
        self.__humedad = humedad
    
    def setFeelLike(self, sensacionTermica):
        self.__sensacionTermica = sensacionTermica
    

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                nombre=self.__nombre,
                capital=self.__capital,
                cantidadHabitantes=self.__cantidadHabitantes,
                cantidadDepartamentos=self.__cantidadDepartamentos,
                temperatura=self.__temperatura,
                humedad=self.__humedad,
                sensacionTermica=self.__sensacionTermica
                )
            ) 
        return d
        
    
    #VALIDACION
    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor