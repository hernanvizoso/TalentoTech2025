# ***📌 Tabla de multiplicar***

# Consigna:

# Mostrar la tabla de multiplicar de un numero n hasta m elementos, ambos datos serán solicitados al usuario.

# Validar que sean enteros positivos ( >=1 ).

multiplicando = 0
multiplicador = 0
contador = 1
resultado = False

while resultado == False:
    multiplicando = input ("ingrese numero a multiplicar: ")
    if multiplicando.isdigit():
        multiplicando = int(multiplicando)
        resultado = True
    else:
        print(f"Error! ingrese solo numeros")
    

resultado = False
while resultado == False:
    multiplicador = input (f"ingrese la cantidad de veces a multiplicar el numero {multiplicando}: ")
    if multiplicador.isdigit():
        multiplicador = int(multiplicador)
        resultado = True
    else:
        print(f"Error! ingrese solo numeros")
        
title = "Impreso con bucle while"
print(f"{title:#^100}")

while contador <= multiplicador:
    print(f"{multiplicando} * {contador} = {multiplicando * contador}")
    contador +=1
    
contador = 0

title = "impreso con el bucle for in range"
print(f"{title: ^100}")
for i in range(1,multiplicador+1):
    print(f"{multiplicando} * {i} = {multiplicando * i}")
    

    

    
    


