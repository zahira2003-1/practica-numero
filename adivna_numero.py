import random
numero_secreto = random.randint(1, 50)
intentos = 0

while intentos < 5:
    numero_jugador = int(input("Tenes que adivinar el numero secreto: "))
    intentos += 1

    if numero_jugador == numero_secreto:
        print("🎉 ¡Felicitaciones! Adivinaste el número.")
        break
    elif numero_jugador < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")

if numero_jugador != numero_secreto:
    print(f" ¡Perdiste!  El número era {numero_secreto}.") 

