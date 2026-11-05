#01-octubre-26 Eliza yepes 
#**Parte 2: Bucle while con nombres**
#1.Crea una lista de nombres: ["Juan", "Pedro", "Jorge", "María","Ana"].
#2. Usa un bucle while para iterar sobre los nombres:
# Si el nombre es "Ana", imprime "¡Ana está en la lista!" y termina el bucle con break.
# Si el nombre empieza con "J", omite ese nombre con continue.
# En cualquier otro caso, imprime el nombre.

# Crear una lista de nombres
nombres = ["Juan", "Pedro", "Jorge", "María", "Ana"]

# Recorrer la lista con while
i = 0

while i < len(nombres):
    nombre = nombres[i]
    
    i += 1

    if nombre == "Ana":
        print("¡Ana está en la lista!")
        break

    elif nombre[0]== "J":
        continue

    else:
        print(nombre)
    

    