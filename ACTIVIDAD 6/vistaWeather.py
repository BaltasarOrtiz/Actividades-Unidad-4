import tkinter as tk
from tkinter import messagebox
from ClaseProvincia import Provincia

#----------------------------------------------------------------------------------------------------------------------
#Clase que muestra el listado de provincias
class ProvinciaList(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    #Funcion para insertar una provincia en la listbox
    def insertar(self, provincia, index=tk.END):
        text = "{}".format(provincia.getNombre())
        self.lb.insert(index, text)
    
    #Funcion para borrar una provincia de la listbox
    def borrar(self, index):
        self.lb.delete(index, index)
    
    #Al accionar doble click sobre una provincia, se muestra en el formulario
    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)

#----------------------------------------------------------------------------------------------------------------------
#Clase que genera el formulario de una provincia
class ProvinciaForm(tk.LabelFrame):
    fields = ("Nombre", "Capital", "Cantidad de Habitantes", "Cantidad de departamentos/partidos","Temperatura","Sensacion Termica", "Humedad")
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Provincia", padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()

    #Define los campos del formulario para luego mostrar los datos de la provincia
    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry

    #Muestra los datos de la provincia en el formulario
    def mostrarEstadoProvinciaEnFormulario(self, provincia):
        # a partir de un provincia, obtiene el estado
        # y establece en los valores en el formulario de entrada
        values = (provincia.getNombre(), provincia.getCapital(), provincia.getCantidadHabitantes(), provincia.getCantidadDepartamentos() ,provincia.getTemperatura(), provincia.getFeelLike(), provincia.getHumedad())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

    #Funcion para obtener los datos del formulario
    def crearProvinciaDesdeFormulario(self):
        #obtiene los valores de los campos del formulario
        #para crear un nuevo provincia
        values = [e.get() for e in self.entries]
        prov=None
        try:
            prov = Provincia(*values)
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e), parent=self)
        self.limpiar()
        return prov
    
    #Funcion para limpiar los campos del formulario
    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

#----------------------------------------------------------------------------------------------------------------------
#Clase para crear una provincia
class ProvinciaCreateForm(tk.LabelFrame):
    fields = ("Nombre", "Capital", "Cantidad de Habitantes", "Cantidad de departamentos/partidos")
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Provincia", padx=10, pady=10, **kwargs)
        self.frame2 = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame2.pack()

    #Defino los campos del formulario para luego mostrar los datos de la provincia
    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame2, text=text)
        entry = tk.Entry(self.frame2, width=25)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry

    #obtiene los valores de los campos del formulario para crear una nueva provincia
    def crearProvinciaDesdeFormulario(self):
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

#----------------------------------------------------------------------------------------------------------------------

#Clase para confirmar la creacion de una provincia en una nueva ventana emergente
class NewProvincia(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.Weather = None
        self.form = ProvinciaCreateForm(self)
        self.btn_add = tk.Button(self, text="Confirmar", command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)

    #Funcion para confirmar la creacion de una provincia
    def confirmar(self):
        self.Provincia = self.form.crearProvinciaDesdeFormulario()
        if self.Provincia:
            messagebox.showinfo("AVISO", str("Provincia añadida correctamente") ,parent=self)
            self.destroy()
    #Funcion para obtener la provincia creada
    def show(self):
        self.grab_set()#Ventana emergente que permite interactuar con ella sin actuar sobre la principal
        self.wait_window()
        return self.Provincia

#----------------------------------------------------------------------------------------------------------------------
#Clase - Vista general de provincias
class ProvinciaView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Weathers")
        self.list = ProvinciaList(self, height=15)
        self.form = ProvinciaForm(self)
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)

        self.btn_new = tk.Button(self, text="Agregar Provincia")
        self.btn_new.pack(side=tk.BOTTOM, pady=5)

        self.btn_new2 = tk.Button(self, text="Eliminar Provincia")
        self.btn_new2.pack(side=tk.BOTTOM, pady=5)
    
    def setControlador(self, ctrl):
        #vincula la vista con el controlador
        self.ctrl = ctrl
        self.btn_new.config(command=self.ctrl.agregarProvincia)
        #Se asigna el callback
        self.list.bind_doble_click(self.ctrl.seleccionarProv)
        self.btn_new2.config(command=self.ctrl.borrarProvincia)
        self.btn_new2.config(state=tk.DISABLED)

    #Funcion para agregar una provincia a la lista de la interfaz
    def agregarProvincia(self, Weather):
        self.list.insertar(Weather)
    
    #Funcion para eliminar una provincia de la lista de la interfaz
    def borrarProvincia(self, index):
        self.form.limpiar()
        self.list.borrar(index)
        self.btn_new2.config(state=tk.DISABLED)
        messagebox.showinfo("AVISO", str("Provincia eliminada correctamente") ,parent=self)

    #Funcion para ver una provincia de la lista de la interfaz
    def verProvinciaEnForm(self, Weather):
        self.btn_new2.config(state=tk.NORMAL)
        self.form.mostrarEstadoProvinciaEnFormulario(Weather)

#----------------------------------------------------------------------------------------------------------------------