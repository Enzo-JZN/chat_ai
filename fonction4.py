################################################################
### Question 4 les présidents ayant abordé le thème nation. ###
###############################################################

def president_nation():
    # Initialisation d'une liste et d'un dico
    listes_president = []
    dico_occ_nation = {}

    # On fair une boucle où i prendra le nom des présidents et on utilisera ensuite read et split pour avoir une
    # chaine et une liste des mots
    for i in files_names:
        with open("./cleaned/" + "/" + i, 'r') as fichier:
            contenu = fichier.read()
            liste_mot = contenu.split()

        # Si le nom président du président fini par un chiffre, on supprime alors ce chiffre
        nom_president = (i[11:-4])
        if nom_president[-1] >= chr(48) and nom_president[-1] <= chr(57):
            nom_president = nom_president[:-1]

        # On verfie la presence du mot "nation" à l'interieur de la liste
        if "nation" in liste_mot:

            # On utilsie la foncton TF pour avoir un dico de chaque mot et de leur occurence.
            dico_mot_fichier = occurences_chaines(contenu)

            # On ajoute le nom du president dans la liste s'il n'est pas déja present
            if not (nom_president in listes_president):
                listes_president.append(nom_president)

            # On cherche leur occurence dans le dico initial et on l'ajoute à la valeur actuelle
            if (nom_president in dico_occ_nation.keys()):
                dico_occ_nation[nom_president] += dico_mot_fichier["nation"]

            # Si president n'est pas une clé du dico, alors on la met et on definit sa valeur
            if not (nom_president in dico_occ_nation.keys()):
                dico_occ_nation[nom_president] = dico_mot_fichier["nation"]

        # On cherche à obtenir l'occurence max et celui qui est à l'origine de cette parole
        max_occ_nation = [0, 0]
        for i in dico_occ_nation.items():
            if max_occ_nation[1] < i[1]:
                max_occ_nation = i

    # Affichage
    return ("Les presidents qui ont répété le mot « Nation » sont", listes_president,
            "et celui qui l'a repete le plus de fois est :", max_occ_nation[0])


# print(president_nation())
