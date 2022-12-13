import geocoder as geo

while True:
    ip=input('Introduce IP: ')
    g = geo.ip(ip)
    print('La IP entrada proviene de {}, {}'.format(g.country,g.city))
    o = input('¿Desea continuar (s/n)?: ')
    if o == 'n': 
        break