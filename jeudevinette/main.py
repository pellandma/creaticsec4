# TP2 jeu de devinettes

import random





def JeuDeDevinette():
    boundarie1 = int(input("Plus petit nombre"))
    boundarie2 = int(input("Plus Grand nombre"))
    nb_essai = 0
		
    x = random.randint(boundarie1, boundarie2)


    print("J'ai choisi un nombre entre ", boundarie1,"et ", boundarie2, "\nA vous de deviner: ")
    essai = None
    
    while x != essai:
      nb_essai += 1
      essai = int(input())
      if essai < x:
	  	
	        print("Mauvaise reponse, c'est plus haut")
	        
	        
	
      if essai > x:
	        print('mauvaise reponse, elle est plus basse ')
	        
	        

    if essai == x:
        print("Bravo! Bonne reponse, vous avez reussi en: ", nb_essai)

        quit = input("voulez vous quitter: y/n\n")
        if quit == "y":
            print("merci et au revoir")
        if quit == "n":
            JeuDeDevinette()


JeuDeDevinette()
