from ObjectEncoder import ObjectEncoder
from vistaPaciente import Newpaciente

class ManejadorPaciente:
    __conn: ObjectEncoder
    __paciente: list
    __pacienteActual: tuple
    
    #Constructor de la clase que recibe el objetoEncoder y el objetoVista
    def __init__(self, conn, vista):
        self.__conn = conn
        self.__paciente=self.__conn.decodificarDiccionario()
        self.vista = vista
    
    #Metodo que agrega pacientes a la lista
    def agregarPaciente(self):
        nuevoPaciente = Newpaciente(self.vista).show()
        if nuevoPaciente:
            self.__paciente.append(nuevoPaciente)
            self.vista.agregarpaciente(nuevoPaciente) #Envia el paciente nuevo a la vista de la interfaz
    
    #Metodo que graba los datos en el archivo json
    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.toJSON())
    
    def toJSON(self):
        lista_aux = []
        for paciente in self.__paciente:
            lista_aux.append(paciente.toJSON())
        return lista_aux
    #---------------------------------------------------------------------------------------------------------------------
    
    #Metodo que obtiene el paciente actual (Utilizando una tupla)
    def seleccionarPaciente(self, index):
        self.__pacienteActual = (index,self.__paciente[index])
        self.vista.verpacienteEnForm(self.__pacienteActual[1])
    
    #Metodo para modificar el paciente actual
    def modificarPaciente(self):
        detallesPaciente = self.vista.obtenerDetalles()
        self.__paciente[self.__pacienteActual[0]] = detallesPaciente
        self.vista.modificarpaciente(detallesPaciente, self.__pacienteActual[0])
        self.grabarDatos()

    #Metodo que elimina el paciente seleccionado
    def borrarPaciente(self):
        self.__paciente.pop(self.__pacienteActual[0])
        self.vista.borrarpaciente(self.__pacienteActual[0])
        self.grabarDatos()
        
    
    #Metodo que calcula el IMC del paciente seleccionado
    def calcularIMC(self):
        imc = self.__pacienteActual[1].calcularIMC()
        self.vista.mostrarIMC(imc)

    #Iniciar Aplicacion
    def start(self):
        for c in self.__paciente:
            self.vista.agregarpaciente(c)
        self.vista.mainloop()