print("Continuamos con las trivias, esta será una de dos preguntas.\nComo siempre, comenzaremos conociéndomos un poco.\n")
nombre = input("¿Cuál es tu nombre?\n")
puntos = 0
print("\n¡Genial, ",nombre,"!\nComencemos con las preguntas.\n")
print("Empezarás con ", puntos,"puntos.Recuerda que solo debes escribis la letra de la respuesta.\n")
print ("1) ¿En qué año fue el combate de Angamos?\n")
print ("a) 1879")
print ("b) 1934")
print ("c) 2021")
print ("d) ¿Combate, es bacán?\n")
respuesta_1 = input()
while respuesta_1 != "a":
  print("\nUy, parece que alguien reprobó historia en la escuela, inténtalo nuevamente\n")
  respuesta_1 = input()
puntos += 10
print("\n¡Bien, obtuviste ", puntos,"puntos! Sigamos con la siguiente pregunta.\n")
print ("1) ¿Quién fue héroe en ese combate?\n")
print ("a) Miguel Grau")
print ("b) Jose Olaya")
print ("c) Avelino Cáceres")
print ("d) El Chapulin Colorado\n")
respuesta_2 = input()
if respuesta_2 == "b":
  print("\n¡No! Olaya no fue, el se comía las cartas")
elif respuesta_2 == "c":
  print("\nÉl tampoco, era brujo")
elif respuesta_2 == "d":
  print("\nUhmm, buen intento pero tampoco fue el Chapulin")
elif respuesta_2 == "x":
  puntos += 9999999999
  print("\nEsta es una opción secreta, ahora tienes ", puntos," y ademas obtuviste la vacante para la beca")
else: 
  puntos += 10
  print("\n¡Respuesta correcta! Ahora tienes ", puntos,"puntos.")

