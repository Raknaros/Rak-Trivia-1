print("Hola, te invito a jugar esta nueva trivia.\n")

nombre = input("¿Cuál es tu nombre?\n")

print("Genial, ", nombre,", comenzaremos la trivia.\n")
edad = int(input("¿Qué edad tienes?\n"))

if edad >= 25:
  print("Oh, tienes ", edad," años. Esta trivia es para ti\n")
  print ("1) ¿Quién creó Facebook?\n")
  print ("a) Linus Torvalds")
  print ("b) Bill Gates")
  print ("c) Mark Zuckerberg")
  print ("d) Dennis Ritchie")
  respuesta_1 = input("\nTu respuesta: ")
  if respuesta_1 == "c":
    print("¡Acertaste ", nombre,"!")
  else: print("Inténtalo nuevamente.")
else:
  print("Oh, tienes ", edad," años. Esta trivia es para ti")
  print ("1) ¿Quién creó Paypal y es el dueño de Tesla?\n")
  print ("a) Linus Torvalds")
  print ("b) Bill Gates")
  print ("c) Elon Musk")
  print ("d) Dennis Ritchie")
  respuesta_2 = input("\nTu respuesta: ")
  if respuesta_2 == "c":
    print("¡Acertaste ", nombre,"!")
  else: print("Inténtalo nuevamente.")