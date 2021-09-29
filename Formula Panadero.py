from tkinter import *

raiz= Tk()

raiz.config(bg='purple', bd=60)

miframe=Frame(raiz, width=1200, height=600, bg='light blue', bd=50)

miframe.pack(expand=5)

miharina=StringVar()
miagua=StringVar()
milevadura=StringVar()
misal=StringVar()

Titulo=Label(miframe, text='FORMULA PANADERO:', font=50, bg='light green' )
Titulo.grid(row=0, column=0, sticky='W', padx=10, pady=10)

cuadroharina=Entry(miframe, textvariable=miharina)
cuadroharina.grid(row=1, column=1, padx=10, pady=10)


cuadroagua=Entry(miframe, textvariable=miagua)
cuadroagua.grid(row=2, column=1, padx=10, pady=10)

cuadrolevadura=Entry(miframe, textvariable=milevadura)
cuadrolevadura.grid(row=3, column=1, padx=10, pady=10)


cuadrosal=Entry(miframe, textvariable=misal)
cuadrosal.grid(row=4, column=1, padx=10, pady=10)

def calculoagua():
        
        calculoagua=int(cuadroharina.get()) * (70) / (100) 

        return miagua.set(calculoagua) 

def calculolevadura():

        calculolevadura=int(cuadroharina.get()) * (2) / (100)

        return milevadura.set(calculolevadura)

def calculosal():

        calculosal=int(cuadroharina.get()) * (2) / (100)

        return misal.set(calculosal)


botoncalculo=Button(raiz, text='Realizar calculo', command=lambda: [calculoagua(), calculolevadura(), calculosal()])
botoncalculo.pack()

def cerrar():
    raiz.destroy()

botoncerrar=Button(raiz, text='Cerrar', command=cerrar)
botoncerrar.pack(side=TOP)

harinalabel=Label(miframe, text='Flour (in grams):', font=30, bg='light green')
harinalabel.grid(row=1, column=0, sticky='W', padx=10, pady=10)

agualabel=Label(miframe, text='Water ml:', font=30, bg='light green', textvariable=calculoagua)
agualabel.grid(row=2, column=0, sticky='W', padx=10, pady=10)

levaduralabel=Label(miframe, text='Yeast (in grams):', font=30, bg='light green', textvariable=calculolevadura)
levaduralabel.grid(row=3, column=0, sticky='W', padx=10, pady=10)

sallabel=Label(miframe, text='Salt (in grams):', font=30, bg='light green', textvariable=calculosal)
sallabel.grid(row=4, column=0, sticky='W', padx=10, pady=10)




raiz.mainloop()
