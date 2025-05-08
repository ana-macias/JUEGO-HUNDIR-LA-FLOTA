# JUEGO-HUNDIR-LA-FLOTA
Desarrollo en Python del juego

Estructura del Programa

1.- Crear Tableros:
Se generan cuatro tableros (matrices de 10x10):
Dos para el jugador: barcos y disparos.
Dos para el rival: barcos y disparos.
Cada casilla empieza vacía ("_").

2.- Colocación de Barcos:
Manual (Jugador): El jugador introduce la posición y orientación (horizontal o vertical) de cada barco.
Aleatoria (Rival): El programa coloca los barcos del rival en posiciones válidas aleatorias sin superposiciones.

3.- Disparos:
El jugador y el rival realizan disparos alternados:
Si aciertan un barco ("O"), se marca con "X".
Si fallan, se marca con "#".
Si ya dispararon a esa casilla, pierden el turno.

4.- Verificación de victoria:
Después de cada turno, se revisa si aún quedan barcos ("O") en el tablero del oponente.
Si no quedan barcos, el juego termina y se anuncia al ganador.

5.- Variables
Los barcos barcos están en un diccionario con los nombres y tamaños de los barcos, por ejemplo:
vr.barcos = {"Acorazado": 4,"Crucero": 3,"Lancha": 2}








