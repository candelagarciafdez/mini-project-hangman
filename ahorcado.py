#Importamos random para buscar palabras de manera aleatoria
import random
from dibujos_ahorcado import ahorcado_paso

#Lista de palabras que el programa puede elegir para que la adivinemos
lista_palabras = ["perro", "gato", "python", "programacion", "ahorcado", "juego", "ordenador", "IronHack", "consola", "terminal", "ubuntu", "funciones", "jupyter"]

#Creamos una función que busca una palabra de manera aleatoria en nuestra lista
palabra = random.choice(lista_palabras)
#Asignamos espacios en blanco por cada letra que contenga la palabra
huecos = ["_" for letra in palabra]
#Iniciamos el contador de fallos a cero
fallos = 0
#Cuando la palabra contiene todas las letras, se llega a la solución
solucion = [letra for letra in palabra]

#Creamos una función que nos imprima cómo está el muñeco según el número de fallos mediante los índices que nos dan los fallos, imprimimos la lista explotada de huecos separada por espacios
def print_estado():
    print(ahorcado_paso[fallos])
    print(*huecos, sep = " ")
   
#Inicializamos la victoria como False
victory = False
print_estado()
#Mientras el jugador no haya ganado o los fallos sean menores que cero nos sigue pidiendo letras y las pasa a minúsculas
while not victory or fallos <6:
    letrajugador = input ("Introduce una letra: ")
    letrajugador = letrajugador.lower()
    #Inicializamos es_fallo como verdadero
    es_fallo = True
    #Si la letra que introduce el jugador está dentro de la palabra, se rellenan esos huecos y es_fallo es falso.
    for i,letra in enumerate(palabra):
        if letrajugador == letra:
            huecos[i] = letrajugador
            es_fallo = False
    #Cuando el jugador falla se agrega un fallo a fallos, cuando llega a 6, sale del bucle        
    if es_fallo:
        fallos += 1
        if fallos == 6:
            break
    #Cuando el número de huecos está relleno y es igual a la solución, el jugador gana y se sale del bucle
    if huecos == solucion:
        victory = True   
        break     
   
    #Imprime el estado del muñeco
    print_estado()
#Da un mensaje al jugador de si ha ganado o no
if victory:
    print("Has ganado")
    print(*huecos, sep = " ")
else:
    print("Has perdido")
    print_estado()




