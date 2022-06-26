import tkinter as tk
from tkinter import messagebox
from ClaseProvincia import Provincia


class WeatherList(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        
    def insertar(self, weather, index=tk.END):
        text = "{}".format(weather.getNombre())
        self.lb.insert(index, text)
    
    def borrar(self, index):
        self.lb.delete(index, index)

    def modificar(self, weather, index):
        self.borrar(index)
        self.insertar(weather, index)


    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)

class WeatherForm(tk.LabelFrame):
    fields = ("Nombre", "Capital", "Cantidad de Habitantes", "Cantidad de departamentos/partidos","Temperatura","Sensacion Termica", "Humedad")
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Provincia", padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()

    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry

    def mostrarEstadoWeatherEnFormulario(self, weather):
        # a partir de un weather, obtiene el estado
        # y establece en los valores en el formulario de entrada
        values = (weather.getNombre(), weather.getCapital(), weather.getCantidadHabitantes(), weather.getCantidadDepartamentos() ,weather.getTemperatura(), weather.getHumedad(),weather.getFeelLike())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)
    
    def crearWeatherDesdeFormulario(self):
        #obtiene los valores de los campos del formulario
        #para crear un nuevo weather
        values = [e.get() for e in self.entries]
        weather=None
        try:
            weather = Provincia(*values)
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e), parent=self)
        self.limpiar()
        return weather
    

    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)


class WeatherCreateForm(tk.LabelFrame):
    fields = ("Nombre", "Capital", "Cantidad de Habitantes", "Cantidad de departamentos/partidos")
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Provincia", padx=10, pady=10, **kwargs)
        self.frame2 = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame2.pack()

    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame2, text=text)
        entry = tk.Entry(self.frame2, width=25)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry

    def crearWeatherDesdeFormulario(self):
        #obtiene los valores de los campos del formulario
        #para crear un nuevo weather
        values = [e.get() for e in self.entries]
        weather=None
        try:
            weather = Provincia(*values)
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e), parent=self)
        self.limpiar()
        return weather
    
    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)



class NewWeather(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.Weather = None
        self.form = WeatherCreateForm(self)
        self.btn_add = tk.Button(self, text="Confirmar", command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)

    def confirmar(self):
        self.Weather = self.form.crearWeatherDesdeFormulario()
        if self.Weather:
            messagebox.showinfo("AVISO", str("Provincia añadida correctamente") ,parent=self)
            self.destroy()

    def show(self):
        self.grab_set()
        self.wait_window()
        return self.Weather


class UpdateWeatherForm(WeatherForm):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
    


class WeatherView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Weathers")
        self.list = WeatherList(self, height=15)
        self.form = UpdateWeatherForm(self)
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
    
        self.btn_new = tk.Button(self, text="Agregar Provincia")
        self.btn_new.pack(side=tk.BOTTOM, pady=5)
    
    def setControlador(self, ctrl):
        #vincula la vista con el controlador
        self.ctrl = ctrl
        self.btn_new.config(command=self.ctrl.agregarProvincia)
        self.list.bind_doble_click(self.ctrl.seleccionarProv)
    
    def agregarWeather(self, Weather):
        self.list.insertar(Weather)

    def modificarWeather(self, Weather, index):
        self.list.modificar(Weather, index)

    def borrarWeather(self, index):
        self.form.limpiar()
        self.list.borrar(index)
    
    def obtenerDetalles(self):
        return self.form.crearWeatherDesdeFormulario()
    
    def verWeatherEnForm(self, Weather):
        self.form.mostrarEstadoWeatherEnFormulario(Weather)
