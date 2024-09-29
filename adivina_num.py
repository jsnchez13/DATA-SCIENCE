import random

def adivina_el_numero():
    intents = 3
    num_aleatori = random.randrange(1,10)

    print("\n\nBENVINGUT/DA AL JOC D'ADIVINAR EL NUMERO ALEATORI. TENS 3 INTENTS!")

    while intents != 0:
        num_user = int(input("\nDona'm un número per adivinar: "))
        if num_user < num_aleatori:
            print("El numero proporcionat es menor al numero aleatori")
            intents -= 1
        elif num_user > num_aleatori:
            print("El numero proporcionat es major al numero aleatori")
            intents -= 1
        elif num_aleatori == num_user:
            print("Has encertat el numero secret!")
            break