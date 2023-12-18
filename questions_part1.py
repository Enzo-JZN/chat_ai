from calculs import *

#################################################################################
# Fichier qui comprend les fonctions pour répondre aux questions de la partie 1 #
#################################################################################


###############################################
### Question 1 Affichage valeur TF-IDF == 0 ###
###############################################

# Fonction qui cherche les mots les moins importants et les renvois
# Partie 1
def calcul_mot_dit_nn_important():
    # Appel de la fonction TF_IDF pour obtenir la matrice
    valeur_tf_idf = TF_IDF("cleaned")
    L = []

    # On fait une boucle où i va aller piocher des tuples des cles et des valeurs de la liste
    for i in valeur_tf_idf.items():
        addition = 0
        for somme in i[1]:
                addition += somme
        if addition == 0:
            L.append(i[0])
    return (L)


# Partie 2
# 1 Afficher la liste des mots les moins importants dans le corpus de documents.
def mot_moins_important():
    liste_mot_non_important = []
    for i in res.items():
        nb = 0
        for values in i[1]:
            nb += values
        if nb <= 0.5:
            liste_mot_non_important.append(i[0])
    return ("la liste des mots les moins importants dans tous les documents sont: ", liste_mot_non_important)


#############################################################################
### Question 2 Afficher le(s) mot(s) ayant le score TF-IDF le plus élevé ###
############################################################################

# C'est une fonction qui cherche les mots ayant le score TF-IDF le plus élevé
# Retourne ces mêmes mots
def score_IDF_eleve():
    # Initialisation d'une liste pour stocker les mots et leurs valeur TF_IDF
    liste = []

    # Parcours la matrice TF_IDF
    for i in res.items():
        nb = 0
        # Calcul la somme des scores TF_IDF et les ajoutes à la liste
        for values in i[1]:
            nb += values
        liste.append([i[0], nb])
    # Stocke le mot avec le score le plus élévée
    max = ["", 0]

    # Cherche le mot avec le score le plus élevé
    for a in liste:
        if max[1] < a[1]:
            max = a

    # Initialise une liste si des mots on le meme score
    # Puis cherche si des mots ont le meme score max et les ajoutent à la liste
    liste_mot_iDF_egaux = [max[0]]
    for a in liste:
        if a[1] == max[1] and a[0] != max[0]:
            liste_mot_iDF_egaux.append(a[0])
    # Renvoie les mots avec le score le plus élevé
    return liste_mot_iDF_egaux



###########################################################################
### Question 3 Indiquer le mot le plus utilisé par le predident chirac ###
##########################################################################

# On crée une fonction pour trouver le(s) mot(s) le(s) plus répété(s) par le président Chirac.
# Et retourne la liste des mots qu'il a le plus prononcés
def indiquer_le_mot_plus_utilise(president):
    # On donne le chemin pour acceder au fichier qui contiennent le nom du president recherche
    directory = './cleaned'
    files_names = list_of_files(directory, "txt")

    # On créera un liste max qui prendra pour valeur le mot avec le plus d'occurences, on l'initialise à 0, 0. car on mettra en premier
    # le mot puis son occurence
    max = [0, 0]
    contenu = ""

    # On fait une boucle des fichiers pour obtenir le contenu (chaine de caractère) de tous les fichiers réunis qui correspondent
    # à ceux dont l'auteur est Chirac.
    for i in files_names:
        if president in i:
            with open(directory + '/' + i, 'r', encoding="utf-8") as fichier:
                contenu += fichier.read() + " "

    # On utilise la fonction TF qui correspond à occurences_chaines(chaine) pour avoir un dico de chaque mot et de leur occurence
    dico = occurences_chaines(contenu)
    for a in dico.items():
        # on cherche le mot avec la plus grande occurence et on l'ajoutera dans max
        if max[1] < a[1] and a[0] != '':
            max = a

    # on verfie si il y a plusieurs mots qui ont la même occurence que max, si oui on les ajoutera dans la liste
    liste_mot = [max]
    for j in dico.items():
        if max[1] == j[1]:
            if max[0] != j[0]:
                liste_mot.append(j[0])
    return liste_mot



################################################################
### Question 4 les présidents ayant abordé le thème nation. ###
###############################################################
#Cette fonction cherche les présidents qui ont parlé de la "Nation" et renvoit la liste de ceux qui en ont parlé
def president_nation():
    # Initialisation d'une liste et d'un dico
    listes_president = []
    dico_occ_nation = {}
    max_occ_nation = [0, 0]
    # On fait une boucle où i prendra le nom des présidents et on utilisera ensuite read et split pour avoir une
    # chaine et une liste des mots
    for i in files_names:
        with open("./cleaned/" + "/" + i, 'r', encoding="utf-8") as fichier:
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
            "et celui qui l'a répèté le plus de fois est :", max_occ_nation[0])




################################################################################
### 5. Indiquer les présidents qui ont parler du climat et/ou de l’écologie ###
###############################################################################

# Dictionnaire brut avec les noms des présidents et leurs dates d'élection
presidents_et_dates = {
    "Giscard dEstaing": 1974,
    "Mitterrand": 1981,
    "Chirac": 1995,
    "Sarkozy": 2007,
    "Hollande": 2012,
    "Macron": 2017
}


# La fonction suivante recherche la liste des présidents qui ont abordé en premier les sujets liés au climat, à l'écologie
# ou au réchauffement dans les discours et renvoie cette liste.

def climat_president():
    # Obtient la liste des noms de fichiers dans le répertoire "cleaned"
    files_names = list_of_files("./cleaned", "txt")
    liste_president = []

    # Parcourt chaque fichier, lit et divise chaque fichier en mots
    for i in files_names:
        with open("./cleaned/{}".format(i), 'r', encoding="utf-8") as fichier:
            contenu = fichier.read()
            texte_mot_cleaned = contenu.split()
            # Obtient le nom du président à partir du nom du fichier
            nom_president = (i[11:-4])

            # Si le nom président se termine par un chiffre, supprime ce chiffre
            if nom_president[-1] >= chr(48) and nom_president[-1] <= chr(57):
                nom_president = nom_president[:-1]

            # Vérifie si des termes liés au climat, à l'écologie ou au réchauffement sont présents dans le texte
            if ("ecologie" in texte_mot_cleaned) or ("climat" in texte_mot_cleaned) or ("réchauffement" in texte_mot_cleaned) or ("écologique" in texte_mot_cleaned) or ("ecolo" in texte_mot_cleaned):

                # Ajoute le nom du président à la liste s'il a parlé de l'écologie et s'il n'est pas déjà présent
                if not (nom_president in liste_president):
                    liste_president.append(nom_president)

    # On met un choix multiple pour couvrir toutes les options
    # Si aucun président n'a abordé ces sujets, retourne "aucun"
    if liste_president == []:
        return "aucun"
    # Sinon renvoit les présidents qui en ont parlé
    else:
        return liste_president

