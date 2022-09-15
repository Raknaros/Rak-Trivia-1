import time
import random
puntaje = 0
start_trivia = True
intentos = 0
print("Bienvenidos nuevamente a otra de mis trivias.\nEsta vez tendrá una dinámica diferente, podrás intentarlo cuántas veces quieras.")
time.sleep(1)
print("\nLa pregunta será sobre....")
time.sleep(1)
print("videojuegos.")
time.sleep(1)
while start_trivia == True:
  intentos += 1
  print("Este será tu intento número",intentos,".")
  time.sleep(1)
  print ("¿Qué significan las siglas D.O.T.A? \n")
  time.sleep(1)
  print ("a) De Oro Tremenda Aventura")
  time.sleep(1)
  print ("b) Defense Of The Ancients")
  time.sleep(1)
  print ("c) Defición Original Tremenda Aventura")
  time.sleep(1)
  print ("d) Defensa Onde Trabajan Ancianos\n")
  respuesta = input()
  while respuesta != "b":
    print("Inténtalo nuevamente")
    respuesta = input()
  puntaje = random.randint(5,15)
  print("Correcto, tienes ",puntaje,".")
  print("¿Quieres intentarlo nuevamente?")
  repetir = input("Di si, si deseas continuar: \n").lower()
  
  
  