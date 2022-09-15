print("Para este reto haremos una calculadora con las operaciones básicas y de solo dos números. Comencemos\n")
x = int(input("Ingresa el primer número: "))
y = int(input("Ingresa el segundo número: "))
z = input("Ingresa la operación que deseas realizar: ")
if z == "+":
  print("\nEl resultado es ",x+y,".")
elif z == "-":
  print("\nEl resultado es ",x-y,".")
elif z == "*":
  print("\nEl resultado es ",x*y,".")
elif z == "/":
  print("\nEl resultado es ",x/y,".")
else:
  print("Ingresa un operador válido(+, -, *, /)")