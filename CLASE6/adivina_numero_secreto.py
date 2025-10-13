# Adivina el numero secreto
# El programa genera un numero secreto entre 1 y 50.
# El usuario tiene 5 intentos para adivinarlo.
# Despues de cada intento, el programa dice si el numero ingresado es mayor o menor que el secreto

import random

title = "ADIVINA EL NUMERO SECRETO!"
sub_title = "Debera ingresar un numero de 1 a 50."
sub_title2 = "Tiene 5 oportunidades para adivinar. SUERTE!"
numero_secreto = random.randint(1,50)
intentos = 0
total_intentos = 5
acerto = False
print(f"{title: ^80}")
print(f"{sub_title: ^80}")
print(f"{sub_title2: ^80}")
while intentos <=total_intentos and acerto == False:
    respuesta = input("Arriesgue un numero:")
    intentos += 1
    if respuesta.isdigit():       
        if int(respuesta) == numero_secreto:
            print(f"Felicidades! adivino el numero en {intentos} intentos.")
            acerto = True
        elif int(respuesta) > numero_secreto:
            print(f"El numero secreto es menor.")
        else:
            print(f"El numero secreto es mayor")
    else:
        print(f"Error! Ingrese solo numeros del 1 al 50")
    
    # if acerto == False:
    #    respuesta = input(f"Restan {total_intentos - intentos}. Arriesgue un nuevamente:") 
       
if acerto == False:
    print(f"No adivino. Mas suerte la proxima")