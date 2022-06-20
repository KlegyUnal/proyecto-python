from random import randint

print("*******************")
print("* PAPELAZO ONLINE *")
print("*******************")

opciones = ["piedra", "papel", "tijeras"]

points_player1 = 0
points_player2 = 0
ronda = 1

nickname1 = input("Player1 - ¿Cual es tu nombre de usuario?: \n")
nickname2 = input("Player2 - ¿Cual es tu nombre de usuario?: \n")

while points_player1 < 2 and points_player2 < 2:

    print(f"\nRONDA {ronda} : {nickname1} vs {nickname2}\n")

    user1 = input(f"{nickname1}: ¿Piedra, Papel o Tijeras?: ")
    user1 = user1.replace(" ", "").lower()

    user2 = input(f"{nickname2}: ¿Piedra, Papel o Tijeras?: ")
    user2 = user2.replace(" ", "").lower()

    if user1 and user2 in opciones:

        if user1 == user2:
          print(f"\n{nickname1} : {user1}  VS  {nickname2} : {user2}")
          print("\n¡Empate!")
          points_player1 += 0
          points_player2 += 0

        elif user1 == "piedra" and user2 == "tijeras":
          print(f"\n{nickname1} : piedra  VS  {nickname2} : tijeras")
          print(f"\n¡{nickname1} gana!")
          points_player1 += 1
        
        elif user1 == "piedra" and user2 == "papel":
          print(f"\n{nickname1} : piedra  VS  {nickname2} : papel")
          print(f"\n¡{nickname2} gana!")
          points_player2 += 1

        elif user1 == "papel" and user2 == "piedra":
          print(f"\n{nickname1} : papel  VS  {nickname2} : piedra")
          print(f"\n¡{nickname1} gana!")
          points_player1 += 1

        elif user1 == "papel" and user2 == "tijeras":
          print(f"\n{nickname1} : papel  VS  {nickname2} : tijeras")
          print(f"\n¡{nickname2} gana!")
          points_player2 += 1

        elif user1 == "tijeras" and user2 == "papel":
          print(f"\n{nickname1} : tijeras  VS  {nickname2} : papel")
          print(f"\n¡{nickname1} gana!")
          points_player1 += 1

        elif user1 == "tijeras" and user2 == "piedra":
          print(f"\n{nickname1} : tijeras  VS  {nickname2} : piedra")
          print(f"\n¡{nickname2} gana!")
          points_player2 += 1
        
        print(f"\nMARCADOR : {nickname1} : {points_player1} - {nickname2} : {points_player2}\n")
        ronda += 1
    
    else: 
      print(f"\nUna de las opciones elegidas no es valida")

if points_player2 > points_player1:
  print(f"\n¡{nickname2} HA GANADO!")
elif points_player1 > points_player2:
  print(f"\n¡{nickname1} HA GANADO!")
  
print("\nFin del Juego")
