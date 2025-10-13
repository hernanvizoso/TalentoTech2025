# Encuesta de popularidad
# Hacer una encuesta sobre cual es el superheroe favorito de los estudiantes.
# Las opciones son "Iron Man", "Spider-Man", "Batman", "Wonder Woman".
# Guardar las respuestas en una lista y al final mostrar cuantos votos obtuvo cada uno

super_heroes = ("Iron Man", "Spider-Man", "Batman", "Wonder Woman")
votos_encuesta = [0,0,0,0]
title = "Resultado de la encuesta:"

for i in range(len(super_heroes)):
    print(f" codigo {i}: {super_heroes[i]}")
    print(f"Presione enter para finalizar")
heroe = input("Ingrese el codigo del super heroe: ")

while heroe != "":
    if heroe.isdigit() and int(heroe) < 5 and int(heroe) > 0:
        votos_encuesta[int(heroe) - 1] +=1
    else:
        print(f"Error! ingrese un codigo valido")
    heroe = input("Ingrese el codigo del super heroe: ")
    
print(f"votos encuesta: {votos_encuesta}")

# encuesta_ordenada = sorted(votos_encuesta)

print(f"")
print(f"{title: ^100}")

for i in range(len(votos_encuesta)):
    print(f"Total votos {super_heroes[i]}: {votos_encuesta[i]}")