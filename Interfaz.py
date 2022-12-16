"""
        Interfaz grafica para Localizador de IP.

        Version = 0.2.1

        Novedades: 
        
            - Boton aceptar suprimido, remplazado por un entry que devolvera el resultado
            - Frame creado para poder darle estilo a la ventana

        ----Odrork----
"""

from tkinter import * 
from tkinter import messagebox as MessageBox
import geocoder as geo

#Declaracion variable vacia, utilizada para almacenar la IP entrada.
IP = '190.111.40.250'

r= StringVar()

def Localizar (IP): 
    g = geo.ip(IP)
    print('La IP entrada proviene de {}, {}'.format(g.country,g.city))
     
#Creacion de la raiz. La raiz es eel contenedor base de todos los widgets que se iran integrando
root = Tk()
root.title('Localizador IP')        #Título de la ventana

frame = Frame(root)
frame.config(width=200, height=200, bg='CFCF0C')

#Creacion del primer label de texto
label = Label(frame, text='Entrada IP')
label.grid(row=0, column=0, sticky='w', padx=5, pady=5)

#Creación de la entrada de IP por pantalla. 
entry = Entry(frame)
entry.grid(row=0, column=1, padx=5, pady=5)
entry.config(justify='rigth', state='normal')

#Label salida del resultado
Label(frame, text="Localizacion").pack()
label.grid(row=1,column=0,sticky='w', padx=5, pady=5)

#Impresion del resultado
Entry(frame, justify="center", textvariable=r, state="disabled").pack()
entry.grid(row=1, column=1, padx=5, pady=5)

#Boton 'Cancelar' 
buttonCancelar = Button(frame, text='Cerrar', command=root.destroy, justify='center')
buttonCancelar.place(x=200, y=20)
buttonCancelar.grid(row=4, column=1, padx=5, pady=5)

#Loop de la ventana. 
root.mainloop()
