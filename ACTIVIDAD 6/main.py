from ManejadorWeather import Manejador
from vistaWeather import ProvinciaView
from ObjectEncoder import ObjectEncoder


if __name__ == "__main__":
    conn = ObjectEncoder('datosweather.json') 
    vista = ProvinciaView()
    ManejadorClima = Manejador(conn, vista)
    vista.setControlador(ManejadorClima)
    ManejadorClima.start()