import adivina_num
import pedra_paper_tisores
import penjat

def menu():
    print("SELECCIÓ DE JOCS:\n")

    seleccio_user = int(input("1. Adivina el número\n2. Pedra - Paper - Tisores\n3. Penjat\n\nDona'm el numero del joc a jugar: "))
    if(seleccio_user == 1):
        adivina_num.adivina_el_numero()
    elif(seleccio_user == 2):
        pedra_paper_tisores.pedra_paper_tisores_func()
    elif(seleccio_user == 3):
        penjat.llegir_paraula_random()

menu()