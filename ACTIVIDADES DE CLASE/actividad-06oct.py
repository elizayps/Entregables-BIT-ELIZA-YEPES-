#actividad 06-oct-26 ELIZA YEPES 
#Parte 1: Bucle for con edades**
#1.Crea una lista de edades: [12, 17, 8, 15, 22, 9, 30, 25]
#2.Usa un bucle for para iterar sobre cada edad:
# Si la edad es 25, imprime "¡Encontramos al estudiante de 25 años! Deteniendo el análisis." y termina el bucle con break
# Si la edad es menor a 10, omite esa iteración con continue.
# Si la edad es 18 o mayor, imprime "Adulto: [edad] años"
# En cualquier otro caso, imprime " menor: [edad] años"
edades= [12,17,8,15,22,9,30,25]
for edad in edades:
    if edad == 25:
        print("¡ENCONTRAMOS AL ESTUDIANTE DE 25 AÑOS! deteniendo anaisis")
        break
    elif edad < 10:
        continue
    elif edad >= 18:
        print(f'adulto:{edad} años')
    else:
        print(f'menor: {edad} años')   
     