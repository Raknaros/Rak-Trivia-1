import random
print("Continuamos con las trivias, esta será una de dos preguntas.\nComo siempre, comenzaremos conociéndomos un poco.\n")
nombre = input("¿Cuál es tu nombre?\n")
puntos = random.randint(0, 11)
print("\n¡Genial, ",nombre,"!\nComencemos con las preguntas.\n")
print("Empezarás con ", puntos,"puntos.Recuerda que solo debes escribis la letra de la respuesta.\n")
print ("1) ¿En qué año comenzó la Segunda Guerra Mundial?\n")
print ("a) 1939")
print ("b) 1934")
print ("c) 2021")
print ("d) Cuando las máquinas tomen el poder.\n")
respuesta_1 = input()
while respuesta_1 != "a":
  puntos -= random.randint(0,4)
  print("\nUy, parece que alguien reprobó historia en la escuela y perdió puntos, inténtalo nuevamente\n")
  respuesta_1 = input()
puntos += random.randint(0, 10)
print("\n¡Bien, obtuviste puntos, ahora tienes ", puntos,"puntos! Sigamos con la siguiente pregunta.\n")
print ("1) ¿Qué provocó dicha guerra?\n")
print ("a) La invasión a Polonia")
print ("b) La llegada de los extraterrestres")
print ("c) Los Anukakis")
print ("d) Los reptilianos\n")
respuesta_2 = input()
if respuesta_2 == "b":
  puntos -= random.randint(0, 4)
  print("\n¡No! Eso aún no pasaba, perdiste puntos y ahora tienes ", puntos,"puntos.")
elif respuesta_2 == "c":
  puntos -= random.randint(0, 4)
  print("\nEllos tampoco estaban en esa época, perdiste puntos y ahora tienes ", puntos,"puntos.")
elif respuesta_2 == "d":
  puntos -= random.randint(0, 4)
  print("\nUhmm, buen intento pero ellos aún no aparecen, perdiste puntos y ahora tienes ", puntos,"puntos.")
elif respuesta_2 == "x":
  puntos += random.randint(50, 900)
  print("\nEsta es una opción secreta, ahora tienes ", puntos," y ademas obtuviste la vacante para la beca")
else: 
  puntos += random.randint(0,10)
  print("\n¡Respuesta correcta! Ahora tienes ", puntos,"puntos.")

