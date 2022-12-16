"""
        Interfaz grafica para Localizador de IP.

        Version = 0.2.1

        Novedades: 
        
            - Boton aceptar suprimido, remplazado por un entry que devolvera el resultado
            - Implementacion de estilo 

        ----Odrork----
"""

from tkinter import * 
from tkinter import messagebox as MessageBox
import geocoder as geo

#Declaracion variable vacia, utilizada para almacenar la IP entrada.
IP = ''

r= StringVar()

def Localizar (IP): 
    g = geo.ip(IP)
    print('La IP entrada proviene de {}, {}'.format(g.country,g.city))
     
#Creacion de la raiz. La raiz es eel contenedor base de todos los widgets que se iran integrando
root = Tk()
root.title('Localizador IP')        #Título de la ventana
root.config(bg='#83837F')


#Creacion del primer label de texto
label = Label(root, text='Entrada IP')
label.grid(row=0, column=0, sticky='w', padx=5, pady=5)

#Creación de la entrada de IP por pantalla. 
entry = Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)
entry.config(justify='rigth', state='normal')

#Label salida del resultado
Label(root, text="Localizacion").pack()
label.grid(row=1,column=0,sticky='w', padx=5, pady=5)

#Impresion del resultado
Entry(root, justify="center", textvariable=r, state="disabled").pack()
entry.grid(row=1, column=1, padx=5, pady=5)

#Boton 'Cancelar' 
buttonCancelar = Button(root, text='Cerrar', command=root.destroy, justify='center')
buttonCancelar.place(x=200, y=20)
buttonCancelar.grid(row=4, column=1, padx=5, pady=5)

#Loop de la ventana. 
root.mainloop()
