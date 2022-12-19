"""
        Interfaz grafica para Localizador de IP.

        Version = 0.2.2

        Novedades: 
        
            - Implementacion de la lectura de la IP por el Entry
            - Cambios en la disposicion de la interfaz

        ----Odrork----
"""
import tkinter as tk
from tkinter import * 
from tkinter import messagebox as MessageBox
import geocoder as geo

IP = tk.StringVar()

def Localizar (IP): 
    g = geo.ip(IP)
    print('La IP entrada proviene de {}, {}'.format(g.country,g.city))
     
#Creacion de la raiz. La raiz es eel contenedor base de todos los widgets que se iran integrando
root = Tk()
root.title('Localizador IP')        #Título de la ventana
root.config(bg='#83837F')  #Estilo de la ventana
root.resizable(0,0)
root.geometry('250x150')

#Label titulo
label_titulo = Label(root, text='Localizador')
label_titulo.place(x=92,y=5)

#Label entrada
label_entrada = Label(root, text='Entrada IP')
label_entrada.grid(row=1, column=0, sticky='w', padx=10, pady=5)
label_entrada.place(x=10,y=40)
label_entrada.config(width=10)

#Creación de la entrada de IP por pantalla. 
entry_entrada = Entry(root, textvariable=IP)
entry_entrada.grid(row=1, column=1, padx=5, pady=5)
entry_entrada.config(justify='rigth', state='normal')
entry_entrada.place(x=100,y=40)

#Label salida del resultado
label_localizacion = Label(root, text='Localizacion')
label_localizacion.grid(row=2,column=0, sticky='w', padx=5, pady=5)
label_localizacion.place(x=10, y=75)
label_localizacion.config(width=10)

#Impresion del resultado
salida_localizacion = Entry(root, state='readonly') #, justify="center", textvariable=r, state="disabled")
salida_localizacion.grid(row=2, column=1, padx=5, pady=5)
salida_localizacion.config(justify='rigth', state='disabled')
salida_localizacion.place(x=100,y=76)

#Boton 'Cancelar' 
buttonCancelar = Button(root, text='Cerrar', command=root.destroy, justify='center')
buttonCancelar.place(x=95, y=110)
# buttonCancelar.grid(row=3, column=0)
buttonCancelar.config(width=7,height=1, foreground='#F53A30')

#Loop de la ventana
root.mainloop()
