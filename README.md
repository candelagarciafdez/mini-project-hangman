# Juego del ahorcado

## Reglas del juego
El jugador debe introducir una letra cuando el programa lo pida. Si la letra está en la palabra, se rellenarán los huecos que la contengan. Si no está, se sumará un fallo y el muñeco del ahorcado irá completándose. Se permiten máximo 5 fallos, al sexto se pierde la partida.

## El programa
El programa escoge una palabra aleatoria de una lista de palabras predefinida mediante *random.choice* . Una vez escogida esta palabra, sustituye las letras por guiones bajos para que esto sea lo que le aparece al jugador. Creamos un contador para el número de fallos y creamos una función que nos diga cómo está el muñeco según el número de fallos que lleva el jugador mediante el índice de la lista que contiene los diferentes pasos del muñeco.
Se crea un bucle que saque al jugador del juego cuando ha rellenado los huecos y otro que lo saque si el número de fallos ha llegado a 6. Cuando los huecos rellenos son iguales a la solución, se sale del bucle y se considera una victoria. Según si el jugador ha ganado o perdido, se muestran los respectivos mensajes *"Has ganado"* o *"Has perdido"*. Finalmente, imprimimos el estado del muñeco para el jugador.


## Cosas por mejorar del programa

Algo que me gustaría mejorar del programa, es que almacenase las letras que ya ha dicho el jugador en una variable y que pudiera mostrar un mensaje de *"Esa letra ya la has dicho, di otra"*.



