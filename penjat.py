import random

def llegir_paraula_random():

    ### LLEGIR EL FITXER ###
    with open ("paraules.txt") as fitxer:
        paraules = fitxer.read().splitlines()
        paraula_secreta = random.choice(paraules)

    ### AGAFAR UNA PARAULA I AMAGAR LES LLETRES ###
    num_a_revelar = 1        
    llarg_paraula = list(range(len(paraula_secreta)))
    posicions_revelades = random.sample(llarg_paraula,num_a_revelar)
    
    
    paraula_mostrada = ""
    for i in range(len(paraula_secreta)):
        if i in posicions_revelades:
            paraula_mostrada += paraula_secreta[i]
        else:
            paraula_mostrada += "_"
            
    print(paraula_mostrada)
    
    ### DEMANAR AL USUARI UNA LLETRA I POSAR-LA A LA PARAULA SI COINCIDEIX ###
    num_caracteers_paraula = len(paraula_secreta)
    intents = num_caracteers_paraula*2
    nova_paraula_mostrada = ""
    print(f"Total de intents {intents}")
    
    
    while intents != 0:
        lletres = input("Dona'm una lletra: ")
        for j in range(len(paraula_secreta)):
            if paraula_secreta[j] == lletres or paraula_mostrada[j] != "_":
                nova_paraula_mostrada += paraula_secreta[j]
                print(nova_paraula_mostrada)
            else:
                nova_paraula_mostrada += "_"
                intents -= 1
        
    
            
llegir_paraula_random()