class Fraccion:
    __numerador = 0
    __denominador = 0

    def __init__(self, fraccion):
        if len(fraccion) == 1:
            self.__numerador = int(fraccion[0])
            self.__denominador = 1
        else:
            self.__numerador = int(fraccion[0]) 
            self.__denominador = int(fraccion[1])

    def getFraccion(self):
        numero = "0"
        if self.__numerador != numero:
            numero = (str(self.__numerador)+"/"+str(self.__denominador))
        if self.__denominador == 1:
            numero = str(self.__numerador)
        return numero

    def __add__(self, other):
        self.__numerador = self.__numerador*other.__denominador + self.__denominador*other.__numerador
        self.__denominador =  self.__denominador*other.__denominador
        self.simplificar()
        return self.getFraccion()


    def __sub__(self, other):
        self.__numerador = self.__numerador*other.__denominador - self.__denominador*other.__numerador
        self.__denominador = self.__denominador*other.__denominador
        self.simplificar()
        return self.getFraccion()
    
    def __mul__(self, other):
        self.__numerador = self.__numerador*other.__numerador
        self.__denominador = self.__denominador*other.__denominador
        self.simplificar()
        return self.getFraccion()
    
    def __truediv__(self, other):
        self.__numerador = self.__numerador*other.__denominador
        self.__denominador = self.__denominador*other.__numerador
        self.simplificar()
        return self.getFraccion()
        
    
    def simplificar(self):
        i = self.__numerador
        while i <= self.__numerador and i >= 2:
            if self.__numerador % i == 0 and self.__denominador % i == 0:
                self.__numerador = self.__numerador // i
                self.__denominador = self.__denominador // i
            i -= 1       