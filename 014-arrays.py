#*********************************
# AUTORIDAD DE PENSIONES Y SEGUROS
# AUTOR: SERGIO TORREJON ALBORNOZ
#*********************************
mi_lista = ['Juan', 'Pedro', 'Laura', 'Carmen', 'Susana']
print(mi_lista[0])
print(mi_lista[-1])
print(mi_lista[1])
print(mi_lista[2])
print(mi_lista[-2])

print('-------------------------------------------')
edades = [20, 41, 6, 18, 23]

# Recorriendo los elementos
for edad in edades:
    print(edad)
print()

print('-------------------------------------------')
# Recorriendo los índices
for i in range(len(edades)):
    print(mi_lista[i],edades[i])
print()

print('-------------------------------------------')
# Con while y los índices
indice = 0

while indice < len(edades):
    print(mi_lista[indice],edades[indice])
    indice += 1
print()

print('-------------------------------------------')
# Con while y los índices
lista = []
array = [2,3,4,5]

lista = lista+array

print(lista)

print('-------------------------------------------')
# Con while y los índices
array = [3,5,3]
array1 = [2,3,4,5]

array = array+array1

print(array)

print('-------------------------------------------')
# Con while y los índices
array2 = []

array2.append(10)
array2.append(5)
array2.append(3)

print(array2)

print('-------------------------------------------')
# Con while y los índices
array3 = [2,3,4,5]

array3.pop(2)

print(array3)

print('-------------------------------------------')
# Con while y los índices
array4 = ['hola', 'hello', 'hello', 'hi']

array4.remove('hi')

print(array4)

print('-------------------------------------------')
# Con while y los índices
array5 = [2,3,4,5]
count = len(array5)

print('tamaño de la lista: ',count)

print('-------------------------------------------')
# Con while y los índices
array5 = [2,3,4,5]
count = len(array5)

print('tamaño de la lista: ',count)

print('-------------------------------------------')

colores = ('azul', 'rosa', 'verde','negro','plomo','naranja')
print(colores[2:4])
print(colores[-4:-2])
print(colores[-5:-2])

print('-------------------------------------------')

ltupla = (1, 2, 3)
x, y, z = ltupla
print(x, y, z)

print('-------------------------------------------')

l = [1, 1, 13, 3, 5]
print(l.count(1))

print('-------------------------------------------')
l = [7, 7, 7, 3, 5]
print(l.index(5))

print()
input('presione enter para salir')