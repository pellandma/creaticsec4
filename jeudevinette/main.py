# TP2 jeu de devinettes

import random

x = random.randint(0, 100)
nb_essai = 0

def JeuDeDevinette():


    print("j'ai choisi un nombre entre 0 et 100." "\nA vous de deviner: ")

    essai = int(input())


    if essai < x:
        print("Mauvaise reponse, c'est plus haut")
        nb_essai = + 1
        JeuDeDevinette()

    if essai > x:
        print('mauvaise reponse, elle est plus basse ')
        nb_essai = + 1
        JeuDeDevinette()

    if essai == x:
        print("Bravo! Bonne reponse, vous avez reussi en: ", nb_essai)

        quit = input("voulez vous quitter: y/n\n")
        if quit == "y":
            print("merci et au revoir")
        if quit == "n":
            JeuDeDevinette()


JeuDeDevinette()
