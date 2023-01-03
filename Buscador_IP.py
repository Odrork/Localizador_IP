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
    try:
        print('La IP entrada proviene de {}, {}'.format(g.country,g.city))
        print('lat: {}, lon {}'.format(g.lat,g.lng))
        o = input('¿Desea continuar (s/n)?: ')
    except:
        print('IP no valida')
    if o == 'n': 
        break
