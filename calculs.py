import math
from gestion_fichiers import *

################################################################################################################
### Le fichier calculs.py contient l'ensemble des fonctions qui gèrent les calculs dont le chatBot a besoin ###
################################################################################################################

# Écrire une fonction qui prend en paramètre le répertoire où se trouve l’ensemble des fichiers du corpus
# et qui retourne un dictionnaire associant à chaque mot son score IDF.

def IDF_par_fichier(repertoire):
    directory = './{}'.format(repertoire)  # "/Users/enzojuzyna/Downloads/projet/speeches"
    files_names = list_of_files(directory, "txt")
    if len(files_names) == 0:
        print("Fichers introuvables dans {}".format(directory))
        exit()


    # on va créer une liste qui va contenir tous les mots présents dans les textes du répertoire en un seul exemplaire
    contenu = ""
    liste_contenu = []
    for i in files_names:
        with open(directory + '/' + i, 'r', encoding="utf-8") as fichier_IDF:
            contenu = fichier_IDF.read()
            contenu = contenu.split()
            liste_contenu += contenu
        set_contenu = set(liste_contenu)
    dico = {}

    # remplacer liste contenue par les mots dans le dico

    # parcours la liste de mots et compte le nombre d'occurence pour ensuite calculer le score IDF
    for mot in set_contenu:
        occurence = 0
        for i in files_names:
            with open('./{}/{}'.format(repertoire, i), 'r', encoding="utf-8") as fichier_IDF :
                contenu = fichier_IDF.read()
                contenu = contenu.split()
                if mot in contenu:
                    occurence += 1
        calcul_idf = math.log10((len(files_names) / occurence))
        dico[mot] = calcul_idf

    return dico

a = IDF_par_fichier("cleaned")


# Fonction qui cherche la valeur TF-IDF de chaque mot et retourne un dictionnaire reliant le mot et sa valeur

def TF_IDF(repertoire):
    # Initialisation d'un dictionnaire pour stocker la matrice TF-IDF, d'un dico pour recevoir la valeur de chaque mot et son idf,
    # ansi la récuparation du chemin et de la liste des noms du fichier
    dico_TF_IDF = {}
    dico_IDF = IDF_par_fichier(repertoire)
    directory = './{}'.format(repertoire)
    files_names = list_of_files(directory, "txt")

    # On fait une boucle sur chaque mot du dictionnaire
    for mot in list(dico_IDF.keys()):
        resultat_TF_IDF = []

        # on fait une seconde boulce sur le nom des fichiers
        for i in files_names:

            # Ouverture du fichier en mode lecture
            with open("./cleaned/{}".format(i), "r", encoding="utf-8") as fichier1:

                # On cherche à obtenir une liste de tous les mots
                contenu = fichier1.read()
                contenu_mot = contenu.split()

            valeur_TF = 0
            # Vérification si le mot est présent dans le contenu du fichier, pout optimiser, gagner en vitesse, si le mot n'est pas
            # dans la liste, on ne cherche pas à chercher à l'occurence
            if (mot in contenu_mot) == True:
                # Fonction TF nn optimisée trop longue, changement de méthode
                # valeur_TF = occurences_chaines(texte1)
                # valeur_TF_valeur = resultat_TF_IDF[mot]
                for i in contenu_mot:
                    if mot == i:
                        valeur_TF += 1

            # Si mot pas dans le contenue, alors son TF = 0
            else:
                valeur_TF = 0

            # On calcul TF_IDF, en multipliant la valeur TF par son IDF
            resultat_TF_IDF.append(valeur_TF * dico_IDF[mot])

        # On l'ajoute dans la matrice qu'on a décidé de définir sous forme de dictionnaire.
        dico_TF_IDF[mot] = resultat_TF_IDF
    return dico_TF_IDF


# On teste la fonction avec le répertoire cleaned.
res = TF_IDF("cleaned")


# Fonction qui cherche la valeur TF-IDF de chaque mot pour chquque documents
# Et retourne un dictionnaire le nom du document et son propre dictionnaire des valeurs TF-IDF des mots qu'il contient


def TF_IDF_par_doc():
    # On appel les fonctiosn et on créé les variables nécessaires à cette fonction
    files_names = list_of_files("./cleaned", "txt")
    dico_TF_IDF = TF_IDF("cleaned")
    liste_contenu = {}
    dico_IDF = IDF_par_fichier("cleaned")
    # On fait une boucle qui va séparer le contenu de chaques document dans un dico
    for i in files_names:
        with open(directory + '/' + i, 'r', encoding="utf-8") as fichier_IDF:
            contenu = fichier_IDF.read()
            contenu1 = contenu.split()
            set_mot = set(contenu1)

        dico_occ = occurences_chaines(contenu)
        dico_fichier = {}
        # On fait une boucle pour mettre dans un dico le vecteur TF_IDF de chaque mots dans chaque fichier
        for j in dico_TF_IDF:
            if j in set_mot:
                dico_fichier[j] = dico_occ[j] * dico_IDF[j]
            else:
                dico_fichier[j] = 0
        liste_contenu[i] = dico_fichier
    # Renvoit un dictionnaire qui a en clé le nom du document et en valeurs un dictionnaire
    # des valeurs TF_IDF du document
    return liste_contenu
