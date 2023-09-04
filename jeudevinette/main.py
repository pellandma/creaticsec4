#TP2 jeu de devinettes

import random

def JeuDeDevinette():
    
    nb_essai = 0
    x = random.randint(0, 100)
    print("j'ai choisi un nombre entre 0 et 100." "\nA vous de deviner: ")

    essai = int(input())
    nb_essai + 1 

    if essai < x:
        print("Mauvaise reponse, c'est plus haut")

    if essai > x:
        print('mauvaise reponse, elle est plus basse ')
        
    if essai == x:
        print("Bravo! Bonne reponse, vous avez reussi en: ", (nb_essai)) 
        

        quit = input("voulez vous quitter: y/n\n")
        if quit == "y":
            print("merci et au revoir")
        if quit == "n":
            JeuDeDevinette()
JeuDeDevinette()
