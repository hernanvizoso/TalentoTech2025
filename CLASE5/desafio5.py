# calcula el total y el promedio de los ultimos meses
# el pgm pide la cantidad de meses a calcular

mes = 1
total = 0
cantidad_meses = 0


while cantidad_meses == 0: 
    meses = input(f"Ingrese la cantidad de meses a ingresar: ")
    if meses.isdigit() and int(meses) > 0:
        cantidad_meses = int(meses)
    else:
        print(f"Error! ingrese un numero entero positivo mayor a 0")
        
while mes < cantidad_meses + 1:
    ingreso_mensual = input(f"Ingrese el monto del mes {mes}: ")
    
    if ingreso_mensual.isdigit():
        total += int(ingreso_mensual)
        mes +=1
    else:
        print(f"Error, El monto a ingresar debe ser un numero entero positivo")

# para que quede prolijo el mensaje final se valida cantidad_meses        
if cantidad_meses > 1:
    print(f"Monto total acumulado en los ultimos {cantidad_meses} meses es de: $ {total}")
    print(f"El promedio mensual de los ultimos {cantidad_meses} es de :  $ {total/cantidad_meses}")
    
else:
    print(f"Monto total del ultimo mes: ${total}")
    print(f"Promedio mensual del ultimo mes {total/cantidad_meses}")

