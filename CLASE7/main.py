carrito = ["kjkjkj","slsljsl"," ","mouse","teclado"]
# num = carrito.pop(2)
# num2 = carrito()
# print(carrito)
# print(num)
# print(num2)

# a,b,c = 1,2,3,

# numeros = [1,2,3,50]
# numeros.append(33) # agregar a lo ultimo [1,2,3,50,33]

# productos = [ "leche","Pan","queso","pan"]


# productos.remove("Pan")

# print(productos)  
# Salida: ["leche", "queso"]

carrito = ["sadsadad","asdasdad",""]
carrito.append("mouse")
carrito.append("teclado")

carritoClonado = carrito[::]

elemento_eliminado = carritoClonado.pop()

print("Primer carrito")
print(carrito) # salida: []
print("Segundo carrito")
print(carritoClonado)

par = [2,4,6,8,9]
impar = [1,3,5,7]

numeros = [1,5,7,4,2,7]

eli = par.pop()
impar.append(eli)

par.insert(0,0)
par.extend(impar)
par.sort(reverse=True)

print(par)
print(impar)

invitados = ["Michelle", "Luis", "Cristan","Luis","Pedro"]

posicion = invitados.count("Luis")

print(posicion)

# LIFO (Stack)
pila = []

pila.append("plato 1")
pila.append("plato 2")
pila.append("plato 3")

ultimo = pila.pop()

#FIFO (queue)
cola = []
 
cola.append("persona 1")
cola.append("persona 2")
cola.append("persona 3")

primero = cola.pop(0)
print("primera pers que entra" , primero)

primero = cola.pop(0)
print("segunda pers que entra" , primero)

print(cola)

dias = "lunes","martes","miercoles","jueves","viernes","sabado","domingo"



lista = [1,2,4,5]

lista[2] = 7

dias[2] = "jueves"

a,b = 1,2,3

nombre = "Gustavo"

nombre = "Tri"

print(dias)
# for dia in dias:
#     print(f"Hoy es {dia}")