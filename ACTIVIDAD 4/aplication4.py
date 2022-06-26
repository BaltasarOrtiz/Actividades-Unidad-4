from tkinter import *
from tkinter import ttk
from functools import partial
from ClaseFraccion import Fraccion


class Calculadora(object):
    __ventana=None
    __operador=None
    __panel=None
    __operadorAux=None
    __primerOperando1=None
    __segundoOperando1=None
    __primerOperando2=None
    __segundoOperando2=None


    def __init__(self):
        
        self.__ventana = Tk()
        self.__ventana.title('Tk-Calculadora')
        mainframe = ttk.Frame(self.__ventana, padding="3 10 3 10")
        mainframe.grid(column=0, row=0, sticky=N+W+E+S)
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'

        #Variables
        self.__panel = StringVar()
        self.__operador = StringVar()
        #operandos
        self.__primerOperando1=StringVar()
        self.__primerOperando2=StringVar()
        self.__segundoOperando1=StringVar()
        self.__segundoOperando2=StringVar()
        #auxiliar
        self.__operadorAux=None

        #botones
        operatorEntry=ttk.Entry(mainframe, width=10, textvariable=self.__operador, justify='center', state='disabled')
        operatorEntry.grid(column=1, row=1, columnspan=1, sticky=EW)
        panelEntry = ttk.Entry(mainframe, width=20, textvariable=self.__panel, justify='right',state='disabled')
        panelEntry.grid(column=2, row=1, columnspan=2, sticky=EW)
        ttk.Button(mainframe, text='1', command=partial(self.ponerNUMERO, '1')).grid(column=1, row=3, sticky=W, padx=5, pady=5)
        ttk.Button(mainframe, text='2', command=partial(self.ponerNUMERO,'2')).grid(column=2, row=3, sticky=W, padx=5, pady=5)
        ttk.Button(mainframe, text='3', command=partial(self.ponerNUMERO,'3')).grid(column=3, row=3, sticky=W, padx=5, pady=5)
        ttk.Button(mainframe, text='4', command=partial(self.ponerNUMERO,'4')).grid(column=1, row=4, sticky=W, padx=5, pady=5)
        ttk.Button(mainframe, text='5', command=partial(self.ponerNUMERO,'5')).grid(column=2, row=4, sticky=W, padx=5, pady=5)
        ttk.Button(mainframe, text='6', command=partial(self.ponerNUMERO,'6')).grid(column=3, row=4, sticky=W, padx=5, pady=5)
        ttk.Button(mainframe, text='7', command=partial(self.ponerNUMERO,'7')).grid(column=1, row=5, sticky=W, padx=5, pady=5)
        ttk.Button(mainframe, text='8', command=partial(self.ponerNUMERO,'8')).grid(column=2, row=5, sticky=W, padx=5, pady=5)
        ttk.Button(mainframe, text='9', command=partial(self.ponerNUMERO,'9')).grid(column=3, row=5, sticky=W, padx=5, pady=5)
        ttk.Button(mainframe, text='0', command=partial(self.ponerNUMERO, '0')).grid(column=1, row=6, sticky=W, padx=5, pady=5)
        ttk.Button(mainframe, text='+', command=partial(self.ponerOPERADOR, '+')).grid(column=2, row=6, sticky=W, padx=5, pady=5)
        ttk.Button(mainframe, text='-', command=partial(self.ponerOPERADOR, '-')).grid(column=3, row=6, sticky=W, padx=5, pady=5)
        ttk.Button(mainframe, text='*', command=partial(self.ponerOPERADOR, '*')).grid(column=1, row=7, sticky=W, padx=5, pady=5)
        ttk.Button(mainframe, text='%', command=partial(self.ponerOPERADOR, '%')).grid(column=2, row=7, sticky=W, padx=5, pady=5)
        ttk.Button(mainframe, text='=', command=partial(self.ponerOPERADOR, '=')).grid(column=3, row=7, sticky=W, padx=5, pady=5)
        ttk.Button(mainframe, text='/', command=partial(self.ponerOPERADOR, '/')).grid(column=2, row=8, sticky=W, padx=5, pady=5)
        ttk.Button(mainframe, text='C', command=self.borrarPanel).grid(column=3, row=8, sticky=W, padx=5, pady=5)
        self.__panel.set('')
        panelEntry.focus()
        #-------------------------
        self.__ventana.mainloop()
        #-------------------------
    


    def borrarPanel(self):
        self.__panel.set('')

    # 3/4 % 3/5
    def ponerNUMERO(self, numero):
        if self.__operadorAux==None:
            valor = self.__panel.get()
            self.__panel.set(valor+numero)
        else:
            self.__operadorAux=None
            valor=self.__panel.get()
            self.__primerOperando=int(valor)
            self.__panel.set(numero)


    def resolverOperacion(self, operando1, operacion, operando2):
        resultado=0
        if operacion=='+':
            resultado=operando1+operando2
        elif operacion=='-':
            resultado=operando1-operando2
        elif operacion=='*':
            resultado=operando1*operando2
        elif operacion=='%':
            resultado=operando1/operando2
        elif operacion=='/':
            if self.__primerOperando1 is None:
                self.__primerOperando1=operando1
                self.__segundoOperando1=operando2
            else:
                self.__primerOperando2=operando1
                self.__segundoOperando2=operando2
                
        self.__panel.set(str(resultado))
        
        
    # 3/4 + 1/2 = 5/4
    def ponerOPERADOR(self, op):
        if op=='=':
            operacion=self.__operador.get()
            self.__segundoOperando=int(self.__panel.get())
            self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
            self.__operador.set('')
            self.__operadorAux=None
        else:
            if self.__operador.get()=='':
                self.__operador.set(op)
                self.__operadorAux=op
            else:
                operacion=self.__operador.get()
                self.__segundoOperando=int(self.__panel.get())
                self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
                self.__operador.set(op)
                self.__operadorAux=op
        
        









if __name__ == '__main__':
    cal = Calculadora()
