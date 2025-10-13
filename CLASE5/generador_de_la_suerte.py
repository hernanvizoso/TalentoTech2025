# Generador de numeros de la suerte
# Crear un programa que genere una lista de 6 numeros aleatorios del 1 al 49 (como si fuera un sorteo tipo Loto)
# Mostrar los numeros sin repetir y ordenados de menor a mayor

import random


numeros_aleatorios = []
title = "Numeros de la suerte"
titulos_suerte = ("Primer ", "Segundo ", "Tercer ", "Cuarto ", "Quinto ", "Sexto ")

for i in range(6):
    
    numero = random.randint(1,49)
    while numeros_aleatorios.count(numero) > 0:
            numero = random.randint(1,49)

    numeros_aleatorios.append(numero)

numeros_aleatorios_asc = sorted(numeros_aleatorios)
print(f" ")
print(f"Lista original {numeros_aleatorios}")    
print(f"Lista ordenada {numeros_aleatorios_asc}")

print(f"{title:*^100}")

for i in range(len(numeros_aleatorios_asc)):
    print(f"{titulos_suerte[i]: <8} numero: {numeros_aleatorios_asc[i]}")
