from menu import *

####################################################################################################
### Le fichier menu_chatbot.py sert de menu pour permettre à l'utilisateur de poser des questions###
#####################################################################################################

# Fonction répond à une question de l'utilisateur
def reponses_chatbot():
    chaine = input("Posez une question : ")
    print(affiner_reponse(chaine, trouver_occurrence_et_phrase(calcul_doc_plus_pertinent(chaine),
                                                               trouver_mot_plus_important_TF_IDF(chaine))))
    autre_quest = input(("Voulez vous poser une autre question ? \n"
                         "Si oui : Tapez 1\n"
                         "Si non : Tapez 2\n"))
    if autre_quest == '1':
        reponses_chatbot()
    else:
        print("Au revoir")

# Fonction qui sert de menu au chatBot pour répondre à l'utilisateur
def menu_chatbot():
    print('Bienvenue dans ce Chatbot :')
    print("Ce Chatbot va répondre à vos questions en analysant des textes de présidents français.")
    print("Voulez-vous poser une question ?")
    print("Si oui : Tapez 1")
    print("Si non : Tapez 2")
    reponse = input("Que voulez-vous :")
    if reponse == '1':
        reponses_chatbot()
    else:
        print("Au revoir.")
