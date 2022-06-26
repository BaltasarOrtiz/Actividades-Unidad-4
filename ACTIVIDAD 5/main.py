from hashlib import new
from ObjectEncoder import ObjectEncoder
from vistaPaciente import PacienteView
from ManejadorPaciente import ManejadorPaciente 


if __name__=='__main__':
    conn = ObjectEncoder('pacientes.json') 
    vista = PacienteView()
    ManejadorPaciente = ManejadorPaciente(conn, vista)
    vista.setControlador(ManejadorPaciente)
    ManejadorPaciente.start()