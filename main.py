from  utils import (crear_tablero,colocar_barcos_manual,colocar_barcos_aleatorio,disparo,quedan_barcos)
import time

# Crear tableros
tablero_rival = crear_tablero()
tablero_jugador = crear_tablero()
tablero_disparos_jugador = crear_tablero() 

# Colocar barcos
print("Colocando barcos del jugador...")
colocar_barcos_manual(tablero_jugador)

print("\nColocando barcos del rival...")
colocar_barcos_aleatorio(tablero_rival)

# Iniciar turnos
turno = 1
while True:
    print(f"Turno {turno}: {'Jugador' if turno % 2 != 0 else 'Rival'}")

    if turno % 2 != 0:
        disparo(tablero_rival, tablero_disparos_jugador)
        print("\nTablero del jugador (disparos realizados):")
        print(tablero_disparos_jugador)
        if not quedan_barcos(tablero_rival):
            print("¡Jugador gana!")
            break
    else:
        time.sleep (2.0) # Tiempo que está pensando la máquina
        disparo(tablero_jugador)
        print("\nTablero del jugador (tus barcos):")
        print(tablero_jugador)
        if not quedan_barcos(tablero_jugador):
            print("¡Rival gana!")
            break

    turno += 1