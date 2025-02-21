# calculadora
calculadora con interfaz grafica simple usando tkinter
import tkinter as tk 
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")

entrada_texto = tk.StringVar()

entrada = tk.Entry(ventana, textvariable=entrada_texto, font=("arial",20),
                   bd=10, insertwidth=2, width=14, justify="right") 
entrada.grid(row=0, column=0, columnspan=4) 

def click_boton(valor):
    actual = entrada_texto.get() 
    entrada_texto.set(actual + str(valor))

def limpiar():
    entrada_texto.set("")

def calcular():
    try:
        resultado = eval(entrada_texto.get())
        entrada_texto.set(resultado)
    except:
        messagebox.showerror("Error", "Entrada invalida")    

botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]                 

fila = 1 
columna = 0
for boton in botones:
    if boton == "=":
        b = tk.Button(ventana, text=boton, padx=20, pady=20, font=("Arial", 14),
                      command=calcular, bg="lightgreen")  
    elif boton == "C":
        b = tk.Button(ventana, text=boton, padx=20, pady=20, font=("Arial", 14),
                      command=limpiar, bg="lightcoral")  
    else:
        b = tk.Button(ventana, text=boton, padx=20, pady=20, font=("Arial", 14),
                      command=lambda valor=boton: click_boton(valor))
        
    b.grid(row=fila, column= columna, sticky="nsew")
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1
    
for i in range(5):
    ventana.grid_rowconfigure(i, weight=1)
    ventana.grid_columnconfigure(i, weight=1)
    
ventana.mainloop()          
