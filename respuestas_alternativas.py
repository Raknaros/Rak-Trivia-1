print("Continuamos con las trivias, esta será una de dos preguntas.\nComo siempre, comenzaremos conociéndomos un poco.\n")
nombre = input("¿Cuál es tu nombre?\n")
print("\n¡Genial, ",nombre,"!\nComencemos con las preguntas.\n")
print("Recuerda que solo debes escribis la letra de la respuesta.\n")
print ("1) ¿En qué año fue la independencia del Perú?\n")
print ("a) 1821")
print ("b) 1934")
print ("c) 2021")
print ("d) Aún no nos independizamos\n")
respuesta_1 = input()
while respuesta_1 != "a":
  print("\nUy, parece que alguien reprobó historia en la escuela, inténtalo nuevamente\n")
  respuesta_1 = input()
print("\n¡Bien! Sigamos con la siguiente pregunta.\n")
print ("1) ¿Quién proclamó la independencia?\n")
print ("a) Don José de San Martin")
print ("b) Simón Bolivar")
print ("c) Tupac Amaru")
print ("d) El Chapulin Colorado\n")
respuesta_2 = input()
if respuesta_2 == "b":
  print("\n¡No! Simón Bolivar no fue, el aún ni llegaba")
elif respuesta_2 == "c":
  print("\nÉl tampoco, ni el Inca ni el revolucionario")
elif respuesta_2 == "d":
  print("\nUhmm, buen intento pero tampoco fue el Chapulin")
elif respuesta_2 == "x":
  print("\nEsta es una opción secreta, y te da la automáticamente la vacante para la beca")
else: print("\n¡Respuesta correcta!")

