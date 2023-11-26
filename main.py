import os
import math

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return sorted(files_names)


# Call of the function
directory = "./speeches"
files_names = list_of_files(directory, "txt")
# print(files_names)
print()


# Extraire les noms des présidents à partir des noms des fichiers texte fournis ;
def extract_president_names(file):
    liste = set()
    president_names = set()  # Utilisez un ensemble pour éviter les doublons
    # on fait une première boucle pour mettre dans une liste tous les présidents avec leurs numéros
    # permettant d'enlever leurs type et +
    for i in files_names:
        president_names.add(i[11:-4])

    # on fait 2 boucles pour accéder à chaque caractère et ainsi supprimer les doublons
    for i in president_names:
        # on va créer une liste où on traitera chaque president à part, en utilisant leur table ascii pour
        # déterminer leur type
        vrai_prenom = []
        for j in range(len(i)):

            # on vérifie la condition qui dit que le caractère n'est pas un nombre
            if ord(i[j]) < 48 or ord(i[j]) > 57:
                continue
            else:
                vrai_prenom.append(i[:j])

        # si elle ne possède pas de numéro, on l'ajoute dans liste pour ensuite être copier dans le set
        if vrai_prenom == []:
            vrai_prenom.append(i)
        liste.add(vrai_prenom[0])  # pour changer la liste en mot
    return liste


# print(extract_president_names(files_names))

# Associer à chaque président un prénom
dico = {"Giscard dEstaing": "Valéry", "Macron": "Emmanuelle", "Mitterrand": "François", "Sarkozy": "Nicolas",
        "Chirac": "Jacques", "Hollande": "François"}


def president_prenom(x):
    return (dico[x])

# Afficher la liste des noms des présidents (attention aux doublons) ;
# print(extract_president_names(files_names))


# convertir texte en miniscules + creation repertoire cleaned + copier contenue dans le nouveau repertoire
def convertir_textes_miniscules():
    # on trouve le chemin pour acceder à speeches et ensuite on obtient la liste files.names
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")

    # on trouve le chemin pour acceder à cleaned, nouveau repertorie
    directory_cleaned = "./cleaned"

    # Vérifiez si le répertoire n'existe pas déjà, puis créez-le
    # if not os.path.exists(directory_cleaned):
    os.makedirs(directory_cleaned, exist_ok=True)

    # On va acceder au nom des fichiers pour trouver leurs chemins
    for i in files_names:
        # On crée le chemin et le noveau nom du fichier copier
        chemin_cleaned = directory_cleaned + "/" + i
        chemin_cleaned = directory_cleaned + "/" + i

        # On crée le fihcier copier, puis on copie le contenu du premier fihcier et on le rajoute le tout en miniscule
        with open(chemin_cleaned, "w") as fichier:
            fichier2 = open(directory + "/" + i, "r")
            contenu = fichier2.read()
            fichier.write(contenu.lower())


def supprimer_ponctuation():
    # trouve le chemin d'accés des fichiers à nettoyer
    directory = "./cleaned"
    files_names = list_of_files(directory, "txt")
    # on fait une boucle qui ouvre chaque fichier du répertoire un par un et on met le texte dans une variable
    for nom_fichier in files_names:
        with open(directory + "/" + nom_fichier, "r") as fichier:
            contenu = fichier.read()
        indice = []
        # dans une liste on met toutes les positions où il y a un signe de ponctuations
        for i in range(len(contenu)):
            if (ord(contenu[i]) >= 21 and ord(contenu[i]) <= 47) or (
                    ord(contenu[i]) >= 58 and ord(contenu[i]) <= 64) or (contenu[i]) == "\n":
                indice.append(i)
        n = 0
        contenu1 = ""
        # on fait une boucle qui va copier le contenue du texte jusqu'à la postion d'une ponctuation et remplace cette
        # ponctuation par un espace et cela jusqu'à la fin du texte
        for i in indice:
            contenu1 = contenu1 + contenu[n:i] + " "
            n = i + 1
        # reécrit le nouveau texte sans la ponctuation
        with open(directory + "/" + nom_fichier, "w") as fichier_modifie:
            fichier_modifie.write(contenu1)


