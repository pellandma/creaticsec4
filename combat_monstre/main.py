import random
import time
#VARIABLES
numero_combat = 0
D = random.randint(0,6) * 2
niveau_vie = 20
Force_adversaire = random.randint(1,5) * 2
WinCounter = 0
Force_boss = random.randint(3,5)
#FUNCTIONS



def Boss():

    global niveau_vie
    global WinCounter
    global numero_combat
    numero_combat   += 1    
    
    if D >= Force_boss:
        print("Le Boss a ete tuer")
        niveau_vie = niveau_vie + Force_boss
        WinCounter += 1
    
    
    if D < Force_boss:
        print("Vous avez rouler un ", D, ", Le Boss est plus fort que vous!")
        niveau_vie = niveau_vie - Force_boss
        print("\nIl vous reste", niveau_vie)
        WinCounter -= 1
        if niveau_vie == 0:
            print("You lose")
            quit()





def dodge():
    global niveau_vie
    niveau_vie -= 1
    print(niveau_vie)



def fight():
    global niveau_vie
    global WinCounter
    global numero_combat
    numero_combat   += 1    
    
    if D > Force_adversaire:
        print("Vous avez rouler un ", D, ", L'adversaire a ete tuer!")
        niveau_vie = niveau_vie + Force_adversaire
        WinCounter += 1
    
    
    if D <= Force_adversaire:
        print("Vous avez rouler un ", D, ", L'adversaire est plus fort que vous!")
        niveau_vie = niveau_vie - Force_adversaire
        print("\nIl vous reste", niveau_vie)
        WinCounter -= 1
        if niveau_vie == 0:
            print("You lose")
            quit()


def CombatMonstre():

    global niveau_vie
    

    print("Vous tombez face à face avec un adversaire de difficulté : ",Force_adversaire)

    choix = int(input("\nQue voulez-vous faire ? \n1- Combattre cet adversaire\n2- Contourner cet adversaire et aller ouvrir une autre porte\n3- Afficher les règles du jeu\n4- Quitter la partie\n"))

    if choix == 1:
        fight()
        print("Force de l'Adversaire : ", Force_adversaire, "\nTon niveau de vie: ", niveau_vie, "\nCombat #",numero_combat, "\nparti Gagner: ", WinCounter)
        if WinCounter % 3 == 0:
            Boss()
        time.sleep(5)
        CombatMonstre()
    
    if choix == 2:
        dodge()
        CombatMonstre()

    if choix == 3:
        print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l'adversaire.  Dans ce cas, le niveau de vie de l'usager est augmenté de la force de l'adversaire. Une défaite a lieu lorsque la valeur du dé lancé par l'usager est inférieure ou égale à la force de l'adversaire.  Dans ce cas, le niveau de vie de l'usager est diminué de la force de l’adversaire.\nLa partie se termine lorsque les points de vie de l’usager tombent sous 0.\nL’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")
        CombatMonstre()

    if choix == 4:
        print("Merci et au revoir... ")



CombatMonstre()
        
