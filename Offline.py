from random import randint

print("************")
print("* PAPELAZO *")
print("************\n")

opciones = ["piedra", "papel", "tijeras"]

points_player = 0
points_pc = 0
ronda = 1

nickname = input("¿Cual es tu nombre de usuario?: \n")

while points_player < 2 and points_pc < 2:

    print(f"RONDA {ronda} : {nickname} vs PC")

    user = input("¿Piedra, Papel o Tijeras?: ")
    user = user.replace(" ", "").lower()

    pc = opciones[randint(0, 2)]
    print(f"\nLa computadora ha elegido: {pc}")

    if user in opciones:
        print(f"\nEl usuario ha elegido: {user}")

        if user == pc:
          print(f"{nickname} : {user}  VS  Pc : {pc}")
          print("\n¡Empate!")
          points_player += 0
          points_pc += 0

        elif user == "piedra" and pc == "tijeras":
          print(f"{nickname} : piedra  VS  Pc : tijeras")
          print("\n¡Ganaste!")
          points_player += 1
        
        elif user == "piedra" and pc == "papel":
          print(f"{nickname} : piedra  VS  Pc : papel")
          print("\n¡Perdiste!")
          points_pc += 1

        elif user == "papel" and pc == "piedra":
          print(f"{nickname} : papel  VS  Pc : piedra")
          print("\n¡Ganaste!")
          points_player += 1

        elif user == "papel" and pc == "tijeras":
          print(f"{nickname} : papel  VS  Pc : tijeras")
          print("\n¡Perdiste!")
          points_pc += 1

        elif user == "tijeras" and pc == "papel":
          print(f"{nickname} : tijeras  VS  Pc : papel")
          print("\n¡Ganaste!")
          points_player += 1

        elif user == "tijeras" and pc == "piedra":
          print(f"{nickname} : tijeras  VS  Pc : piedra")
          print("\n¡Perdiste!")
          points_pc += 1
        
        print(f"MARCADOR : {nickname} : {points_player} - Pc : {points_pc}\n\n")
        ronda += 1
    
    else: 
      print(f"\nLa opcion {user} no es valida")

if points_pc > points_player:
  print("\n¡Derrota!")
elif points_player > points_pc:
  print("\n¡Victoria!")
  
print("\nFin del Juego")