import os 

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

# Call of the function
directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(files_names)
print()

#Extraire les noms des présidents à partir des noms des fichiers texte fournis ; 
def extract_president_names(file):
    liste = set()
    president_names = set()  # Utilisez un ensemble pour éviter les doublons
    # on fait une première boucle pour mettre dans une liste tous les présidents avec leurs numéros
    # permettant d'enlever leurs type et + 
    for i in files_names:
        president_names.add(i[11:-4])

    # on fait 2 boucles pour accéder à chaque caractère et ainsi supprimer les doublons
    for i in president_names:
        # on va créer une liste où on traitera chaque president à part, en utilisant leur table ascii pour 
        # déterminer leur type
        vrai_prenom = []
        for j in range(len(i)):

            # on vérifie la condition qui dit que le caractère n'est pas un nombre
            if ord(i[j]) < 48 or ord(i[j]) > 57:
               continue
            else: 
                vrai_prenom.append(i[:j])
        
        # si elle ne possède pas de numéro, on l'ajoute dans liste pour ensuite être copier dans le set
        if vrai_prenom == []:
            vrai_prenom.append(i)
        liste.add(vrai_prenom[0]) #pour changer la liste en mot      
    return liste

print(extract_president_names(files_names))

#Associer à chaque président un prénom 
dico = {"Giscard dEstaing" :"Valéry", "Macron" : "Emmanuelle" , "Mitterrand" : "François" , "Sarkozy" : "Nicolas" , "Chirac" : "Jacques" , "Hollande" : "François" }
def president_prenom(x) : 
    return(dico[x])
print(president_prenom("Macron"))

# Afficher la liste des noms des présidents (attention aux doublons) ; 
print(extract_president_names(files_names))

#convertir texte en miniscules + creation repertoire cleaned + copier contenue dans le nouveau repertoire
def convertir_textes_miniscules():
    # on trouve le chemin pour acceder à speeches et ensuite on obtient la liste files.names
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")

    # on trouve le chemin pour acceder à cleaned, nouveau repertorie
    directory_cleaned = "./cleaned"

    # Vérifiez si le répertoire n'existe pas déjà, puis créez-le
    #if not os.path.exists(directory_cleaned):
    os.makedirs(directory_cleaned, exist_ok=True)
        
    #On va acceder au nom des fichiers pour trouver leurs chemins
    for i in files_names:

        # On crée le chemin et le noveau nom du fichier copier
        chemin_cleaned = directory_cleaned+"/"+i
        chemin_cleaned = directory_cleaned + "/" + i[:-4]
        chemin_cleaned += "_copy" + i[-4:]

        # On crée le fihcier copier, puis on copie le contenu du premier fihcier et on le rajoute le tout en miniscule
        with open(chemin_cleaned, "w") as fichier:
            fichier2 = open(directory + "/" + i,"r")
            contenu = fichier2.read()
            fichier.write(contenu.lower())
            
def supprimer_ponctuation():
    #trouve le chemin d'accés des fichiers à nettoyer
    directory = "./cleaned"
    files_names = list_of_files(directory, "txt")
    #on fait une boucle qui ouvre chaque fichier du répertoire un par un et on met le texte dans une variable
    for nom_fichier in files_names:
        with open(directory + "/" + nom_fichier, "r") as fichier:
            contenu = fichier.read()
        indice = []
        #dans une liste on met toutes les positions où il y a un signe de ponctuations
        for i in range (len(contenu)):
            if (ord(contenu[i]) >= 21 and ord(contenu[i]) <=47) or (ord(contenu[i]) >=58 and ord(contenu[i])<= 64) or (contenu[i])=="\n" :
                indice.append(i)
        n = 0
        contenu1 = ""
        # on fait une boucle qui va copier le contenue du texte jusqu'à la postion d'une ponctuation et remplace cette 
        #ponctuation par un espace et cela jusqu'à la fin du texte
        for i in indice :
            contenu1 = contenu1 + contenu[n:i] + " "
            n = i+1
        #reécrit le nouveau texte sans la ponctuation
        with open(directory + "/" + nom_fichier, "w") as fichier_modifie:
            fichier_modifie.write(contenu1)
        
