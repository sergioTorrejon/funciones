#*********************************
# AUTORIDAD DE PENSIONES Y SEGUROS
# AUTOR: SERGIO TORREJON ALBORNOZ
#*********************************
numero = int(input("Escriba un número: "))
if numero % 2 != 0:
    print(f"{numero} es impar")
else:
    print(f"{numero} es par")

print('-------------------------------------------')
numero = int(input("Escriba un número: "))
if numero % 2:
    print(f"{numero} es impar")
else:
    print(f"{numero} es par")


print('-------------------------------------------')
numero = int(input("Escriba un número: "))
if numero % 2 == 0:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")

print('-------------------------------------------')
numero = int(input("Escriba un número: "))
if not numero % 2:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")

input('presione enter para salir')