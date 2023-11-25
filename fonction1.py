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