convertir_textes_miniscules()
supprimer_ponctuation()


# Écrire une fonction qui prend en paramètre une chaine de caractères et qui retourne un dictionnaire
# associant à chaque mot le nombre de fois qu’il apparait dans la chaine de caractères
def occurences_chaines(chaine):
    indice = []
    dico = {}
    liste_mot = []

    # On fait une boucle pour obtenir tous les indices où se trouvent de signes de ponctuation
    for i in range(len(chaine)):
        if (ord(chaine[i]) >= 21 and ord(chaine[i]) <= 47) or (ord(chaine[i]) >= 58 and ord(chaine[i]) <= 64) or (
                chaine[i]) == "\n":
            indice.append(i)

    # On utlisera les indices precedemment acquis pour effectuer des slides dans la chaine de caractere initial et
    # ainsi copier les mots.
    n = 0
    for i in indice:
        liste_mot.append(chaine[n:i])
        n = i + 1

    # On fera une double boucle pour compter le nombre d'occurences de chaque mot tout en créant un dictionnaire
    for i in liste_mot:
        occurences = 0
        for j in liste_mot:
            if i == j:
                occurences += 1
        dico[i] = occurences
    return dico


# print(occurences_chaines("Écrire une fonction qui prend en paramètre une chaine de caractères
# et qui retourne un dictionnaire associant à chaque mot le nombre de fois qu’il apparait dans
# la chaine de caractères."))

# Écrire une fonction qui prend en paramètre le répertoire où se trouve l’ensemble des fichiers du corpus
# et qui retourne un dictionnaire associant à chaque mot son score IDF.

def IDF_par_fichier(repertoire):
    directory = './{}'.format(repertoire)  # "/Users/enzojuzyna/Downloads/projet/speeches"
    files_names = list_of_files(directory, "txt")
    # on va créer une liste qui va contenir tous les mots présents dans les textes du répertoire en un seul exemplaire
    contenu = ""
    liste_contenu = []
    for i in files_names:
        with open(directory + '/' + i, 'r') as fichier_IDF:
            contenu = fichier_IDF.read()
            contenu = contenu.split()
            liste_contenu += contenu
    set_mot = set(liste_contenu)
    # On crée un dico qui va contenir tous les mots ainsi que leurs IDF
    dico = {}
    # Pour chaque mot on va vérifier s'il se trouve dans un document et pour chaque document on va ajouté +1 à un compteur
    # afin de pourvoir calculer l'IDF
    for mot in set_mot:
        occurence = 0
        for i in files_names:
            with open(directory + '/' + i, 'r') as fichier_IDF:
                contenu = fichier_IDF.read()
                if mot in contenu:
                    occurence += 1
        calcul_idf = math.log10((len(files_names) / occurence) + 1)
        dico[mot] = calcul_idf
    return dico


a = IDF_par_fichier("cleaned")


# Fonction TF_IDF

def TF_IDF(repertoire):
    # Initialisation d'un dictionnaire pour stocker la matrice TF-IDF, d'un dico pour recevoir la valeur de chaque mot et son idf,
    # ansi la récuparation du chemin et de la liste des noms du fichier
    matrice_TF_IDF = {}
    dico_IDF = IDF_par_fichier(repertoire)
    directory = './{}'.format(repertoire)
    files_names = list_of_files(directory, "txt")

    # On fait une boucle sur chaque mot du dictionnaire
    for mot in list(dico_IDF.keys()):
        resultat_TF_IDF = []

        # on fait une seconde boulce sur le nom des fichiers
        for i in files_names:

            # Ouverture du fichier en mode lecture
            with open("./cleaned/{}".format(i), "r") as fichier1:

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
        matrice_TF_IDF[mot] = resultat_TF_IDF
    # print(len(matrice_TF_IDF))
    return matrice_TF_IDF


# On teste la fonction avec le répertoire cleaned.
res = TF_IDF("cleaned")


# print(res)

###############################################
### Question 1 Affichage valeur TF-IDF == 0 ###
###############################################

