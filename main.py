import random
import time
GREEN = '\033[32m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
RESET = '\033[39m'
puntaje1 = 20
puntaje2 = 20
jugar = True
players = []
history = ["¿En qué año fue el combate de Angamos?","¿Quién fue héroe en el combate de Angamos?","¿En qué año fue la independencia del Perú?","¿Quién proclamó la independencia?","¿En qué año comenzó la Segunda Guerra Mundial?","¿Qué provocó la 2da guerra mundial?"]
maths = ["¿Cuánto es 2 x 5 x 17?","¿Cuánto es 10!?","¿Cuánto es la raiz cuadrada de 144?","¿Cuánto es la derivada de x**5?","¿Qué matemático inventó el cálculo diferencial?","¿Qué teorema inventó Pitágoras?"]
videogames = ["¿Qué significan las siglas D.O.T.A?","¿Qué significan las siglas MMORPG","¿Qué significan las siglas MOBA?","¿Cuál es la última consola de Nintendo","¿En qué año se lanzó el Nintendo64?","¿Cuál es el videojuego más famoso y vendido de Nintendo?"]
history1 = ["a) 1847","b) 1934","c) 2021","d) ¿Combate? Es bacán"]
history2 = ["a) Goku","b) Miguel Grau","c) Miguel Abuelo","d) Jose Olaya"]
history3 = ["a) 1559","b) 1821","c) 2020","d) Aún no nos independizamos"]
history4 = ["a) Simon Bolivar","b) Don Jose de San Martin","c) Pedro Castillo","d) Fujimori"]
history5 = ["a) 1800","b) 1939","c) En la 2da vuelta Keiko Castillo","d) Está por comenzar"]
history6 = ["a) La llegada de los extraterrestres","b) La invasión a Polonia","c) Los Anukakis","d) Los reptilianos"]
maths1 = ["a) 1","b) 170","c) 0","d) -55"]
maths2 = ["a) 10","b) 3628800","c) ¡10!","d) Un millón"]
maths3 = ["a) 14","b) 12","c) 4","d) No se de plantas"]
maths4 = ["a) Y","b) 5X","c) 5XY","d) Z"]
maths5 = ["a) Einstein","b) Leibniz","c) Baldor","d) Este programador"]
maths6 = ["a) El Teorema de la Relatividad","b) El Teorema de Pitágoras","c) El Teorema del amor","d) ¿Teo..qué?"]
videogames1 = ["a) De Oro Tremenda Aventura","b) Defense Of The Ancients","c) Defición Original Tremenda Aventura","d) Defensa Onde Trabajan Ancianos"]
videogames2 = ["a) Mejor Migro a Otra Responsabilidad Provincia","b) Masive Multiplayer Online Role Playing Game","c) Mamá Mira Onde Rajo Piedras","d) Mi Mamá Ostenta Real Pelo"]
videogames3 = ["a) Más Otra Bebida Alcohólica","b) Multiplayer Online Battle Arena","c) Mejor Opto por Bibir la Aventura","d) Moba?"]
videogames4 = ["a) Play 5","b) Nintendo Switch","c) Xbox One","d) Super Nintendo"]
videogames5 = ["a) 1950","b) 1996","c) 2000","d) Próximamente"]
videogames6 = ["a) Super Mario World","b) Wii Sports","c) Pokemon Red Fire","d) Bomberman X"]
print("¡Bienvenidos a la trivia definitiva!\n")
time.sleep(1)
print("Este será un juego para dos, cada jugador podrá elegir su tema y se elegirá quién jugará primero al azar.\n")
print("Tenemos tres temas para elegir:\n")
print(CYAN+"History"+RESET)
print(MAGENTA+"Maths"+RESET)
print(GREEN+"Videogames"+RESET)
time.sleep(2)
print("\nLuego de responder bien cada pregunta se le descontarán puntos de forma aleatoria al otro jugador.\n")
time.sleep(1)
print("El jugador que conserve puntos ganará.\n")
time.sleep(1)
print("Primero vamos a conocernos")
time.sleep(1)
player1 = input("Primer jugador dinos tu nombre: ")
tema1 = input("Ahora elige tu tema:\n").lower()
if tema1 == "history":
  tema3 = history
elif tema1 == "maths":
  tema3= maths
else: tema3 = videogames
player2  = input("Ahora el segundo jugador: ")
tema2 = input("Ahora elige tu tema:\n").lower()
if tema2 == "history":
  tema4 = history
elif tema2 == "maths":
  tema4 = maths
