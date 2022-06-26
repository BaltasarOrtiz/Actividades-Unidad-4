from email.errors import HeaderParseError
from tkinter import *  #type: ignore
from tkinter import ttk, font
import tkinter as tk
import requests

url = 'https://www.dolarsi.com/api/api.php?type=dolar'
res = requests.get(url)
data = res.json()
Banco = data[0]
casa1 = Banco['casa']
valor = casa1["venta"].replace(',', '.')

class Aplication():
    __ventana = None
    __dolares = None
    __pesos = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title("Conversor de dolar a pesos")
        self.__ventana.resizable(False, False)
        fuente = font.Font(weight="bold")
        
        #frame principal
        self.marco = ttk.Frame(self.__ventana, borderwidth=2, relief="raised", padding=(10, 10))

        #labels
        self.text1 = ttk.Label(self.marco, text="Dolares", font=fuente, padding=(5, 5))
        self.text2 = ttk.Label(self.marco, text="Pesos", font=fuente, padding=(5, 5))
        
        #variables
        self.__dolares = DoubleVar()
        self.__pesos = DoubleVar()
        
        #entry
        self.entry1 = ttk.Entry(self.marco, textvariable=self.__dolares, width = 15)
        self.entry2 = ttk.Entry(self.marco, textvariable=self.__pesos, width=15)
        self.entry2.config(state=tk.DISABLED)
        
        #buttons
        self.boton1 = ttk.Button(self.marco, text="Convertir", command = self.convertir, width=20)
        self.boton2 = ttk.Button(self.marco, text="Salir", command=self.__ventana.destroy)
        
        #grid
        self.marco.grid(column=0, row=0, padx=5, pady=5)
        self.text1.grid(column=0, row=0, padx=5, pady=5)
        self.entry1.grid(column=1, row=0, padx=5, pady=5)
        self.text2.grid(column=0, row=1, padx=5, pady=5)
        self.entry2.grid(column=1, row=1, padx=5, pady=5)
        self.boton1.grid(column=0, row=2, padx=5, pady=5, columnspan=2)
        self.boton2.grid(column=2, row=2, padx=5, pady=5)


        #no tocar
        self.__ventana.mainloop()
        
    
    def convertir(self):
        self.entry2.config(state=tk.NORMAL)
        self.entry2.delete(0, END)
        self.__pesos = float(self.__dolares.get() * float(valor)) #type: ignore
        self.entry2.insert(10, str(round(self.__pesos, 2)))
        self.entry2.config(state="readonly")
        

    

if __name__ == "__main__":
    app = Aplication()