# Ejercicio de conversion de moneda
# se agrega corrimiento de toda la tarjeta a la derecha
valor_dolar = 900
valor_euro  = 950

nombre =             input("Ingrese su Nombre        : ")
monto_en_pesos = int(input("Ingrese el monto en pesos: "))

ancho = 100
cantidad_espacios = 30
tabulacion = " " * cantidad_espacios
titulo = "TARJETA DE PRESENTACION"
linea_titulo = f"{tabulacion}║ {titulo.center(ancho - cantidad_espacios - 4)} ║"
linea_nombre = f"{tabulacion}║ Nombre: {nombre}".ljust(ancho - 1) + "║"
linea_monto_pesos = f"{tabulacion}║ Total Pesos   : $ {monto_en_pesos}".ljust(ancho-1) + "║"
linea_dolar =       f"{tabulacion}║ Total Dolares : U$S {monto_en_pesos / valor_dolar }".ljust(ancho -1) +"║"
linea_euro =        f"{tabulacion}║ Total Euros   : € { monto_en_pesos / valor_euro }".ljust(ancho -1) +"║"

borde_superior = f"{tabulacion}╔" + "═" * (ancho - cantidad_espacios - 2) + "╗"
separador = f"{tabulacion}╠" + "═" * (ancho - cantidad_espacios - 2) + "╣"
borde_inferior = f"{tabulacion}╚" + "═" * (ancho - cantidad_espacios - 2) + "╝"

tarjeta=f"""
{borde_superior}
{linea_titulo}
{separador}
{linea_nombre}
{separador}
{linea_monto_pesos}
{linea_dolar}
{linea_euro}
{borde_inferior}
"""


print(tarjeta)
print ("\n¡Esta baratito!! 😂😂😂\n")