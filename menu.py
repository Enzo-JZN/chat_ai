from questions_part1 import *
from questions_part2 import *


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
#On définit une fonction qui a pour role de faire menu. Soit le lien entre les différentes fonctions
def menu():
    clear_terminal()

    # On commence par proposer à l'utilisateur de choisir l'option qu'il souhaite appeler
    print("Que voulez-vous faire ?\n"
          "- Tapez 1 : Si vous voulez avoir les mots les moins importants des fichiers.\n"
          "- Tapez 2 : Si vous voulez afficher les mots avec les TF_IDF les plus élevés.\n"
          "- Tapez 3 : Si vous voulez les mots les plus répétés par le président Chirac.\n"
          "- Tapez 4 : Si vous voulez avoir le nom des présidents qui ont parlé de la Nation et celui l'ayant fait le plus souvent.\n"
          "- Tapez 5 : Si vous voulez savoir qui est le premier président à avoir parlé de l'écologie.\n"
          "- Tapez Q : Si vous souhaitez quitter le menu.")
    choix = input("Tapez : ")

    clear_terminal()

    # Selon le choix de l'utilisateur on appelle la fonction correspondante
    if choix == "1":
        print(calcul_mot_dit_nn_important(), mot_moins_important())
    elif choix == "2":
        print(score_IDF_eleve())
    elif choix == "3":
        print(indiquer_le_mot_plus_utilise("Chirac"))
    elif choix == "4":
        print(president_nation())
    elif choix == "5":
        print(climat_president())
    elif choix.upper() == "Q":
        print("Au revoir.")
        return

    # On met une sécurité si jamais l'utilisateur s'est trompé de commande et lui propose de recommencer
    else:
        essai2 = input("Ce n'est pas une possibilité, voulez-vous réessayer :\n"
                      "- Tapez 1 pour Oui\n"
                      "- Tapez 2 pour Non\n")
        if essai2 == "1":
            menu()
        else:
            print("Au revoir.")

    if choix != 'Q':
        # On propose à l'utilisateur d'essayer une autre possibilité sauf s'il voulait quitter
        encore = input("Voulez-vous essayer une autre possibilité prédéfini ?\n"
                       "- Tapez 1 pour Oui\n"
                       "- Tapez 2 pour Non\n")
        if encore == "1":
            menu()
        else:
            print("Au revoir.")
        return

