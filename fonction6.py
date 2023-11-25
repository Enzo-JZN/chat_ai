#############################################################
### 6. le(s) mot(s) que tous les présidents ont évoqués. ###
############################################################

def mot_evoque():
    # On crée une boucle pour stocker les mots dit par tous les présidents
    mots_evoque = []

    # On fait une boucle sur les mots de la matrice TF_IDF
    # Si le mots a un score minimum dans tous les discours est différent de 0 alors on l'ajoute à la liste
    for score in res:
        if min(res[score]) != 0:
            mots_evoque.append(score)
    # on revoit le(s) mot(s) que tous les présidents ont évoqués
    return ("le(s) mot(s) que tous les présidents ont évoqués sont:", mots_evoque)

