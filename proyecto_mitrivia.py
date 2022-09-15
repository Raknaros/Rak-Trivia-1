# Comenzaremos a redactar nuestra Rak Trivia
print('Estas en la RakTrivia, una trivia sobre World of Warcraft. \n')
print('Veremos que tan veterano eres en videojuegos de tipo MMORPG. \n')
print ("Responder las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Entrer' para enviar tu respuesta. \n")
print ("1) ¿Cuál es el nombre del principe que fue maldecido por el espiritu encerrado en una espada? \n")
print ("a) Rey Arturo")
print ("b) Aragorn")
print ("c) Arthas Menethil")
print ("d) Espadachin Oscuro")

respuesta_1 = input("\nTu respuesta: ")

if respuesta_1 == "b":
  print('Respuesta correcta, eres todo un veterano.')
else: print('U.U al parecer eres nuevo en esto.')