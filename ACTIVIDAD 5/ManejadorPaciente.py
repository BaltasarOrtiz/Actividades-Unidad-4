from hashlib import new
from ObjectEncoder import ObjectEncoder
from vistaPaciente import Newpaciente

class ManejadorPaciente:
    __conn: ObjectEncoder
    __paciente: list
    __pacienteActual: tuple
    

    def __init__(self, conn, vista):
        self.__conn = conn
        self.__paciente=self.__conn.decodificarDiccionario()
        self.vista = vista
        self.seleccion = -1
    

    def agregarPaciente(self):
        nuevoPaciente = Newpaciente(self.vista).show()
        if nuevoPaciente:
            self.__paciente.append(nuevoPaciente)
            self.vista.agregarpaciente(nuevoPaciente)


    def getListaPaciente(self):
        return self.__paciente

    def deletePaciente(self, paciente):
        indice=self.obtenerIndicePaciente(paciente)
        self.__paciente.pop(indice)

    def updatePaciente(self, paciente):
        indice=self.obtenerIndicePaciente(paciente)
        self.__paciente[indice]=paciente
        return self.__paciente[indice]

    def obtenerIndicePaciente(self, paciente):
        bandera = False
        i=0 
        while not bandera and i < len(self.__paciente):
            if self.__paciente[i] == self.__pacienteActual[1]:
                bandera=True
            else:
                i+=1
        return i
    
    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.toJSON())
    
    
    def toJSON(self):
        lista_aux = []
        for paciente in self.__paciente:
            lista_aux.append(paciente.toJSON())
        return lista_aux
    

    def start(self):
        for c in self.__paciente:
            self.vista.agregarpaciente(c)
        self.vista.mainloop()
    
    
    def seleccionarPaciente(self, index):
        self.__pacienteActual = (index,self.__paciente[index])
        self.vista.verpacienteEnForm(self.__pacienteActual[1])
    
    
    def modificarPaciente(self):
        print(self.__pacienteActual[0])
        paciente = self.__paciente[self.__pacienteActual[0]]
        detallesPaciente = self.vista.obtenerDetalles()
        paciente = self.updatePaciente(detallesPaciente)
        self.__paciente[self.__pacienteActual[0]] = paciente
        self.vista.modificarpaciente(paciente, self.__pacienteActual[0])
        self.grabarDatos()


    def borrarPaciente(self):
        paciente = self.__paciente[self.__pacienteActual[0]]
        self.deletePaciente(paciente)
        self.vista.borrarpaciente(self.__pacienteActual[0])
        self.grabarDatos()

    def calcularIMC(self):
        return self.__pacienteActual[1].calcularIMC()
