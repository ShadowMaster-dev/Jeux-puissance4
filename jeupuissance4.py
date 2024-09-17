import os

"""
Pour faire les test des fonctions, mettre en commentaire ceci de cette manière : 

#tab = grille_init()
#jouer(tab)

Puis enlèver les 3 apostrophes au debut des Tests et à la fin pour voir le résultat des diffèrents tests :''' 
"""
#Fonction grille_init() permet d'initaliser la grille de jeu 

def grille_init() :
    """ """
    tab = [
        ['0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0'],
        ]
    return tab

"""
    Fonction affiche_grille  affiche le contenu du tableau sous forme 
    +---+   et de | 0 |
"""
def affiche_grille(tab) :
   
    os.system('cls') 
    separateur = "+---+---+---+---+---+---+---+"
    print(separateur)
    for i in range(len(tab)) :
        ligne = "| "
        for j in range(len(tab[i])) :
            ligne = ligne + tab[i][j] + " | "
        print(ligne)
        print(separateur)
    # Fin Fonction 

"""
    Fonction colonne_libre test si une colonne j du tableau passé  et renvoie un booléen indiquant s’il
        est possible de mettre un jeton dans la colonne (indique si la colonne n’est pas
        pleine) 
"""
def colonne_libre(tab, colonne) :
    """ """
    libre = False
    for i in range(len(tab)) :
        if (colonne <= len(tab[i]) and tab[i][colonne] == '0') :
            libre = True
            break
        
    return libre
    # Fin Fonction colonne_libre 

'''
test colonne libre:

colonne=0
print("test pour la colonne 0, elle doit afficher True car la colonne est libre => " + str(colonne_libre([
        ['0','0','0','0','0','0','0'],
        ['1','0','0','0','0','0','0'],
        ['1','0','0','0','0','0','0'],
        ['1','0','0','0','0','0','0'],
        ['1','0','0','0','0','0','0'],
        ['1','0','0','0','0','0','0'],
        ],colonne)))
print("test pour la colonne 0, elle doit afficher False car la colonne est pleine => " + str(colonne_libre([
        ['1','0','0','0','0','0','0'],
        ['1','0','0','0','0','0','0'],
        ['1','0','0','0','0','0','0'],
        ['1','0','0','0','0','0','0'],
        ['1','0','0','0','0','0','0'],
        ['1','0','0','0','0','0','0'],
        ],colonne)))

'''

# Fonction place_jeton place un jeton du joueur (1 ou 2) dans la colonne) 

def place_jeton(tab, colonne, joueur) :
    """ """
    index = -1
    for i in range(len(tab)) :
        if (tab[i][colonne] == '0') : 
            index = i
    if (index > -1) :
        tab[index][colonne] = joueur
    return tab
    # Fin Fonction place_jeton 

'''
test place_jeton(tab,colonne, joueur) :

tab1=[
    ['0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0'],
    ['1','2','0','0','0','0','0'],
    ]

condition=True
while condition :
    joueur=str(input("joueur 1 ou 2 : "))
    colonne = int(input("Choisissez une colonne : "))
    place_jeton(tab1, colonne ,joueur)
    print(affiche_grille(tab1))
   

'''


#    Fonction horizontale fonction qui renvoie True si le joueur a au moins 4 jetons alignés dans une ligne ;

def horizontale(tab,joueur):
    """ """
    jetonsalignee = 0

    # on boucle sur chaque ligne
    for i in range(len(tab)) :
        if (jetonsalignee >= 4) :
            break
        #chaque ligne j'initialise a 0 le nb de jetonalignée.
        jetonsalignee = 0
        for j in range(len(tab[i])) :
            if (tab[i][j] == joueur) :
                # on cumule les jetons successifs 
                jetonsalignee = jetonsalignee + 1
            else:
            #si la dynamique est cassée on renvient à 0 
                jetonsalignee = 0
            # si on a 4 jetons d'affilé on arrête et on sort de la boucle 
            if (jetonsalignee >= 4) :
                break


    return jetonsalignee >= 4
    # Fin Fonction horizontale

