import os

################################################################################################################
### Le fichier gestion_fichiers.py contient l'ensemble des fonctions qui gèrent le traitement des textes pour ##
### faciliter leurs utilisations                                                                              ##
################################################################################################################

#Fonction qui permet de retourner la liste des fichiers dans un répertoire donné
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


# Extraire les noms des présidents à partir des noms des fichiers texte fournis et retourne un set de tous les noms
def extract_president_names(file):
    liste = set()
    nom_presidents = set()  # Utilisez un ensemble pour éviter les doublons
    # on fait une première boucle pour mettre dans une liste tous les présidents avec leurs numéros
    # permettant d'enlever leurs type et +
    for i in files_names:
        nom_presidents.add(i[11:-4])

    # on fait 2 boucles pour accéder à chaque caractère et ainsi supprimer les doublons
    for i in nom_presidents:
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
dico_prenom = {"Giscard dEstaing": "Valéry", "Macron": "Emmanuelle", "Mitterrand": "François", "Sarkozy": "Nicolas",
        "Chirac": "Jacques", "Hollande": "François"}

# Fonction qui retourne le dictionnaire des prénoms des présidents
def president_prenom(x):
    return (dico_prenom[x])


# Fonction qui convertir texte en miniscules + creation repertoire cleaned + copier contenue dans le nouveau repertoire
# Créé des nouveaux fichiers avec le texte nettoyés
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
        # On crée le chemin et le nouveau nom du fichier copier
        chemin_cleaned = directory_cleaned + "/" + i

        # On crée le fichier copier, puis on copie le contenu du premier fichier et on le rajoute le tout en minuscule
        with open(chemin_cleaned, "w", encoding="utf-8") as fichier:
            fichier2 = open(directory + "/" + i, "r", encoding="utf-8")
            contenu = fichier2.read()
            fichier.write(contenu.lower())

# Fonction qui supprime la ponctuation dans un fichier et réécrit le texte sans ponctuation dans un autre fichier
def supprimer_ponctuation():
    # trouve le chemin d'accés des fichiers à nettoyer
    directory = "./cleaned"
    files_names = list_of_files(directory, "txt")
    # on fait une boucle qui ouvre chaque fichier du répertoire un par un et on met le texte dans une variable
    for nom_fichier in files_names:
        with open(directory + "/" + nom_fichier, "r", encoding="utf-8") as fichier:
            contenu = fichier.read()
        indice = []
        # dans une liste on met toutes les positions où il y a un signe de ponctuations
        ponctuation = [',', '?', ';', '.', '!', '`', "'", '-', ':', '"']
        contenu1 = ""
        # on fait une boucle qui va copier le contenue du texte jusqu'à la postion d'une ponctuation et remplace cette
        # ponctuation par un espace et cela jusqu'à la fin du texte
        for car in contenu:
            if car in ponctuation:
                contenu1 += ' '
            else:
                contenu1 += car
        # reécrit le nouveau texte sans la ponctuation
        with open(directory + "/" + nom_fichier, "w", encoding="utf-8") as fichier_modifie:
            fichier_modifie.write(contenu1)


convertir_textes_miniscules()
supprimer_ponctuation()


# Écrire une fonction qui prend en paramètre une chaine de caractères et qui retourne un dictionnaire
# associant à chaque mot le nombre de fois qu’il apparait dans la chaine de caractères
# Renvoie un dictionnaire avec en clé des mots et en valeur leurs occurrences
def occurences_chaines(chaine):
    indice = []
    dico = {}
    liste_mot = []

    # On fait une boucle pour obtenir tous les indices où se trouvent de signes de ponctuation
    for i in range(len(chaine)):
        if (ord(chaine[i]) >= 21 and ord(chaine[i]) <= 47) or (ord(chaine[i]) >= 58 and ord(chaine[i]) <= 64) or (
                chaine[i]) == "\n":
            indice.append(i)

    # On utlisera les indices précèdemment acquis pour effectuer des slides dans la chaine de caractere initial et
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