else: tema4 = videogames
players.append(player1)
players.append(player2)
input("\nPresiona ENTER para comenzar a jugar...")
while jugar == True:
  elegirplayer = random.randint(0,1)
  if elegirplayer == 1:
    print("Responde ",player1,"...")
    X = random.randint(0,5)
    print(tema3[X])
    if X == 0 and tema1 == "history":
      for i in history1:
        print(i)
        time.sleep(1)
    elif X == 1 and tema1 == "history":
      for i in history2:
        print(i)
        time.sleep(1)
    elif X == 2 and tema1 == "history":
      for i in history3:
        print(i)
        time.sleep(1)
    elif X == 3 and tema1 == "history":
      for i in history4:
        print(i)
        time.sleep(1)
    elif X == 4 and tema1 == "history":
      for i in history5:
        print(i)
        time.sleep(1)
    elif X == 5 and tema1 == "history":
      for i in history6:
        print(i)
        time.sleep(1)
    elif X == 0 and tema1 == "maths":
      for i in maths1:
        print(i)
        time.sleep(1)
    elif X == 1 and tema1 == "maths":
      for i in maths2:
        print(i)
        time.sleep(1)
    elif X == 2 and tema1 == "maths":
      for i in maths3:
        print(i)
        time.sleep(1)
    elif X == 3 and tema1 == "maths":
      for i in maths4:
        print(i)
        time.sleep(1)
    elif X == 4 and tema1 == "maths":
      for i in maths5:
        print(i)
        time.sleep(1)
    elif X == 5 and tema1 == "maths":
      for i in maths6:
        print(i)
        time.sleep(1)
    elif X == 0 and tema1 == "videogames":
      for i in videogames1:
        print(i)
        time.sleep(1)
    elif X == 1 and tema1 == "videogames":
      for i in videogames2:
        print(i)
        time.sleep(1)
    elif X == 2 and tema1 == "videogames":
      for i in videogames3:
        print(i)
        time.sleep(1)
    elif X == 3 and tema1 == "videogames":
      for i in videogames4:
        print(i)
        time.sleep(1)
    elif X == 4 and tema1 == "videogames":
      for i in videogames5:
        print(i)
        time.sleep(1)
    elif X == 5 and tema1 == "videogames":
      for i in videogames6:
        print(i)
        time.sleep(1)
    respuesta = input("Ingresa tu respuesta: ")
    J = random.randint(1,4)
    if respuesta == "b":
      print("¡Correcto!\nAl otro jugador se le descontarán...", J, "puntos")
      puntaje1 -= J
    else: 
      print("Error, tienes ",J,"puntos menos")
      puntaje2 -= J
  else:
    print("Responde",player2,"...")
    X = random.randint(0,5)
    print(tema4[X])
    if X == 0 and tema2 == "history":
      for i in history1:
        print(i)
        time.sleep(1)
    elif X == 1 and tema2 == "history":
      for i in history2:
        print(i)
        time.sleep(1)
    elif X == 2 and tema2 == "history":
      for i in history3:
        print(i)
        time.sleep(1)
    elif X == 3 and tema2 == "history":
      for i in history4:
        print(i)
        time.sleep(1)
    elif X == 4 and tema2 == "history":
      for i in history5:
        print(i)
        time.sleep(1)
    elif X == 5 and tema2 == "history":
      for i in history6:
        print(i)
        time.sleep(1)
    elif X == 0 and tema2 == "maths":
      for i in maths1:
        print(i)
        time.sleep(1)
    elif X == 1 and tema2 == "maths":
      for i in maths2:
        print(i)
        time.sleep(1)
    elif X == 2 and tema2 == "maths":
      for i in maths3:
        print(i)
        time.sleep(1)
    elif X == 3 and tema2 == "maths":
      for i in maths4:
        print(i)
        time.sleep(1)
    elif X == 4 and tema2 == "maths":
      for i in maths5:
        print(i)
        time.sleep(1)
    elif X == 5 and tema2 == "maths":
      for i in maths6:
        print(i)
        time.sleep(1)
    elif X == 0 and tema2 == "videogames":
      for i in videogames1:
        print(i)
        time.sleep(1)
    elif X == 1 and tema2 == "videogames":
      for i in videogames2:
        print(i)
        time.sleep(1)
    elif X == 2 and tema2 == "videogames":
      for i in videogames3:
        print(i)
        time.sleep(1)
    elif X == 3 and tema2 == "videogames":
      for i in videogames4:
        print(i)
        time.sleep(1)
    elif X == 4 and tema2 == "videogames":
      for i in videogames5:
        print(i)
        time.sleep(1)
    elif X == 5 and tema2 == "videogames":
      for i in videogames6:
        print(i)
        time.sleep(1)
    respuesta = input("Ingresa tu respuesta: ")
    J = random.randint(1,4)
    if respuesta == "b":
      print("¡Correcto!\nAl otro jugador se le descontarán...", J, "puntos")
      puntaje1 -= J
    else: 
      print("Error, tienes ",J,"puntos menos")
      puntaje2 -= J
  G = input("\nSeguimos jugando(si/no): ").lower()
  if G == "no":
    jugar = False
print("Listo, ahora determinaremos quién ganó.\n")
time.sleep(3)
if puntaje1 < puntaje2:
  print(player2)
else: print("¡",player1," has ganado la trivia!\n")
print("Gracias por participar, vuelve pronto.")