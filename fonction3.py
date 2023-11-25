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