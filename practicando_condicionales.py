print("Primer ejercicio")
numero = int(input("Ingrese un numero: "))
if numero >= 0:
  print("\nIngresaste un valor positivo")
else:
  print("\nIngresaste un valor negativo")

print("\nSegundo ejercicio")
numero2 = int(input("Ingrese otro numero: "))
numero2 *= numero2
if numero2 >= 0:
  print("\nIngresaste un valor positivo")
else:
  print("\nIngresaste un valor negativo")

print("\nTercer ejercicio")

numero3 = int(input("Ingrese el primer numero del ejercicio 3: "))
numero4 = int(input("Ingrese el segundo numero del ejercicio 3: "))
if numero3 > numero4:
  print("\nEl numero mayor es ", numero3)
else:
  print("\nEl numero mayor es ", numero4)