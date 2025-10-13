# Ejercicios clase 2

print("=== Registro de Cliente ===")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
correo = input("Ingrese su correo electronico: ")

ancho = 70
titulo = "TARJETA DE PRESENTACION"
linea_titulo = f"║ {titulo.center(ancho - 4)} ║"
linea_nombre = f"║ Nombre: {nombre} {apellido}".ljust(ancho - 1) + "║"
linea_edad = f"║ Edad: {edad}".ljust(ancho-1) + "║"
linea_correo = f"║ Correo: {correo}".ljust(ancho -1) +"║"

borde_superior = f"╔" + "═" * (ancho - 2) + "╗"
separador = f"╠" + "═" * (ancho - 2) + "╣"
borde_inferior = f"╚" + "═" * (ancho - 2) + "╝"

tarjeta = f"""
{borde_superior}
{linea_titulo}
{separador}
{linea_nombre}
{linea_edad}
{linea_correo}
{borde_inferior}
"""

print ("\n¡Registro completado! Aqui esta la tarjeta del cliente:\n")
print(tarjeta)

