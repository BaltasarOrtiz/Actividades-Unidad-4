from email.errors import HeaderParseError
from tkinter import *  #type: ignore
from tkinter import ttk, font
import tkinter as tk


class Aplication:
    __ventana = None
    __precio = None
    __valorCheck = None
    __total = None
    __IVA = None


    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title("Calculadora IVA")
        self.__ventana.resizable(False, False)
        fuente = font.Font(weight="bold")
        
        #Frame Principal
        self.marco = ttk.Frame(self.__ventana, borderwidth=2, relief="raised", padding=(10, 10))

        #Textos
        self.text1 = ttk.Label(self.marco, text="Precio sin IVA", font=fuente, padding=(5, 5))
        #texto de salida de calculo
        self.text4 = ttk.Label(self.marco, text="IVA", font=fuente, padding=(5, 5))
        self.text5 = ttk.Label(self.marco, text="Precio con IVA", font=fuente, padding=(5, 5))
        
        #Variables
        self.__precio = DoubleVar()
        self.__IVA = StringVar()
        self.__total = StringVar()

        #Entradas
        self.entry1 = ttk.Entry(self.marco, textvariable=self.__precio)
        self.entry2 = ttk.Entry(self.marco, textvariable=self.__IVA,  width=15)
        self.entry3 = ttk.Entry(self.marco, textvariable=self.__total, width=15)
        self.entry2.config(state=tk.DISABLED)
        self.entry3.config(state=tk.DISABLED)
        
        #Checks de IVA
        self.__valorCheck = IntVar()
        self.check1 = ttk.Radiobutton(self.marco, text="IVA 21%", value = 0, variable=self.__valorCheck)
        self.check2 = ttk.Radiobutton(self.marco, text="IVA 10.5%", value = 1, variable=self.__valorCheck)
        
        

        #Botones
        self.boton1 = ttk.Button(self.marco, text="Calcular", command = self.calcular, width=20)
        self.boton2 = ttk.Button(self.marco, text="Salir", command=self.__ventana.destroy)

        #Grids
        self.marco.grid(column=0, row=0, padx=5, pady=5)
        self.text1.grid(column=0, row=0, padx=5, pady=5)
        self.entry1.grid(column=1, row=0, padx=5, pady=5)
        #grid check
        self.check1.grid(column=0, row=1, padx=5, pady=5)
        self.check2.grid(column=0, row=2, padx=5, pady=5)
        
        #Grids de textos de Salida
        self.text4.grid(column=0, row=3, padx=5, pady=5)
        self.text5.grid(column=0, row=5, padx=5, pady=5)
        self.entry2.grid(column=1, row=3, padx=10, pady=10)
        self.entry3.grid(column=1, row=5, padx=10, pady=10)

        #Grids de Botones
        self.boton1.grid(column=0, row=6, padx=5, pady=5)
        self.boton2.grid(column=1, row=6, padx=5, pady=5)


        #Importante para que se vea la ventana
        self.__ventana.mainloop()
    
    #Funcion que calcula el IVA
    def calcular(self):
        self.entry2.config(state=tk.NORMAL)
        self.entry3.config(state=tk.NORMAL)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        if self.__valorCheck.get() == 0: #type: ignore
            self.__IVA = float(self.__precio.get()* 0.21) #type: ignore
            self.__total = float(self.__precio.get()) + self.__IVA #type: ignore
            self.entry2.insert(0, str(round(self.__IVA, 2)))
            self.entry2.config(state="readonly")
        else:
            self.__IVA = float((self.__precio.get()) * 0.105) #type: ignore
            self.__total = float(self.__precio.get()) + self.__IVA #type: ignore
            self.entry2.insert(0, str(round(self.__IVA, 2)))
            self.entry2.config(state="readonly")
        self.entry3.insert(0, str(round(self.__total, 2)))
        self.entry3.config(state="readonly")


if __name__ == "__main__":
    app = Aplication()