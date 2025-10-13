#  Parte 1:

# Crear una lista con los nombres de los y las clientes que vamos a procesar. Recorrer la lista y mostrar el nombre de cada cliente o clienta, junto con su posición en la lista (por ejemplo, Cliente 1, Cliente 2, etc.).

# Recorrer la lista con un for y mostrar el nombre de cada cliente junto con su posición en la lista (por ejemplo: Cliente 1: Ana).

# Si encuentras un nombre vacío, mostrar un mensaje de alerta indicando que ese dato no es válido.

# Ejemplo de salida:

# Cliente 1: Ana
# Cliente 2: Juan
# Cliente 3: [ALERTA] Nombre no válido
# Cliente 4: Marta

# Parte 2 (optativa)

# Además, como bonus, probá aplicar el método .capitalize() de Python, que sirve para poner en mayúscula la primera letra de una palabra y en minúscula el resto.

# Ejemplo:

# nombre = "mArIa"
# print(nombre.capitalize())

# Usalo para que los nombres válidos siempre aparezcan en el formato correcto, sin importar cómo estén escritos en la lista.je de alerta indicando que ese dato no es válido.

lista_clientes = []
titulo = " Lista de clientes: "
total_clientes = input("\n Ingrese el total de clientes a registrar o 0 para finalizar: ")
valida_total = False

while valida_total == False:
    if not total_clientes.isdigit():
        print("Error, Ingrese un numero valido.")
        total_clientes = input("Ingrese el total de clientes a registrar o 0 para finalizar.")
        
    else: 
        total_clientes = int(total_clientes)
        valida_total = True
        
print(f"Total Clientes a registrar: {total_clientes}")

for i in range(total_clientes ):
    nombre = input(f"Ingrese el cliente numero {i+1}: ")
    lista_clientes.append(nombre)

print(f"\n{titulo:#^80}\n")
print(f"Total clientes ingresados: {len(lista_clientes)}")
i=1
for cliente in lista_clientes:
    valido_nombre = cliente.replace(" ","")

    if valido_nombre.isalpha():
        print(f"Cliente {i}: {cliente.title()}")
    else:
        print(f"Cliente {i}:[ALERTA] Nombre no válido")
        
    i+=1
    
        