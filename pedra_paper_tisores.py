import random

def pedra_paper_tisores_func():
    punts_jugador = 0
    punts_maquina = 0
    
    
    print("\n\nBENVINGUT/DA AL JOC DE PEDRA - PAPER - TISORES. EL PRIMER QUE ARRIBI A 3 GUNAYA!")
    while punts_jugador != 3 and punts_maquina != 3:
        llista_random = random.choice(["Pedra","Paper","Tisores"])
        resposta_user = input("\nQue vols tirar? Pedra, Paper o Tisores? ")

        if (resposta_user == "Pedra" and llista_random == "Paper"):
            print("\nLa màquina ha tret Paper. Punt per la màquina!\n\n")
            punts_maquina +=1
            print(f"RESULTATS PER ARA. PUNTS DEL JUGADOR: {punts_jugador} PUNTS DE LA MÀQUINA: {punts_maquina}\n")

        elif(resposta_user == "Pedra" and llista_random == "Tisores"):
            print("\nLa màquina ha tret Tisores. Punt per l'usuari!\n\n")
            punts_jugador +=1
            print(f"RESULTATS PER ARA. PUNTS DEL JUGADOR: {punts_jugador} PUNTS DE LA MÀQUINA: {punts_maquina}\n")

        elif(resposta_user == "Pedra" and llista_random == "Pedra"):
            print("\nLa màquina ha tret Pedra. Punt per ningu!\n\n")
            print(f"RESULTATS PER ARA. PUNTS DEL JUGADOR: {punts_jugador} PUNTS DE LA MÀQUINA: {punts_maquina}\n")

        elif(resposta_user == "Paper" and llista_random == "Pedra"):
            print("\nLa màquina ha tret Pedra. Punt per el usuari!\n\n")
            punts_jugador +=1
            print(f"RESULTATS PER ARA. PUNTS DEL JUGADOR: {punts_jugador} PUNTS DE LA MÀQUINA: {punts_maquina}\n")

        elif(resposta_user == "Paper" and llista_random == "Tisores"):
            print("\nLa màquina ha tret Tisores. Punt per la màquina\n\n")
            punts_maquina +=1
            print(f"RESULTATS PER ARA. PUNTS DEL JUGADOR: {punts_jugador} PUNTS DE LA MÀQUINA: {punts_maquina}\n")

        elif(resposta_user == "Paper" and llista_random == "Paper"):
            print("\nLa màquina ha tret Paper. Punt per ningu!\n\n")
            print(f"RESULTATS PER ARA. PUNTS DEL JUGADOR: {punts_jugador} PUNTS DE LA MÀQUINA: {punts_maquina}\n")

        elif(resposta_user == "Tisores" and llista_random == "Pedra"):
            print("\nLa màquina ha tret Pedra. Punt per la màquina\n\n")
            punts_maquina +=1
            print(f"RESULTATS PER ARA. PUNTS DEL JUGADOR: {punts_jugador} PUNTS DE LA MÀQUINA: {punts_maquina}\n")

        elif(resposta_user == "Tisores" and llista_random == "Paper"):
            print("\nLa màquina ha tret Paper. Punt per l'usuari\n\n")
            punts_jugador +=1
            print(f"RESULTATS PER ARA. PUNTS DEL JUGADOR: {punts_jugador} PUNTS DE LA MÀQUINA: {punts_maquina}\n")

        elif(resposta_user == "Tisores" and llista_random == "Tisores"):
            print("\nLa màquina ha tret Tisores. Punt per ningu\n\n")
            print(f"RESULTATS PER ARA. PUNTS DEL JUGADOR: {punts_jugador} PUNTS DE LA MÀQUINA: {punts_maquina}\n")