from calculs import *

###############################################
### Question 1 Tokenisation de la Question ###
###############################################
def tokenisation_question(question):
    # On va d'abord mettre tous les termes de la question en minuscules
    # Pour cela on crée une chaine de caractère vide où on va stocker les mots
    question_minuscule = ''
    # On fait une boucle pour vérifier chaque caractère de la question
    for lettre in question:
        # S'il est en majuscule, on le rajoute à la chaine de caractère après l'avoir passé en minuscule
        if 65 <= ord(lettre) <= 90:
            question_minuscule += chr(ord(lettre) + 32)
        # Sinon, on le rajoute telle quel
        else:
            question_minuscule += lettre

    # On va maintenant enlever la ponctuation de la question
    # On crée une chaine de caractère pour y mettre la question nettoyée
    question_clean = ''
    # On parcourt chaque caractère de la question
    for caractere in question_minuscule:
        # Si c'est une ponctuation on le remplace par un espace
        if ((21 <= ord(caractere) <= 47) or (58 <= ord(caractere) <= 64) or (91 <= ord(caractere) <= 96)
                or (123 <= ord(caractere) <= 126) or (caractere) == "\n"):
            question_clean += ' '
        # Sinon, on le rajoute tel quel
        else:
            question_clean += caractere

    # On utilise la fonction split pour séparer tous les mots de la question et les mettre dans une liste
    mot_question = question_clean.split()
    return mot_question



########################################################################
### Question 2 Recherche des mots dans le Corpus et dans la question ###
########################################################################
def mot_question_et_document(question):
    # On crée une liste vide pour y stocker les mots présents à la fois dans la question et dans le document
    mot_question_documents = []
    # On appelle la fonction tokenisation pour avoir les mots présent dans la question
    mot_question = tokenisation_question(question)
    # On appelle la fonction IDF_par_fichier pour avoir le dico des mots présent dans le corpus de texte
    mot_repertoire = IDF_par_fichier('cleaned')

    # Pour chaque mot de la question on vérifie s'il est dans le corpus et si oui on l'ajoute dans la liste
    for mot in mot_question:
        if mot in mot_repertoire:
            mot_question_documents.append(mot)
    return mot_question_documents



##########################################################
### Question 3 Calcul du vecteur TF-IDF pour la Question ###
##########################################################
def TF_IDF_question(question):
    # Crée un dico vide pour y stocker le vecteur TF_IDF de la question
    vecteur_TF_IDF_question = {}

    # Appel une focntion qui va donner l'ensemble des mots de la questions
    # Et une qui va donner l'ensemble des mots de chaque fichier ainsi que la valeur de son IDF
    mots_questions = tokenisation_question(question)
    mots_repertoire = IDF_par_fichier('cleaned')
    # On appel la fonction qui donne les mots présent dans la quetion et dans le document
    mot_question_documents = mot_question_et_document(question)

    # On fait une boucle pour calculer le vecteur TF_IDF de chaque mots pour chaque fichier
    for mots in mots_repertoire:

        # On vérifie si le mot est présent à la fois dans la question et dans le texte
        if mots in mot_question_documents:
            # On fait un boucle pour calculer le nombre d'occurences du mot dans la question
            occ_mot = 0
            for mot in mots_questions:
                if mots == mot:
                    occ_mot += 1
            # On calcul le score TF du mot
            score_TF = occ_mot / len(mots_questions)
            # Si oui on calcul sa valeur et on l'ajoute au dico des vecteurs
            vecteur_TF_IDF_question[mots] = score_TF * mots_repertoire[mots]

        # Sinon sa valeur est égal à zéro
        else:
            vecteur_TF_IDF_question[mots] = 0

    # On renvoit le dico
    return vecteur_TF_IDF_question

#########################################
### Question 4 Calcul de la Similarité ###
#########################################

#Calcul le produit scalaire entre deux vecteurs
def produit_scalaire(A, B):
    somme = 0
    for i in A:
        somme = somme + (A[i] * B[i])
    return somme

