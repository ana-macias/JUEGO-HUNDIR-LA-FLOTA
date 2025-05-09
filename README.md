## JUEGO-HUNDIR-LA-FLOTA 

Desarrollo en Python del juego (¡¡¡¡CON MUCHA AYUDA DE CHATGPT!!!!)

Estructura del Programa
El juego se reparte en tres scripts:
    1.- main.py ( script principal que ejecuta el juego)
    2.- utils.py (script desde donde se cargan las funciones que hacen el juego)
    3.- variables.py ( script donde tenemos las variables necesarias para las funciones)

1.- Crear Tableros:
Se generan tres tableros (matrices de 10x10):
Dos para el jugador: barcos y disparos.
Uno para el rival: barcos. (Oculto)
Cada casilla empieza vacía ("_").

2.- Colocación de Barcos:
Manual (Jugador): El jugador introduce la posición y orientación (horizontal o vertical) de cada barco. (No he conseguido que no se salgan)
Aleatoria (Rival): El programa coloca los barcos del rival en posiciones aleatorias. (No he conseguido que no se salgan)

3.- Disparos:
El jugador y el rival realizan disparos alternados:
Si aciertan un barco ("O"), se marca con "X".
Si fallan, se marca con "#".
Si ya dispararon a esa casilla, pierden el turno.

4.- Verificación de victoria:
Después de cada turno, se revisa si aún quedan barcos ("O") en el tablero del oponente.
Si no quedan barcos, el juego termina y se anuncia al ganador.

5.- Variables
Los barcos están en un diccionario con los nombres y tamaños de los barcos:
barcos = {"Acorazado": 4,"Crucero": 3,"Lancha": 2}








