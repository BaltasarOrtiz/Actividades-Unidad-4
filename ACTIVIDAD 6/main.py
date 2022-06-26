from ManejadorWeather import Manejador
from vistaWeather import WeatherView
from ObjectEncoder import ObjectEncoder


if __name__ == "__main__":
    conn = ObjectEncoder('datosweather.json') 
    vista = WeatherView()
    ManejadorClima = Manejador(conn, vista)
    vista.setControlador(ManejadorClima)
    ManejadorClima.start()