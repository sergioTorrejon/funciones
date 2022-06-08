#*********************************
# AUTORIDAD DE PENSIONES Y SEGUROS
# AUTOR: SERGIO TORREJON ALBORNOZ
#*********************************
def multiplica_por_5(numero):
    print(f'{numero} * 5 = {numero * 5}')
print('Comienzo del programa')    
multiplica_por_5(7)
print('Siguiente')
multiplica_por_5(113)
print('Fin')

print('-------------------------------------------')
# Con while y los índices
def diHola():
    print("Hello!")

diHola()

print('-------------------------------------------')

def holaConNombre(name):
    print("Hello " + name + "!")

holaConNombre("Ada")

def multiplica(val1, val2):
    print(val1 * val2)
    return val1 * val2

multiplica(3, 5)

def suma(a, b):
    return a + b

result = suma(1, 2)
print(result)

print(max(2, 3)) # Devuelve 3 ya que 3 es el mayor de los dos valores
print(max(2, 3, 23))

list1 = [1, 2, 4, 5, 54]
print(max(list1))

list2 = ['a', 'b', 'c' ]
print(max(list2))


list1 = [1, 2, 4, 5, -54]
print(min(list1)) # Devuelve -54 ya que -54 es el más pequeño de los valores en la lista.

list2 = ['a', 'b', 'c' ]
print(min(list2))

print(divmod(5,2)) # muestra (2,1)
print(divmod(13.5,2.5))

def indeterminados_posicion(*args):
    for arg in args:
        print(arg)

indeterminados_posicion(5,"Hola Plone",[1,2,3,4,5])

def super_funcion(*args,**kwargs):
    total = 0
    for arg in args:
        total += arg
    print ("sumatorio => ", total)
    for kwarg in kwargs:
        print( kwarg, "=>", kwargs[kwarg])

super_funcion(50, -1, 1.56, 10, 20, 300, cms="Plone", edad=38)

print()
input('presione enter para salir')