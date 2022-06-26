from tkinter import * #type: ignore
from tkinter import ttk, font


class Aplication:
    __ventana = None
    __altura = None
    __peso = None
    __IMC = None

    def __init__(self):
        self.__ventana = Tk()
        #self.__ventana.geometry("700x500")
        self.__ventana.title("Calculadora de IMC")
        self.__ventana.resizable(False, False)
        fuente = font.Font(weight="bold")


        #Ingreso de datos
        self.marco = ttk.Frame(self.__ventana, borderwidth=2, relief="raised", padding=(10, 10))
        #textos
        self.alturaLbl = ttk.Label(self.marco, text="Altura", font=fuente, padding=(5, 5))
        self.pesoLbl = ttk.Label(self.marco, text="Peso", font=fuente, padding=(5, 5))

        #variables
        self.__altura = DoubleVar(value=0.0)
        self.__peso = DoubleVar(value=0.0)
        self.__IMC = DoubleVar() #float
        self.__mensaje = StringVar()
        
        #estilo de entradas
        e = ttk.Style()
        e.configure("TEntry", background="red")
        #entradas
        self.alturaEntry = ttk.Entry(self.marco, width=45, textvariable=self.__altura)
        self.pesoEntry = ttk.Entry(self.marco, width=45, textvariable=self.__peso)

        #estilo de botones
        s = ttk.Style()
        s.configure("TButton", font=fuente, foreground='red', background = 'orange')
        #botones 
        self.separ1 = ttk.Separator(self.marco, orient=HORIZONTAL)
        self.boton1 = ttk.Button(self.marco, text="Calcular", command=self.calcular, width=20)
        self.boton2 = ttk.Button(self.marco, text="Limpiar", command=self.limpiar, width=20)
        self.boton3 = ttk.Button(self.marco, text="Cerrar", command=self.__ventana.destroy)
        #salida del IMC
        ttk.Label(self.marco, textvariable=self.__IMC, font=fuente, foreground='blue').grid(column=1, row=5)
        ttk.Label(self.marco, textvariable=self.__mensaje, font=fuente, foreground='blue').grid(column=1, row=6)

        #grid
        self.marco.grid(column=0, row=0, padx=5, pady=5)
        self.alturaLbl.grid(column=0, row=0)
        self.alturaEntry.grid(column=1, row=0)

        self.pesoLbl.grid(column=0, row=1)
        self.pesoEntry.grid(column=1, row=1)

        self.separ1.grid(column=0, row=2, columnspan=3, pady=20, sticky=EW)
        self.boton1.grid(column=0, row=3, padx=20, sticky=E) #CALCULAR
        self.boton2.grid(column=2, row=3, padx=20, sticky=W) #LIMPIAR
        self.boton3.grid(column=1, row=4, padx=20, pady=10, sticky=S+E+W+N) #CERRAR

        #importante
        self.alturaEntry.focus_set()
        self.__ventana.mainloop()

    
    def calcular(self):
        peso = float(self.pesoEntry.get())
        altura = float(self.alturaEntry.get())
        IMC = peso / altura**2
        self.__IMC.set("Tu índice de masa corporal es: {:.1f} Kg/m^2".format(IMC)) #type: ignore
        if IMC < 18.5:
            self.__mensaje.set("Peso inferior al normal")
        elif IMC >= 18.5 and IMC < 25:
            self.__mensaje.set("Peso normal")
        elif IMC >= 25 and IMC < 30:
            self.__mensaje.set("Peso superior al normal")
        else:
            self.__mensaje.set("Obesidad")
        
    
    def limpiar(self):
        self.pesoEntry.delete(0, END)
        self.alturaEntry.delete(0, END)
        self.__IMC.set("") #type: ignore
        self.__mensaje.set("")


if __name__ == "__main__":
    app = Aplication()
