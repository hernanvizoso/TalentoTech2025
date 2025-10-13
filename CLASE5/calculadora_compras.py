
# ▶️Pedir el monto de una compra.

# ▶️Si supera $10.000 → aplicar 20% de descuento.

# ▶️Si está entre  5.000y 10.000 → aplicar 10%.

# ▶️Si es menor → no hay descuento.

# 🔴Mostrar el precio final.

compra = 0
descuento = 0

while compra == 0:
    compra=input("ingrese el monto de la compra: ")
    
    if not compra.isdigit() and int(compra > 0):
        print("Error! ingrese un valor positivo mayor a 0")
        
compra = int(compra)

if compra > 10000:
    descuento = 20
elif compra <= 10000 and compra >=5000:
    descuento = 10

print (f"Total compra   : $  {compra}")
print (f"Total descuento: % {descuento}")
if descuento > 0:
    print(f"Total a pagar  : $ {compra - (compra * descuento / 100)}")
else: 
    print(f"Total a pagar  : $ {compra }")

    


        
    