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