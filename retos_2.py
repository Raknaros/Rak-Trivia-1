import time
print("Ahora, más retos.\n")
x = int(input("Ingresa tu edad: \n"))
print("\n")
for i in range (1,x+1):
  print(i)
time.sleep(2)
print("\nAhora escribiremos solo los impares.")
y = int(input("\nIngresa un número: \n"))
print("\n")
for j in range (y,0,-2):
  print(j)
time.sleep(2)
print("\nAhora tendremos un factorial.")
f = 1
z = int(input("Ingresa el número para calcular el factorial: \n"))
for k in range (1,z+1,1):
  f *= k
print (f)