from hashlib import new
from ObjectEncoder import ObjectEncoder
from vistaPaciente import PacienteView
from ManejadorPaciente import ManejadorPaciente 


if __name__=='__main__':
    #conn - objeto de conexion al archivo json
    conn = ObjectEncoder('pacientes.json') 
    #vista - objeto de la clase PacienteView
    vista = PacienteView()
    #ManejadorPaciente objeto de la clase ManejadorPaciente
    ManejadorPaciente = ManejadorPaciente(conn, vista)
    #setControlador permite vincular la vista con el ManejadorPaciente
    vista.setControlador(ManejadorPaciente)
    #Iniciar aplicacion 
    ManejadorPaciente.start()