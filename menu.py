from main import *

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
          "- Tapez 6 : Si vous voulez avoir l'ensemble des mots importants que tous les présidents ont évoqués.\n"
          "- Tapez Q : Si vous souhaitez quitter le menu.")
    choice = input("Tapez : ")

    clear_terminal()

    # Selon le choix de l'utilisateur on appelle la fonction correspondante
    if choice == "1":
        print(calcul_mot_dit_nn_important(), mot_moins_important())
    elif choice == "2":
        print(score_IDF_eleve())
    elif choice == "3":
        print(indiquer_le_mot_plus_utilise("Chirac"))
    elif choice == "4":
        print(president_nation())
    elif choice == "5":
        print(climat_president())
    elif choice == "6":
        print(mot_evoque())
    elif choice.upper() == "Q":
        print("Au revoir.")
        return

    # On met une sécurité si jamais l'utilisateur s'est trompé de commande et lui propose de recommencer
    else:
        retry = input("Ce n'est pas une possibilité, voulez-vous réessayer :\n"
                      "- Tapez 1 pour Oui\n"
                      "- Tapez 2 pour Non\n")
        if retry == "1":
            menu()
        else:
            print("Au revoir.")
            return

    # On propose à l'utilisateur d'essayer une autre possibilité
    encore = input("Voulez-vous essayer une autre possibilité ?:\n"
                   "- Tapez 1 pour Oui\n"
                   "- Tapez 2 pour Non\n")
    if encore == "1":
        menu()
    else:
        print("Au revoir.")
        return


(menu())
