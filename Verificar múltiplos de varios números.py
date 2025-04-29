# Verificar múltiplos de varios números
# 
# Datos utilizados para los cálculos:
# Crear un programa un número dado por el usuario
# Verifique si es múltiplo de: 2, 3, 5, 7, 9, 10 y 11.
# Imprimir un mensaje por cada verificación.
#
def calcular(x,y):
    if x % y == 0:
        print(f"{x} es multiplo de {y}")
    elif y % x == 0:
        print(f"{y} es multiplo de {x}")
    else:
        print("Los números no son multiplos")
a = int(input("Ingrese un número: "))
b = 2
c = 3
d = 5
e = 7
f = 9
g = 10
h = 11
print("Resultado multiplo de 2")
calcular(a,b)
print()
print("Resultado multiplo de 3")
calcular(a,c)
print()
print("Resultado multiplo de 5")
calcular(a,d)
print()
print("Resultado multiplo de 7")
calcular(a,e)
print()
print("Resultado multiplo de 9")
calcular(a,f)
print()
print("Resultado multiplo de 10")
calcular(a,g)
print()
print("Resultado multiplo de 11")
calcular(a,h)
print()
print("Programa finalizado")
print()
input("Presione ENTER para cerrar")