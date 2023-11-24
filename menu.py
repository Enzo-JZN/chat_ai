from main import *

#On définit une fonction qui a pour role de faire menu. Soit le lien entre les différentes fonctions
def menu():

#On commence par proposez à l'utilisateur de choisir l'option qu'il souhaite appeler
    print("Que voulez-vous faire ?\n"
          "- Tapez 1 : Si vous voulez avoir les mots les moins importants des fichiers.\n"
          "- Tapez 2 : Si vous voulez afficher les mots avec les TF_IDF les plus élevés.\n"
          "- Tapez 3 : Si vous voulez les mots les plus répétés par le président Chirac.\n"
          "- Tapez 4 : Si vous voulez avoir le nom des présidents qui ont parlé de la Nation et celui l'ayant fais le plus souvent.\n"
          "- Tapez 5 : Si vous voulez savoir qui est le premier président à avoir parlé de l'écologie.\n"
          "- Tapez 6 : Si vous voulez avoir l'ensemble des mots importants que tous les présidents ont évoqués.\n"
          "- Tapez Q : Si vous souhaitez quitter le menu.")
    choice = input("Tapez : ")

#Selon le choix de l'utilisateur on appele la fonction demander
    if choice == "1":
        print(TF_IDF_NUL())
    elif choice == "2":
        print(TF_IDF_HIGH())
    elif choice == "3":
        print(indiquer_le_mot_plus_utilise("Chirac"))
   # elif choice == "4":

    elif choice == "5":
        print(president_ecologie())
    elif choice == "6":
        mot_globaux_presidents()
    elif choice == "Q":
        print("Au revoir.")

#On met une sécurité si jamais l'utilisateur c'est trompé de commande et lui propose de recommencer
    else:
        retry = input("Ce n'est pas une possiblité voulez_vous réessayer :\n"
                     "- Tapez 1 pour Oui\n"
                     "- Tapez 2 pour Non\n")
        if retry == "1":
            print(menu())
        else:
            print("Au revoir.")
#On propose à l'utilisateur d'essayer une autre possiblité
    encore = input("Voulez-vous esssayer une autre possibilité ?:\n"
                     "- Tapez 1 pour Oui\n"
                     "- Tapez 2 pour Non\n")
    return
print(menu())



