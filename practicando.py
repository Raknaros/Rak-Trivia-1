print("Comenzaremos con la 2da tanda de ejercicios\n")
print('El primero consiste en repetir una palabra\n')
y = input("Ingresa una palabra: ")
x = int(input("\n¿Cuántas veces quieres que se repita?\n"))

while x > 0:
  print(y)
  x += -1
print("\nEjercicio terminado")

print("\nEl segundo ejercicio es explotar un número del 1 al 10\n")
bomba = int(input("Ingresa el numero que deseas explotar: \n"))
z = 0
while z < 11:
  if z == bomba:
    print("¡BOOM!")
  else:
    print(z)
  z += 1
print("\nEjercicio 2 terminado\n")
print("Ahora procederemos con el último y más difícil ejercicio.\nEste trata de crear un triángulo eligiendo el número de filas que que tendrá.")
filas = int(input("¿Cuántas filas tendrá el triángulo?\n"))
c = 0
while c <= filas:
  f = 0
  while f < c:
    print("+", end = " ")
    f += 1
  print(" ")
  c += 1
print("\nTerminó la 2da tanda de ejercicios")


    

