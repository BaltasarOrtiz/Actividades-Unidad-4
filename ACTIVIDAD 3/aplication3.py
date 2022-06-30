from email.errors import HeaderParseError
from tkinter import *  #type: ignore
from tkinter import ttk, font
import tkinter as tk
import requests

#Obtenemos informacion de la API
url = 'https://www.dolarsi.com/api/api.php?type=dolar'
res = requests.get(url)
data = res.json()
Banco = data[0]
valor = Banco['casa']['venta'].replace(',', '.')


class Aplication():
    __ventana : Tk
    __dolares : StringVar  
    __pesos : StringVar

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title("Conversor de dolar a pesos")
        self.__ventana.resizable(False, False)
        fuente = font.Font(weight="bold")
        
        #Frame Principal
        self.marco = ttk.Frame(self.__ventana, borderwidth=2, relief="raised", padding=(10, 10))

        #Textos 
        self.text1 = ttk.Label(self.marco, text="Dolares", font=fuente, padding=(5, 5))
        self.text2 = ttk.Label(self.marco, text="Pesos", font=fuente, padding=(5, 5))
        
        #Variables
        self.__dolares = StringVar()
        self.__dolares.trace("w", self.convertir)
        self.__pesos = StringVar()
        
        #Entradas  
        self.entry1 = ttk.Entry(self.marco, textvariable=self.__dolares, width = 15)
        self.label = ttk.Label(self.marco, textvariable=self.__pesos, width=15)
        
        #Botones
        self.boton2 = ttk.Button(self.marco, text="Salir", command=self.__ventana.destroy)
        
        #Grids
        self.marco.grid(column=0, row=0, padx=5, pady=5)
        self.text1.grid(column=0, row=0, padx=5, pady=5)
        self.entry1.grid(column=1, row=0, padx=5, pady=5)
        self.text2.grid(column=0, row=1, padx=5, pady=5)
        self.label.grid(column=1, row=1, padx=5, pady=5)
        self.boton2.grid(column=2, row=2, padx=5, pady=5)

        #Importante para que se vea la ventana
        self.__ventana.mainloop()
    
    #Funcion para convertir
    def convertir(self, *args):
        if self.entry1.get() == "":
            self.__pesos.set("") #type: ignore
        else:
            total = float(float(self.__dolares.get()) * float(valor))
            self.__pesos.set(round(total, 2))

if __name__ == "__main__":
    app = Aplication()