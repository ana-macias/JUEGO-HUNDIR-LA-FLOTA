import numpy as np
import random
import variables as vr

def crear_tablero():
    return np.full((10, 10), "_")

def colocar_barcos_manual(tablero):
    for barco, tamaño in vr.barcos.items():
        colocado = False
        while not colocado:
            try:
                print(f"\nColoca tu {barco} (tamaño {tamaño})")
                fila = int(input("Fila inicial (0-9): "))
                columna = int(input("Columna inicial (0-9): "))
                orientacion = input("Orientación (H para horizontal, V para vertical): ").upper()

                if orientacion == "H":
                    for i in range(tamaño):
                        tablero[fila, columna+i] = "O"
                elif orientacion == "V":
                    for i in range(tamaño):
                        tablero[fila+i, columna] = "O"
                else:
                    print("Orientación inválida.")
                    continue
                colocado = True
            except:
                print("Entrada inválida.")
    return tablero

def colocar_barcos_aleatorio(tablero):
    for barco, tamaño in vr.barcos.items():
        colocado = False
        while not colocado:
            fila = random.randint(0, 9)
            columna = random.randint(0, 9)
            orientacion = random.choice(["H", "V"])
            if orientacion == "H":
            
                for i in range(tamaño):
                        tablero[fila, columna+i] = "O"
                colocado = True
            else:
                
                for i in range(tamaño):
                        tablero[fila+i, columna] = "O"
                colocado = True
    return tablero

def disparo(tablero_objetivo, tablero_disparos=None):
    
    fila = int(input("Selecciona la fila (0-9): "))
    columna = int(input("Selecciona la columna (0-9): "))

    if tablero_objetivo[fila, columna] == "O":
            tablero_objetivo[fila, columna] = "X"
            print("¡Impacto!")
            if tablero_disparos is not None:
                tablero_disparos[fila, columna] = "X"
    elif tablero_objetivo[fila, columna] in ["#", "X"]:
            print("Posición ya seleccionada. Pierdes el turno.")
    else:
            tablero_objetivo[fila, columna] = "#"
            print("Agua.")
            if tablero_disparos is not None:
                tablero_disparos[fila, columna] = "#"

    print("Entrada inválida. Pierdes el turno.")
    return tablero_objetivo

def quedan_barcos(tablero):
    return "O" in tablero