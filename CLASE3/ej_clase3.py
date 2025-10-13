"""
1- Solicita al cliente o clienta su nombre, apellido, edad y correo electronico
2- Compruebe que el nombre, el apellido y el correo no esten en blanco, y que la edad sea mayor a 18 años
3- Muestre los datos por la terminal, en el orden que se ingresaron. Si alguno de los datos ingresados no cumple los requisitos,
   solo mostrar el texto 'ERROR!'

"""

print("=== Registro de Cliente ===")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
correo = input("Ingrese su correo electronico: ")

if(nombre==""): 
    print("ERROR!")
else:
    print(nombre)
if(apellido==""): 
    print("ERROR!")
else:
    print(apellido)
if(edad=="" or int(edad) <=18): 
    print("ERROR!")
else:
    print(edad)

if(correo==""): 
    print("ERROR!")
else:
    print(correo)
    
