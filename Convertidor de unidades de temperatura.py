# Convertidor de unidades de temperatura
# 
# Datos utilizados para los cálculos:
#
#       De ºC a ºF: se multiplica la temperatura en °C por 1.8 y se suma 32
#       De ºC a K: se suman 273.15 a la temperatura en °C
#       
C = 10    # Se define la variable de temperatura en Celsius a ser convertida en Fahrenheint y Kelvin
Fahrenheint = C * 1.8 + 32      # Se define la variable Fahrenheint la cual es la operación de conversión
Kelvin = C + 273.15      # Se define la variable Kelvin la cual es la operación de conversión
print(C),
print("Grados Celsius equivalen a:")
print()
input("Presiona Enter para realizar la Conversión de grados")
print()
print("Fahrenheint")
print(Fahrenheint)   # Muestra el valor de la variable Fahrenheint, siendo este el resultado
print()
print("Kelvin")
print(Kelvin)   # Muestra el valor de la variable Kelvin, siendo este el resultado
print()
print("Programa finalizado")
print()
input("Presione ENTER para cerrar")