'''
#test fonction horizontale :
#test avec le joueur 1
print("test 1 , ce test doit afficher True si le joueur 1 à gagner en horizontale => " + str(horizontale([
        ['0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0'],
        ['1','1','1','1','0','0','0'],
        ['0','2','0','2','2','2','2'],
        ['0','0','0','0','0','0','0'],
        ], '1')))

print("test 2 , ce test doit afficher False car  le joueur 1 n'a pas gagner en horizontale => " + str(horizontale([
        ['0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0'],
        ['1','1','1','0','0','0','0'],
        ['0','2','0','2','2','2','2'],
        ['0','0','0','0','0','0','0'],
        ], '1')))

#test avec le joueur2

print("test 1 , ce test doit afficher True si le joueur 2 à gagner en horizontale => " + str(horizontale([
        ['0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0'],
        ['1','1','1','1','0','0','0'],
        ['0','2','0','2','2','2','2'],
        ['0','0','0','0','0','0','0'],
        ], '2')))

print("test 2 , ce test doit afficher false car le joueur 2 à gagner en horizontale => " + str(horizontale([
        ['0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0'],
        ['1','1','1','1','0','0','0'],
        ['0','2','0','0','2','2','2'],
        ['0','0','0','0','0','0','0'],
        ], '2')))
'''


#    Fonction verticale fonction qui renvoie True si le joueur a au moins 4 jetons alignés dans une ligne 
"""
Pseudo code de la fonction verticale(tab, joueur):





"""
def verticale(tab, joueur):
    jetonsalignee = 0

    for col in range(len(tab[0])) :

        if (jetonsalignee >= 4) :
            break
        else : 
            jetonsalignee = 0
        for ligne in range(len(tab)) :
            if (tab[ligne][col] == joueur) :
                """ on cumule les jetons successifs  """
                jetonsalignee = jetonsalignee + 1
            else:
                """ si la dynamique est cassé on renvient à 0 """
                jetonsalignee = 0
            """ si on a 4 jetons d'affilé on arrête et on sort de la boucle """
            if (jetonsalignee >= 4) :
                break


    return jetonsalignee >= 4
    """ Fin Fonction verticale """

'''
#test fonction verticale:

#test pour le joueur 1:

print("test 1 , ce test doit afficher True si le joueur 1 à gagner en verticale  => " + str(verticale([
        ['1','0','0','0','0','0','0'],
        ['1','0','0','0','0','1','0'],
        ['1','0','0','0','0','1','0'],
        ['0','1','1','1','0','1','0'],
        ['0','2','0','2','2','1','2'],
        ['0','0','0','0','0','1','0'],
        ], '1')))

print("test 2 , ce test doit afficher false car le joueur 1 n'a pas gagner en verticale  => " + str(verticale([
        ['1','0','0','0','0','0','0'],
        ['1','0','0','0','0','0','0'],
        ['1','0','0','0','0','0','0'],
        ['0','1','1','1','0','1','0'],
        ['0','2','0','2','2','1','2'],
        ['0','0','0','0','0','1','0'],
        ], '1')))

#Test pour le joueur 2:

print("test 1 , ce test doit afficher True si le joueur 2 à gagner en verticale  => " + str(verticale([
        ['1','0','0','0','0','0','0'],
        ['1','0','0','0','0','1','0'],
        ['1','2','0','0','0','1','0'],
        ['0','2','1','1','0','1','0'],
        ['0','2','0','2','2','1','2'],
        ['0','2','0','0','0','1','0'],
        ], '2')))

print("test 2 , ce test doit afficher false car le joueur 2 n'a pas gagner en verticale  => " + str(verticale([
        ['1','0','0','0','0','0','0'],
        ['1','0','0','0','0','0','0'],
        ['1','0','0','0','0','0','0'],
        ['0','1','1','1','0','1','0'],
        ['0','2','0','2','2','1','2'],
        ['0','0','0','0','0','1','0'],
        ], '2')))
'''

