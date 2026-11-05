#Actividad 08-oct-26 Eliza yepes 
# # Mostrar las primeras 10 filas.
# Cuántas filas tiene?
#Mostrar solo las columnas:
# Producto
# Precio
# Mostrar únicamente productos mayores a $100.000.
# Crear una columna Precio Final.
# Mostrar únicamente productos de laptop.
import pandas as pd
ventas = pd.read_excel("Archivos-clase/Ventastaller.xlsx")
print("Dimensiones de ventas:", ventas.shape)
print(ventas.head(10))
print(ventas[["Producto","Precio_Unitario"]])
print(ventas[ventas["Precio_Unitario"] > 100000])