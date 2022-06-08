#*********************************
# AUTORIDAD DE PENSIONES Y SEGUROS
# AUTOR: SERGIO TORREJON ALBORNOZ
#*********************************
a = int(input('Ingrese su edad: '))
if a < 18:
    print(f'Usted tiene {a} años es MENOR de Edad')
if a >= 18:
    print(f'Usted tiene {a} años es MAYOR de Edad')

print('-------------------------------------------')
b = int(input('Ingrese los años de trabajo: '))
if b < 25:
    pass
if b >= 25:
    print(f'Usted tiene {b} años ya puede jubilarse')
if b >= 40:
    print(f'Usted tiene {b} años ya deberia jubilarse')


print('-------------------------------------------')
c = int(input("¿Cuántos años tiene? "))
if c >= 18:
    print("Es usted mayor de edad")
elif c < 0:
    print("No se puede tener una edad negativa")
else:
    print("Es usted menor de edad")

input('presione enter para salir')