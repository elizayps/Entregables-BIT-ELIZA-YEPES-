 #actividad 01-10-26 Eliza yepes
#inventario de una tienda
inventario = [
    {"producto": "camisa", "precio": 25900, "stock": "11"},
    {"producto": "pantalon", "precio": 39900, "stock": "23"}
]
#1 añadir nuevo producto al inventario
inventario.append({"producto":"abrigo","precio": 50000,"stock": "23"})
#comprueba que se agrego correctamente 
print(inventario)
#2 convertir los valores de stock en numeros enteros 
for x in inventario: 
    x ["stock"] = int(x["stock"])
#comprueba si los valores de stock pasaron a numeros enteros 
print(inventario)
#3 actualiza el precio de cada producto sumando 10000
for nuevo_precio in inventario:
    nuevo_precio ["precio"] += 10000
print(inventario)
#4 imprime con f-string
for item in inventario:
    print(f'Hay{item["stock"]}unidades del producto {item["producto"]}. su precio por unidad es de {item["precio"]}')