#   fonction gagne qui renvoie True si le joueur a gagné ;
"""
Pseudo code de la fonction gagne(tab, joueur):



"""

def gagne(tab, joueur) :
   
    return horizontale(tab,joueur) or verticale(tab,joueur) #or diagonale(tab,joueur)
'''
#test de la fonction gagne(tab, joueur) :

#Test pour savoir si le joueur 1 à gagné( en horizontale ou en verticale):

print("test 1 , ce test doit afficher True si le joueur 1 à gagner en verticale ou en horizontale  => " + str(gagne([
        ['1','0','0','0','0','0','0'],
        ['1','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0'],
        ['1','1','1','1','0','1','0'],
        ['0','2','0','2','2','1','2'],
        ['0','0','0','0','0','1','0'],
        ], '1')))

print("test 2 , ce test doit afficher False car le joueur 1 n'a pas gagner ni en verticale ou ni en horizontale  => " + str(gagne([
        ['1','0','0','0','0','0','0'],
        ['1','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0'],
        ['0','1','1','1','0','1','0'],
        ['0','2','0','2','2','1','2'],
        ['0','0','0','0','0','1','0'],
        ], '1'))) 

#test pour savoir si le joueur 2 a gagné (en horizontale ou en verticale) :

print("test 1 , ce test doit afficher True car le joueur 2 à gagner en verticale ou en horizontale  => " + str(gagne([
        ['1','0','0','0','0','0','0'],
        ['1','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0'],
        ['1','1','1','1','0','1','0'],
        ['0','2','2','2','2','1','2'],
        ['0','0','0','0','0','1','0'],
        ], '2')))    

print("test 2 , ce test doit afficher False car le joueur 2 n'a pas gagner ni en verticale et horizontale  => " + str(gagne([
        ['1','0','0','0','0','0','0'],
        ['1','0','0','0','0','0','0'],
        ['0','0','0','0','0','0','0'],
        ['0','1','1','1','0','1','0'],
        ['0','2','0','2','2','1','2'],
        ['0','0','0','0','0','1','0'],
        ], '2'))) 
'''


"""
    tour_joueur(tab,joueur) : fonction qui permet au joueur de placer un jeton
    dans la colonne choisie. Elle indique si la colonne est pleine et permet alors au
    joueur de choisir une autre colonne ;
"""
"""
Pseudo code de la fonction tour_joueur(tab,joueur):




"""
def tour_joueur(tab,joueur) :
    """ """
    affiche_grille(tab)
    print("Joueur " + joueur + " joue")
    choixfait = False
    while choixfait == False :
        colonne = int(input("Choisie une colonne : "))
        if (colonne_libre(tab, colonne)) : 
            place_jeton(tab, colonne , joueur)
            choixfait = True
        else :
            print("faites un autre choix la colonne n'est pas libre du joueur")

"""
    fonction qui renvoie True s’il y a égalité et False sinon ;
"""
"""
Pseudo code de la fonction egalite(tab):




"""
def egalite(tab):
   
   return gagne(tab,"1") == gagne(tab, "2")

"""
Pseudo code de la fonction jouer(tab):

"""
def jouer(tab) :
    """ """
    finJeu = False
    while finJeu == False :
        finJeu == True 
        tour_joueur(tab, '1')  
       
        tour_joueur(tab, '2')  

        """ Si un joueur gagne on arrête de jouer"""
        if(gagne(tab, '1') or gagne(tab, '2')):
            break
        
        """ Si des colonnes sont librent on continue a jouer : finJeu == False  """
        for colonne in range(len(tab[0])) :
            if (colonne_libre(tab, colonne)):
                finJeu == False 

    """ Affichage du resultat final """
    affiche_grille(tab)
    if (egalite(tab)):
        print("Egalité entre les deux joueurs ")
    elif(gagne(tab, "1")):
        print("Joueur 1 a gagné")
    else:
        print("Joueur 2 a gagné")
    print("Fin de jeu")


tab = grille_init()
jouer(tab)

