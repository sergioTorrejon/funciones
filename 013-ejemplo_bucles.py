#*********************************
# AUTORIDAD DE PENSIONES Y SEGUROS
# AUTOR: SERGIO TORREJON ALBORNOZ
#*********************************
array = [2,3,4,5]
for i in array:
    print('Hola', end=' ')
print()

print('-------------------------------------------')
for numero in  array:
    print(f'El doble de número {numero} es: {numero * 2}')
print()


print('-------------------------------------------')
for i in [0, 1, 2]:
    print(f"{i} * {i} = {i ** 2}")

print()
for i in [0, 1, 2, 3]:
    print(f"{i} * {i} * {i} = {i ** 3}")

print('-------------------------------------------')
for i in "SERGIO":
    print(f'{i}')
print()

input('presione enter para salir')