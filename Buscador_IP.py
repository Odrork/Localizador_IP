"""
Devuelve país y cuidad de la IP entrada.

---Odrork--

"""


#Import de geocoder
import geocoder as geo

#Creación de bucle while.
while True:
    ip=input('Introduce IP: ') #Entrada de IP
    g = geo.ip(ip)
    print('La IP entrada proviene de {}, {}'.format(g.country,g.city))
    o = input('¿Desea continuar (s/n)?: ')
    if o == 'n': 
        break