print(convertir_textes_miniscules())
print(supprimer_ponctuation())

# Écrire une fonction qui prend en paramètre une chaine de caractères et qui retourne un dictionnaire
# associant à chaque mot le nombre de fois qu’il apparait dans la chaine de caractères
def occurences_chaines(chaine):
    indice = []
    dico = {}
    liste_mot = []

    # On fait une boucle pour obtenir tous les indices où se trouvent de signes de ponctuation 
    for i in range(len(chaine)):
        if (ord(chaine[i]) >= 21 and ord(chaine[i]) <=47) or (ord(chaine[i]) >=58 and ord(chaine[i])<= 64) or (chaine[i])=="\n" :
            indice.append(i)
        
    # On utlisera les indices precedemment acquis pour effectuer des slides dans la chaine de caractere initial et
    # ainsi copier les mots.
    n = 0
    for i in indice:
        liste_mot.append(chaine[n:i])
        n = i + 1

    # On fera une double boucle pour compter le nombre d'occurences de chaque mot tout en créant un dictionnaire
    for i in liste_mot:
        occurences = 0
        for j in liste_mot:
            if i == j:
                occurences += 1
        dico[i] = occurences
    return dico

# print(occurences_chaines("Écrire une fonction qui prend en paramètre une chaine de caractères 
# et qui retourne un dictionnaire associant à chaque mot le nombre de fois qu’il apparait dans 
# la chaine de caractères."))

# Écrire une fonction qui prend en paramètre le répertoire où se trouve l’ensemble des fichiers du corpus
# et qui retourne un dictionnaire associant à chaque mot son score IDF. 

def IDF_par_fichier(repertoire):
    
    directory = './{}'.format(repertoire) # "/Users/enzojuzyna/Downloads/projet/speeches"    
    files_names = list_of_files(directory, "txt")

    contenu = ""
    liste_contenu = []
    for i in files_names:
        with open(directory + '/' + i, 'r') as fichier_IDF :
            contenu = fichier_IDF.read()
            contenu = contenu.split()
            liste_contenu += contenu
    set_mot = set(liste_contenu)

    dico = {}
    for mot in set_mot:
        occurence = 0
        for i in files_names:
            with open(directory + '/' + i, 'r') as fichier_IDF :
                contenu = fichier_IDF.read()
                if mot in contenu:
                    occurence += 1
        calcul_idf = math.log10((len(files_names) / occurence) + 1)
        dico[mot] = calcul_idf
    return dico

a = IDF_par_fichier("cleaned")

# Indiquer le mot le plus utilisé par le predident chirac
def indiquer_le_mot_plus_utilise(president):

    # On donne le chemin pour acceder au fichier qui contiennent le nom du president recherche
    directory = './cleaned' # "/Users/enzojuzyna/Downloads/projet/speeches"    
    files_names = list_of_files(directory, "txt")
    
    # On créera un liste max qui prendra pour valeur le mot avec le plus d'occurences, on l'initialise à 0
    max = [0, 0]
    contenu = ""
    for i in files_names:
        if president in i:
            with open (directory + '/'+ i, 'r') as fichier:
                contenu += fichier.read() + " "
    dico = occurences_chaines(contenu)
    for a in dico.items():
        if max[1] < a[1] and a[0] != '':
            max = a

    liste_mot = [max]
    for j in dico.items():
        if max[1] == j[1]:
            if max[0] != j[0]:
                liste_mot.append(j[0])
    return liste_mot

print(indiquer_le_mot_plus_utilise("Chirac")) 

#President qui ont parlé de la Nation:

# On donne le chemin pour acceder au fichier qui contiennent le nom du president recherche
directory = './speeches' # "/Users/enzojuzyna/Downloads/projet/speeches"    
files_names = list_of_files(directory, "txt")
    
# On créera un liste max qui prendra pour valeur le mot avec le plus d'occurences, on l'initialise à 0
liste_president = []
for i in files_names:
    with open (directory + '/'+ i, 'r') as fichier:
        contenu = fichier.read()
    if "Nation" in contenu or "nation" in contenu:
        liste_president.append(i[11:-4])

set_president = set()
for i in extract_president_names(files_names):
    if i in liste_president:
        set_president.add(i)
            
print(set_president)
