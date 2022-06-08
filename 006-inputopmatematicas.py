#*********************************
# AUTORIDAD DE PENSIONES Y SEGUROS
# AUTOR: SERGIO TORREJON ALBORNOZ
#*********************************
a = int(input('Introduzca un numero a: '))
b = int(input('Introduzca un numero b: '))
suma = a+b
resta = a-b
multiplicacion = a*b
cuadrado = a**2
cubo = a**3
print('suma :',suma)
print('resta :',resta)
print('multiplicacion :',multiplicacion)
print('exponente al cuadrado de a: ',cuadrado)
print('exponente al cubo de a: ',cubo)

if b==0:
    print('No existe division entre cero')
else:
    division = a/b 
    print('division :',division)
input('presione enter para salir')