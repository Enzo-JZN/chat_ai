from questions_part2 import *
def reponses_chatbot():
    question = input("Quelle est votre question ?")
    #print(generer_reponse(question, 'cleaned', document, ))
    
def menu_chatbot():
    print('Bienvenue dans ce Chatbot :')
    print("Ce Chatbot va répondre à vos questions en analysant des textes de présidents français.")
    print("Voulez-vous poser une autre question ?")
    print("Si oui : Tapez 1")
    print("Si non : Tapez 2")
    reponse = input("Que voulez-vous :")
    if reponse == '1':
        reponses_chatbot()
    else:
        print("Au revoir.")
