# Solicite los nombres de los y las clientes uno por uno y valide que cada nombre no esté vacío. 
# Si se deja el campo vacío, mostrar un mensaje de advertencia y volver a pedir el nombre.

# Guarde cada nombre válido en una lista, asegurándote de agregarlo con el método .append(). 

# Permití que se finalice la carga de nombres escribiendo la palabra "fin". 

# Una vez finalizada la carga, ordená alfabéticamente los nombres en la lista y mostrá la lista ordenada utilizando un bucle for.

lista_clientes = []
nombre = ""
title = "Ingreso de clientes."
titulo_clientes_registrados = "Clientes registrados:"
error_nombre_vacio= "El nombre no puede estar vacio."
error_nombre_con_numero = "El nombre solo puede contener letras"
pido_cliente = "Ingrese el nombre del cliente o fin para finalizar: "
datos_no_ingresados = "No se han ingresado datos de clientes."


def muestro_error(error):
    '''
    muestro_error
        imprime el error.
        
        Parametros:
            Error a imprimir.
            
        Retorna:
            non
    '''
    print(f"\n {error}")   

     
# help(muestro_error)

print(f"\n{title: ^120}\n")

nombre= input(f"\n {pido_cliente}")

while nombre != "fin":
    valido_nombre = nombre.replace(" ","")
    if valido_nombre == "":
        # print(f"\n {error_nombre_vacio}")
        muestro_error(error_nombre_vacio)
        
    elif valido_nombre.isalpha(): 
        lista_clientes.append(nombre)
        
    else:
        # print(f"\n {error_nombre_con_numero}")
        muestro_error(error_nombre_con_numero)
        
    nombre= input(f"\n {pido_cliente}")
        

lista_clientes_ordenada = sorted(lista_clientes)

print(f"\n {titulo_clientes_registrados: ^90}\n ")

if len(lista_clientes_ordenada) > 0:
    for nombre_cliente in lista_clientes_ordenada:
        print(f"\n {nombre_cliente: ^90}")
else:
    print(f"\n {datos_no_ingresados: ^90}")

