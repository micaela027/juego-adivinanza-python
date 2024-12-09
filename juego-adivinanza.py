

import random


numero_secreto = random.randint(1,99)
cant_intentos = 0
cant_max_intentos = 5
adivinado = False


print ("¡Bienvenido al juego de adivinar el numero secreto!")
while not adivinado:
    if not cant_intentos < cant_max_intentos:
        print("¡Game over! No has podido adivinar el número")
        break
    entrada = input("Introduce un numero del 1 al 99: ") 
    numero = int(entrada)

    if numero == numero_secreto:
        adivinado = True
        print("¡Felicitaciones! has adivinado el numero secreto")
        
    elif numero < numero_secreto:
        print("El numero es mayor al ingresado")
    else:
        print("El numero es menor al ingresado")
    cant_intentos += 11