#Calcul la norme d'un vecteur
def norme_vecteur(A):
    somme = 0
    for i in A:
        somme = somme + (A[i]) ** 2
    somme = (somme) ** (1 / 2)
    return somme

#Calcul la similarité cosinus entre deux vecteurs
def similarite_cosinus(A, B):
    produit_scalaire_ab = produit_scalaire(A, B)
    norme_a = norme_vecteur(A)
    norme_b = norme_vecteur(B)
    res = (produit_scalaire_ab / (norme_a + norme_b))
    return res

###########################################################
### Question 5 Calcul du Document le Plus Pertinent ###
###########################################################
def calcul_doc_plus_pertinent(question):
    #Calcul les vecteurs TF_IDF nécessaires à la fonction
    TF_IDF_tous_fichier = TF_IDF_par_doc()
    TF_IDF_question1 = TF_IDF_question(question)

    dico_similarite = {}
    #Pour chaque document calcul la similarité cosinus entre le vecteur de la question et celui du doc
    for i in TF_IDF_tous_fichier:
        similarite = similarite_cosinus(TF_IDF_tous_fichier[i], TF_IDF_question1)
        dico_similarite[i] = similarite

    #Recherche le document le plus adapté
    max = 0
    indice_max = 0
    for i in dico_similarite:
        if max < dico_similarite[i]:
            max = dico_similarite[i]
            indice_max = i
    return indice_max


############################################
### Question 6 Génération d'une Réponse ###
############################################
# Permet de trouver la phrase dans le texte


#Recherche le mot le plus important dans la question et renvoit ce même mot
def trouver_mot_plus_important_TF_IDF(question):
    dico_TD_IDF_question = TF_IDF_question(question)
    max = 0
    mot = ""
    for i in dico_TD_IDF_question.items():
        if max < i[1]:
            max = i[1]
            mot = i[0]
    return mot



def trouver_occurrence_et_phrase(document, mot):
    directory = "./speeches"
    with open(directory + '/' + document, 'r') as file:
        contenu_document = file.read()

    #Cherche la position d'un mot dans un document
    position_mot = -1
    for i in range(0, len(contenu_document)):
        if contenu_document[i:i + len(mot)] == mot:
            position_mot = i
            break

    #Cherche la phrase qui contient le mot
    debut_phrase = 0
    #On fait un boucle qui va chercher le point qui termine la phrase précédente, pour trouver où commence celle là.
    for i in range(position_mot, 0, -1):
        if contenu_document[i] == '.':
            debut_phrase = i + 1
            break

    #Cherche la fin de la phrase
    fin_phrase = len(contenu_document)
    # Fait une boucle pour trouver le point de fin de phrase.
    for i in range(position_mot, len(contenu_document)):
        if contenu_document[i] == '.':
            fin_phrase = i
            break

    #Renvoit la première phrase ou se trouve le mot
    phrase_contenant_mot = contenu_document[debut_phrase:fin_phrase + 1]
    return phrase_contenant_mot


################################################
### Question 7 Affiner et Améliorer la Réponse ###
################################################


def generer_reponse(question, corpus, files_names, Score_TF_IDF_CLEANED):
    liste_mot = question.split()
    liste_mot_TF_IDF = []

    idx = 0
    # Permet d'obtenir la position de du corpus dans la liste des fichiers
    for index in range(len(files_names)):
        if corpus in files_names[index]:
            idx = index

    # Permet d'ajouter le score tf_idf de chaque mot correspondant dans une liste
    for mot in liste_mot:
        liste_mot_TF_IDF.append(Score_TF_IDF_CLEANED[liste_mot.index(mot)][idx])

    # Permet d'obtenir la position du score max TF IDF dans la liste mot
    index_max = liste_mot_TF_IDF.index(max(liste_mot_TF_IDF))
    mot_max = liste_mot[index_max]
    phrase = trouver_occurrence_et_phrase(corpus, mot_max)

    return  phrase
