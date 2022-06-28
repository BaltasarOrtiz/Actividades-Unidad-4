from ClaseProvincia import Provincia
from vistaWeather import NewProvincia
from ObjectEncoder import ObjectEncoder
import requests
API_KEY = "231fa16968ff3ff18230a2ffd246efe9"

class Manejador:
    __lista_provs : list
    __prov_actual : tuple
    __contr : ObjectEncoder


    def __init__(self, decodificador, vista):
        self.__contr = decodificador
        self.__lista_provs = self.__contr.decodificarDiccionario()
        self.vista = vista

    #obtengo los datos del clima de la api dada el nombre de la provincia
    def getDatosProv(self, prov_actual):
        try:
            response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?units=metric&q={prov_actual.getNombre()}&appid={API_KEY}')
            data = response.json()
            prov_actual.setTemperatura(data['main']['temp'])
            prov_actual.setHumedad(data['main']['humidity'])
            prov_actual.setFeelLike(data['main']['feels_like'])
        except:
            raise ValueError("No se pudo obtener los datos del clima")
        


    def seleccionarProv(self, index):
        self.__prov_actual = (index,self.__lista_provs[index])
        self.getDatosProv(self.__prov_actual[1])
        self.vista.verProvinciaEnForm(self.__prov_actual[1])


    #AGREGAR
    def agregarProvincia(self):
        nuevaProv = NewProvincia(self.vista).show()
        if nuevaProv:
            self.getDatosProv(nuevaProv)
            self.__lista_provs.append(nuevaProv)
            self.vista.agregarProvincia(nuevaProv)
            self.grabarDatos()
    
    #ELIMINAR
    def borrarProvincia(self):
        self.__lista_provs.pop(self.__prov_actual[0])
        self.vista.borrarProvincia(self.__prov_actual[0])
        self.grabarDatos()


    
    #JSON
    def grabarDatos(self):
        self.__contr.guardarJSONArchivo(self.toJSON())


    def toJSON(self):
        lista_aux = []
        for prov in self.__lista_provs:
            lista_aux.append(prov.toJSON())
        return lista_aux

    #INICIA APP
    def start(self):
        for c in self.__lista_provs:
            self.vista.agregarProvincia(c)
        self.vista.mainloop()