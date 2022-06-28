import tkinter as tk
from tkinter import messagebox
from unittest import expectedFailure
from ClaseProvincia import Provincia


class ProvinciaList(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insertar(self, provincia, index=tk.END):
        text = "{}".format(provincia.getNombre())
        self.lb.insert(index, text)
    
    def borrar(self, index):
        self.lb.delete(index, index)
        
    def modificar(self, provincia, index):
        self.borrar(index)
        self.insertar(provincia, index)

    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)


class ProvinciaForm(tk.LabelFrame):
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

    def mostrarEstadoProvinciaEnFormulario(self, provincia):
        # a partir de un provincia, obtiene el estado
        # y establece en los valores en el formulario de entrada
        values = (provincia.getNombre(), provincia.getCapital(), provincia.getCantidadHabitantes(), provincia.getCantidadDepartamentos() ,provincia.getTemperatura(), provincia.getFeelLike(), provincia.getHumedad())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

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
    

    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

class ProvinciaCreateForm(tk.LabelFrame):
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

    def crearProvinciaDesdeFormulario(self):
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

class NewProvincia(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.Weather = None
        self.form = ProvinciaCreateForm(self)
        self.btn_add = tk.Button(self, text="Confirmar", command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)

    def confirmar(self):
        self.Provincia = self.form.crearProvinciaDesdeFormulario()
        if self.Provincia:
            messagebox.showinfo("AVISO", str("Provincia añadida correctamente") ,parent=self)
            self.destroy()

    def show(self):
        self.grab_set()
        self.wait_window()
        return self.Provincia


class UpdateProvinciaForm(ProvinciaForm):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)



class ProvinciaView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Weathers")
        self.list = ProvinciaList(self, height=15)
        self.form = UpdateProvinciaForm(self)
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
        self.list.bind_doble_click(self.ctrl.seleccionarProv)
        
        self.btn_new2.config(command=self.ctrl.borrarProvincia)
        self.btn_new2.config(state=tk.DISABLED)

    def agregarProvincia(self, Weather):
        self.list.insertar(Weather)

    def modificarProvincia(self, Weather, index):
        self.list.modificar(Weather, index)

    def borrarProvincia(self, index):
        self.form.limpiar()
        self.list.borrar(index)
        self.btn_new2.config(state=tk.DISABLED)
        messagebox.showinfo("AVISO", str("Provincia eliminada correctamente") ,parent=self)

    def obtenerDetalles(self):
        return self.form.crearProvinciaDesdeFormulario()

    def verProvinciaEnForm(self, Weather):
        self.btn_new2.config(state=tk.NORMAL)
        self.form.mostrarEstadoProvinciaEnFormulario(Weather)
        