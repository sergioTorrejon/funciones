#*********************************
# AUTORIDAD DE PENSIONES Y SEGUROS
# AUTOR: SERGIO TORREJON ALBORNOZ
#*********************************
numero = int(input("Escriba el tamaño de la Lista: "))
lista = []
for i in range(numero):
    valor = int(input(f"Ingrese un numero posición {i+1} :"))
    lista.append(valor)

print(lista)

print('-------------------------------------------')

numero = int(input("Escriba el tamaño de la Lista: "))
lista = []
for i in range(numero):
    valor = input(f"Ingrese un palabra en posición {i+1} :")
    lista.append(valor)

print(lista)

print()
input('presione enter para salir')