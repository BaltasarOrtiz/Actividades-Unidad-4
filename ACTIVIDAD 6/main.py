from ManejadorWeather import Manejador
from vistaWeather import ProvinciaView
from ObjectEncoder import ObjectEncoder


if __name__ == "__main__":
    #conn - objeto de conexion al archivo json
    conn = ObjectEncoder('datosweather.json') 
    #vista - objeto de la clase ProvinciaView
    vista = ProvinciaView()
    #manejador - objeto de la clase Manejador
    ManejadorClima = Manejador(conn, vista)
    #setControlador permite vincular la vista con el Manejador
    vista.setControlador(ManejadorClima)
    #Iniciar Aplicacion
    ManejadorClima.start()