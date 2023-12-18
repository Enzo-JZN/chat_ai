from menu_chatbot import *
from menu import *

#############################################################################################################
### Le Fichier main.py a pour rôle de gérer les échanges entre l'utilisateur et le reste de l'application ###
#############################################################################################################


print("Bienvenue dans cette application :")
print("Si vous voulez voir le fonctionnalités primaires : Tapez 1")
print("Si vous voulez discutez avec le ChatBot : Tapez 2")
print("Si vous voulez quitter : Tapez Q")

# Fonction qui sert de menu global pour permettre à l'utilisateur d'avoir toutes les fonctionnalitées 
# Elle ne retourne rien car elle sert d'affichage
def choix_menu():
    choix = input("Quel est votre choix : ")
    if choix == '1':
        menu()
    elif choix == '2':
        menu_chatbot()
    elif choix == 'Q':
        print("Merci et au revoir.")
    else:
        print("Votre choix est incorrect voulez-vous réessayer : ")
        print("Si oui : Tapez 1")
        print("Si non : Tapez 2")
        nouveau_choix = input("Quel est votre choix : ")
        if nouveau_choix == '1':
            print(choix_menu())
        else:
            print("Au revoir.")
    return
choix_menu()

