from ClaseProvincia import Provincia
from vistaWeather import NewWeather
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
    
    def getDatosProv(self, prov_actual):
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?units=metric&q={prov_actual.getNombre()}&appid={API_KEY}')
        data = response.json()
        prov_actual.setTemperatura(data['main']['temp'])
        prov_actual.setHumedad(data['main']['humidity'])
        prov_actual.setFeelLike(data['main']['feels_like'])

    def seleccionarProv(self, index):
        self.__prov_actual = (index,self.__lista_provs[index])
        self.getDatosProv(self.__prov_actual[1])
        self.vista.verWeatherEnForm(self.__prov_actual[1])

    
    #AGREGAR
    def agregarProvincia(self):
        nuevaProv = NewWeather(self.vista).show()
        if nuevaProv:
            self.getDatosProv(nuevaProv)
            self.__lista_provs.append(nuevaProv)
            self.vista.agregarWeather(nuevaProv)
            self.grabarDatos()

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
            self.vista.agregarWeather(c)
        self.vista.mainloop()