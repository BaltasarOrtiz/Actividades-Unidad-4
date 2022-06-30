import tkinter as tk
from tkinter import messagebox
from ClasePaciente import Paciente 

#----------------------------------------------------------------------------------------------------------------------

# Clase - Listado de Pacientes
class PacienteList(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        # Genera Listbox de Pacientes
        self.lb = tk.Listbox(self, **kwargs)
        #Scrollbar de la Listbox
        scroll = tk.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        #Packs para Listbox y Scrollbar
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    
    #Funcion para insertar paciente en la listbox
    def insertar(self, paciente, index=tk.END):
        text = "{}, {}".format(paciente.getApellido(), paciente.getNombre())
        self.lb.insert(index, text)

    #Funcion para borrar un paciente en la listbox
    def borrar(self, index):
        messagebox.showinfo("Paciente borrado", "Paciente Borrado Correctamente")
        self.lb.delete(index, index)

    #Funcion para modificar o actualizar un paciente de la listbox
    def modificar(self, paciente, index):
        self.lb.delete(index, index)
        self.insertar(paciente, index)

    #Al accionar doble click sobre un paciente, se muestra en el formulario
    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)

#----------------------------------------------------------------------------------------------------------------------

#Clase - Formulario del Paciente
class PacienteForm(tk.LabelFrame):
    fields = ("Apellido", "Nombre", "Email", "Teléfono","Altura","Peso")
    def __init__(self, master, **kwargs):
        super().__init__(master, text="paciente", padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        #Se crean los campos con los valores asignados en el fields
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()

    #Define los campos del formulario para luego mostrar los datos del paciente
    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry

    #Funcion para mostrar un paciente en el formulario
    def mostrarEstadopacienteEnFormulario(self, paciente):
        # a partir de un paciente, obtiene el estado
        # y establece en los valores en el formulario de entrada
        values = (paciente.getApellido(), paciente.getNombre(),paciente.getEmail(), paciente.getTel(), paciente.getAltura(), paciente.getPeso())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

    #Funcion que obtiene los valores de la entrada para crear un paciente en el formulario
    def crearpacienteDesdeFormulario(self):
        #obtiene los valores de los campos del formulario
        #para crear un nuevo paciente
        values = [e.get() for e in self.entries]
        paciente=None
        try:
            paciente = Paciente(*values)
            messagebox.showinfo("AVISO", str("Paciente guardado correctamente") ,parent=self)
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e), parent=self)
        self.limpiar()
        return paciente
    
    #Funcion que muestra el IMC de un paciente   
    def verIMC(self, imc):
        messagebox.showinfo("IMC", imc ,parent=self)

    #Funcion para limpiar las entradas
    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

#----------------------------------------------------------------------------------------------------------------------

#Clase - Para crear un nuevo paciente y mostrarlo en la interfaz

class Newpaciente(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.paciente = None
        #Crea el formulario y da acceso al mismo a traves de self.form
        self.form = PacienteForm(self)
        self.btn_add = tk.Button(self, text="Confirmar", command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)

    #Funcion para confirmar la creacion del nuevo paciente en la nueva ventana
    def confirmar(self):
        self.paciente = self.form.crearpacienteDesdeFormulario()
        if self.paciente:
            self.destroy()
    
    #Funcion para retornar el paciente creado
    def show(self):
        #Ventana emergente que permite interactuar con ella sin actuar sobre la principal
        self.grab_set()
        self.wait_window()
        return self.paciente


class UpdatePacienteForm(PacienteForm):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.btn_save = tk.Button(self, text="Guardar")
        self.btn_delete = tk.Button(self, text="Borrar")
        self.btn_IMC = tk.Button(self, text="IMC")
        self.btn_save.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.btn_delete.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.btn_IMC.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
    
    #Callback para guardar un paciente y actualizarlo en la listbox
    def bind_save(self, callback):
        self.btn_save.config(command=callback)
    
    #Callback para borrar un paciente de la listbox
    def bind_delete(self, callback):
        self.btn_delete.config(command=callback)

    #Callback para calcular el IMC de un paciente seleccionado en la listbox
    def bind_IMC(self, callback):
        self.btn_IMC.config(command=callback)

#----------------------------------------------------------------------------------------------------------------------

#Clase - Vista general de pacientes

class PacienteView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de pacientes")
        #Self.list es el objeto que genera el listado de pacientes
        self.list = PacienteList(self, height=15) #define el largo del listbox
        #Self.form es el objeto que controla los callbacks de los botones
        self.form = UpdatePacienteForm(self) #callbacks
        self.btn_new = tk.Button(self, text="Agregar paciente")
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)
    
    def setControlador(self, ctrl):
        self.ctrl = ctrl #Se vincula la vista con el controlador
        self.btn_new.config(command=self.ctrl.agregarPaciente)
        #Se asigna el callback para la seleccion de un paciente
        self.list.bind_doble_click(self.ctrl.seleccionarPaciente)
        #Se asignan los callbacks de las funciones en el UpdatePacienteForm
        self.form.bind_save(self.ctrl.modificarPaciente)
        self.form.bind_delete(self.ctrl.borrarPaciente)
        self.form.bind_IMC(self.ctrl.calcularIMC)
    
    #Agrega un paciente a la lista de la interfaz
    def agregarpaciente(self, paciente):
        self.list.insertar(paciente)
    
    #Actualiza un paciente en la lista de la interfaz
    def modificarpaciente(self, paciente, index):
        self.list.modificar(paciente, index)
    
    #Borra un paciente de la lista de la interfaz
    def borrarpaciente(self, index):
        self.form.limpiar()
        self.list.borrar(index)
    
    #Obtiene el paciente seleccionado en la lista de la interfaz
    def obtenerDetalles(self):
        return self.form.crearpacienteDesdeFormulario()
    
    #Muestra un paciente en el formulario de la interfaz
    def verpacienteEnForm(self, paciente):
        self.form.mostrarEstadopacienteEnFormulario(paciente)
    
    #Muestra el IMC de un paciente en la interfaz
    def mostrarIMC(self, imc):
        self.form.verIMC(imc)
#----------------------------------------------------------------------------------------------------------------------