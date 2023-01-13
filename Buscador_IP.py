"""
Devuelve país y cuidad de la IP entrada.

---Odrork--
"""

#Import de geocoder
import geocoder as geo

# Función localizar IP
def Localizador(ip): 
    g = geo.ip(ip)
    print('La IP entrada proviene de {}, {}'.format(g.country,g.city))
    print('lat: {}, lon {}'.format(g.lat,g.lng))


#Creación de bucle while.
while True:
    ip=input('Introduce IP: ') #Entrada de IP
    Localizador(ip)
    o = input('¿Desea continuar (s/n)?: ')
    if o == 'n': 
        break

