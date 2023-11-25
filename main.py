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


# print(president_prenom("Macron"))

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

        # On crée le fichier copier, puis on copie le contenu du premier fichier et on le rajoute le tout en minuscule
        with open(chemin_cleaned, "w", encoding="utf-8") as fichier:
            chemin_original = directory + "/" + i
            with open(chemin_original, "r", encoding="utf-8") as fichier_original:
                contenu = fichier_original.read()
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

    # On met un choix multiple pour couvrir toutes les options
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
print(climat_president())

