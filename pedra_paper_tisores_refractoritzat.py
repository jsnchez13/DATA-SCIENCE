import random

def pedra_paper_tisores_func2():
    punts_maquina = 0
    punts_jugador = 0
    
    
    print("\n\nBENVINGUT/DA AL JOC DE PEDRA - PAPER - TISORES. EL PRIMER QUE ARRIBI A 3 GUNAYA!")
    
    while punts_jugador != 3 and punts_maquina != 3:
        resposta_user = int(input("Selecciona (1. Pedra, 2. Paper, 3. Tisores): "))
        ia = random.randint(1,3)
        if (resposta_user == ia):
            print("Empat")
            print(f"La IA ha tret {ia}")
            print(f"RESULTATS PER ARA. PUNTS DEL JUGADOR: {punts_jugador} PUNTS DE LA MÀQUINA: {punts_maquina}\n")
        elif(resposta_user == 1 and ia == 2 or ia == 3):
            print("Punt per el user")
            print(f"La IA ha tret {ia}")
            punts_jugador += 1
            print(f"RESULTATS PER ARA. PUNTS DEL JUGADOR: {punts_jugador} PUNTS DE LA MÀQUINA: {punts_maquina}\n")
        elif(resposta_user == 2 and ia == 1 or ia == 3):
            print("Punt per el user")
            print(f"La IA ha tret {ia}")
            punts_jugador += 1
            print(f"RESULTATS PER ARA. PUNTS DEL JUGADOR: {punts_jugador} PUNTS DE LA MÀQUINA: {punts_maquina}\n")
        elif(resposta_user == 3 and ia == 1 or ia == 2):
            print("Punt per el user")
            print(f"La IA ha tret {ia}")
            punts_jugador += 1
            print(f"RESULTATS PER ARA. PUNTS DEL JUGADOR: {punts_jugador} PUNTS DE LA MÀQUINA: {punts_maquina}\n")
        else:
            print("Punt per la IA")
            print(f"La IA ha tret {ia}")
            punts_maquina += 1
            print(f"RESULTATS PER ARA. PUNTS DEL JUGADOR: {punts_jugador} PUNTS DE LA MÀQUINA: {punts_maquina}\n")

pedra_paper_tisores_func2()