import signal
import random

def handler(signal, frame):
    print("¡ADIOS!")
    exit(0)

    signal.signal(signal.SIGINT, handler)

def numero_aleatorio():
    n_intentos = 0
    numero_aleatorio = random.randint(0,100)

    while True:
        try:
            n_intentos += 1     
            numero_ingresado = int(input("Adivina el número entre el 1 y el 100: "))

            if (numero_aleatorio > numero_ingresado):
                print(f"El número secreto es mayor que: {numero_ingresado}")
                print(f"Llevas {n_intentos} intentos")
            elif (numero_aleatorio < numero_ingresado):
                print(f"El número secreto es menor que: {numero_ingresado}")
                print(f"Llevas {n_intentos} intentos")
            elif (numero_aleatorio == numero_ingresado):
                print("¡Felicidades has acertado el numero secreto!")
                pregunta = input("¿Quieres jugar de nuevo? (s/n)")
                n_intentos = 0

                if (pregunta != 's'):
                    print("¡ADIOS!")

                    break

        except KeyboardInterrupt:
            print("\n¡ADIOS!")
            break

numero_aleatorio()