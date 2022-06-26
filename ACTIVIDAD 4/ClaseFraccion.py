class Fraccion:
    __numerador = 0
    __denominador = 0

    def __init__(self, numerador, denominador):
        self.__numerador = numerador 
        self.__denominador = denominador

    def getFraccion(self):
        return (self.__numerador,"/",self.__numerador)

    def __add__(self, other):
        self.__numerador = self.__numerador*other.__denominador + self.__denominador*other.__numerador
        self.__denominador =  self.__denominador*other.__denominador
        return self.getFraccion()

    def __sub__(self, other):
        self.__numerador = self.__numerador*other.__denominador - self.__denominador*other.__numerador
        self.__denominador = self.__denominador*other.__denominador
        return self.getFraccion()
    
    def __mul__(self, other):
        self.__numerador = self.__numerador*other.__numerador
        self.__denominador = self.__denominador*other.__denominador
        return self.getFraccion()
    
    def __truediv__(self, other):
        self.__numerador = self.__numerador*other.__denominador
        self.__denominador = self.__denominador*other.__numerador
        return self.getFraccion()
    
    def simplificar(self):
        for i in range(2, self.__numerador):
            if self.__numerador % i == 0 and self.__denominador % i == 0:
                self.__numerador = self.__numerador // i
                self.__denominador = self.__denominador // i
        return self.getFraccion()
    