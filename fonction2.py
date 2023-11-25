
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