# Partie 1
def calcul_mot_dit_nn_important():
    # Appel de la fonction TF_IDF pour obtenir la matrice
    valeur_td_idf = TF_IDF("cleaned")
    L = []

    # On fait une boucle où i va aller piocher des tuples des cles et des valeurs de la liste
    for i in valeur_td_idf.items():
        occurence = 0
        # On va ensuite compter le nombre de 0, pour savoir si ce mot à un TD-IDF = 0 dans tous les fichiers
        for zero in i:
            if zero == 0:
                occurence += 1
            else:
                break
            # si on a des valeurs TD-IDF dans tous les fichiers pour ce mot, il est alors ajouter à la liste.
            if occurence == 8:
                L.append(i[0])
    return (L)


# print(calcul_mot_dit_nn_important())

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
### Question 2 Afficher le(s) mot(s) ayant le score TD-IDF le plus élevé ###
############################################################################


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


# print(score_IDF_eleve())

###########################################################################
### Question 3 Indiquer le mot le plus utilisé par le predident chirac ###
##########################################################################

# On crée une fonction pour trouver le(s) mot(s) le(s) plus répété(s) par le président Chirac
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
            with open(directory + '/' + i, 'r') as fichier:
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


# print(indiquer_le_mot_plus_utilise("Chirac"))

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

################################################################################
### 5. Indiquer le premier président à parler du climat et/ou de l’écologie ###
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

# La fonction suivante recherche le président qui a abordé en premier les sujets liés au climat, à l'écologie
# ou au réchauffement dans les discours.

def climat_president():
    # Obtient la liste des noms de fichiers dans le répertoire "cleaned"
    files_names = list_of_files("./cleaned", "txt")
    liste_president = []

    # Parcourt chaque fichier, lit et divise chaque fichier en mots
    for i in files_names:
        with open("./cleaned/{}".format(i), 'r') as fichier:
            contenu = fichier.read()
            texte_mot_cleaned = contenu.split()
            # Obtient le nom du président à partir du nom du fichier
            nom_president = (i[11:-4])

            # Si le nom président se termine par un chiffre, supprime ce chiffre
            if nom_president[-1] >= chr(48) and nom_president[-1] <= chr(57):
                nom_president = nom_president[:-1]

            # Vérifie si des termes liés au climat, à l'écologie ou au réchauffement sont présents dans le texte
            if ("ecologie" in texte_mot_cleaned) or ("climat" in texte_mot_cleaned) or (
                    "réchauffement" in texte_mot_cleaned):

                # Ajoute le nom du président à la liste s'il a parlé de l'écologie et s'il n'est pas déjà présent
                if not (nom_president in liste_president):
                    liste_president.append(nom_president)
    
    #On met un choix multiple pour couvrir toutes les options
    # Si aucun président n'a abordé ces sujets, retourne "aucun"
    if liste_president == []:
        return "aucun"
    # Si un seul président a abordé ces sujets, retourne son nom
    elif len(liste_president) == 1:
        return liste_president[0]
    # Si plusieurs présidents ont abordé ces sujets, trouve celui qui a parlé en premier
    else:
        minimum = 999999999999999999
        for i in liste_president:
            # Recherche le président avec le discours le plus ancien sur ces sujets
            if minimum > presidents_et_dates[i]:
                minimum = presidents_et_dates[i]
                president = i
        return "Le président ayant parlé en premier du climat/écologie est M." + president

# Appelle la fonction et imprime le résultat
# print(climat_president())

#############################################################
### 6. le(s) mot(s) que tous les présidents ont évoqués. ###
############################################################

def mot_evoque():
    # On crée une boucle pour stocker les mots dit par tous les présidents
    mots_evoque = []

    # On fait une boucle sur les mots de la matrice TF_IDF
    # Si le mots a un score minimum dans tous les discours est différent de 0 alors on l'ajoute à la liste
    for score in res.items():
        min = 99999999
        for i in score[1]:
            if min > i:
                min = i
        if min != 0:
            mots_evoque.append(score[0])
    # on revoit le(s) mot(s) que tous les présidents ont évoqués
    return ("le(s) mot(s) que tous les présidents ont évoqués sont:", mots_evoque)


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
