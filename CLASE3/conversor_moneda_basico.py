# Ejercicio de conversion de moneda
valor_dolar = 900
valor_euro  = 950

nombre =         input("Nombre        : ")
monto_en_pesos = int(input("Monto en pesos: "))

print(f"total Pesos   : $ {monto_en_pesos} ")
print(f"total Dolares : U$S {monto_en_pesos / valor_dolar }")
print(f"total Euros   : € { monto_en_pesos / valor_euro }")