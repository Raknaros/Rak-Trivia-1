import time
import random
for x in range (5,0,-1):
  print(x)
  time.sleep(1)
print("¡Comenzó la nueva trivia!\n")
time.sleep(2)
print("Esta vez será una sola pregunta con una ruleta de puntaje aleatorio.\n")
time.sleep(2)
print ("1) ¿Qué país invadió lo que actualmente es Brasíl?\n")
time.sleep(1)
print ("a) Portugal")
time.sleep(1)
print ("b) Inglaterra")
time.sleep(1)
print ("c) España")
time.sleep(1)
print ("d) Los Godos\n")
respuesta = input()
while respuesta != ("a"):
  print("Inténtalo nuevamente")
  respuesta = input()
print("¡Correcto!\nSe viene la ruleta de puntos.")
for y in range (10,0,-1):
  puntos = random.randint(4,10)
  time.sleep(1)
  print(puntos)
print("Obtuviste ",puntos,"puntos.")