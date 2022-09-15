print("Ahora tendremos otra tanda de ejercicios.\n")
print('Escribiremos "Hola" cuantas veces se quiera.\n')
x = int(input("¿Cuántas veces se repetirá?\n"))
print("\n")
for i in range (0,x):
  print ("Hola")
print("\nAhora se escribirán los números en cuenta regresiva.\n")
y = int(input("¿Cúal es el número mayor?\n"))
print("\n")
for o in range (0,y+1):
  print(y)
  y -= 1
print("\nAhora haremos un triángulo.")
z = int(input("¿Cuántos pisos tendrá?\n"))
for a in range (0,z+1):
  for j in range (0,a):
    print("+", end=" ")
  print(" ")
