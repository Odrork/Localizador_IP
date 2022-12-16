"""
        Interfaz grafica para Localizador de IP.

        Version = 0.2

        Novedades: 
        
            - Creacion de dos nuevos botones: 'Aceptar' y 'Cancelar' 
            - Implementacion de la funcion de Localizar

        ----Odrork----
"""

from tkinter import * 
from tkinter import ttk
import geocoder as geo

#Declaracion variable vacia, utilizada para almacenar la IP entrada.
IP = ' '

#Funcion que devuelve la direccion de la IP
def Localizar (IP): 
    g = geo.ip(IP)
    print('La IP entrada proviene de {}, {}'.format(g.country,g.city))
     
#Creacion de la raiz. La raiz es eel contenedor base de todos los widgets que se iran integrando
root = Tk()
root.title('Localizador IP')        #Título de la ventana
root.config(width=300, height=200)

#Creacion del primer label de texto
label = Label(root, text="Entrada IP")
label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

#Creación de la entrada de IP por pantalla. 
entry = Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)
entry.config(justify="rigth", state="normal")

#Boton 'Aceptar' 
buttonAceptar = Button(root, text='Aceptar', command=Localizar(label))
buttonAceptar.place(x=40, y=20)
buttonAceptar.grid(row=4, column=0, padx=5, pady=5)

#Boton 'Cancelar' 
buttonCancelar = Button(root, text='Cancelar', command=root.destroy)
buttonCancelar = ttk.Button('Cancelar')
buttonCancelar.grid(row=4, column=1, padx=5, pady=5)

#Loop de la ventana. 
root.mainloop()


