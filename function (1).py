#----------------------------------------------------------------------------PARTIE_1----------------------------------------------------------------------------------------
def Creation_Question_Globale():
import os
import random
from math import *
def intro():
    print("avez vous creer les fichiers ?")
    rep = input('Rentre ton choix (oui,non): ')
    print(ext_pres())
    if rep == 'oui':
        pass
    else : 
        minuscules()
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith("txt"):
            files_names.append(filename)
    return files_names
def modification(txt):
    liste="!#$%&()*+,./:;<=>?@[]^_`{|}~"
    sectxt=""
    for elt in txt :
        if elt in liste:
            sectxt=sectxt + " "
        elif elt == "-":
            if sectxt[-1] == '\n':
                sectxt=sectxt
            else :
                sectxt = sectxt + " "
        elif elt == "'":
            if sectxt[-1] == "l":
                sectxt = sectxt + random.choice("ae")+ " "
            elif sectxt[-1] == "u":
                sectxt = sectxt + random.choice("ie")+ " "
            else :
                sectxt = sectxt + "e "
        else :
            sectxt=sectxt + elt
    return sectxt
def copie(file):
    os.chdir("../")
    texte=""
    f = open(f"speeches/{file}","r",encoding="utf8")
    texte = str(f.read())
    texte = texte.lower()
    return modification(texte)
def creation_cleaned():
    for fichier in list_of_files("./speeches",".txt"):
        if fichier not in os.listdir("cleaned"):
            os.chdir("cleaned")
            f = open(fichier,"x",encoding="utf8")
            f.close()
            f = open(fichier,"w",encoding="utf8")
            f.write(copie(fichier))
            f.close()
    return 
def minuscules():
    if not os.path.exists("cleaned"):
        os.mkdir("cleaned")
        creation_cleaned()      
    return 
def ext_pres():
    liste = os.listdir("speeches")
    L = []
    for fichier in liste: # Pour éviter qu'un utilisateur ajoute un fichier indésirable
        if fichier.endswith(".txt"):
            L.append(fichier)
    Tab = []
    for element in L:
        element = element[11:]
        element = element.replace(".txt","").replace("1","").replace("2","")
        Tab.append(element)
        Tableau_final = list(set(Tab))
    return Tableau_final 
def TF():#fonction qui sert a mettre dans un dico tout les mots avec le nombre de leurs occurances
    liste_of_words = {}
    for fichier in list_of_files("./speeches",".txt") :
        f = open(f"cleaned/{fichier}","r",encoding="utf8")
        texte = f.read()
        for mot in texte.split():
            if mot not in liste_of_words :
                liste_of_words[mot]=1
            else:
                liste_of_words[mot]+=1
    return liste_of_words 
def IDF(mot_chercher):#revoie le log de chaque mot voulu un par un
    cpt=0
    for fichier in list_of_files("./speeches",".txt") :
        f = open(f"cleaned/{fichier}","r",encoding="utf8")
        texte = f.read()
        if mot_chercher in texte.split():
            cpt=cpt+1
    if cpt != 0:
        loga = log((len(list_of_files("./speeches",".txt"))/cpt)) 
    else:
        loga = 0.0
    return loga  
def TF_idf():#revoie le TF-IDF de chaque mot sous forme de dictionnaire
    dico_TF_IDF={}
    for key,valeurs in TF().items():
        dico_TF_IDF[key]=IDF(key)*valeurs
    return dico_TF_IDF
def TF_IDF_mot(val,nom):
    TF_dans_texte = 0
    for fichier in list_of_files("./speeches",".txt") :
        if nom in fichier :
            f = open(f"cleaned/{fichier}","r",encoding="utf8")
            texte = f.read()
            for mot in texte.split():
                if mot == val :   
                    TF_dans_texte+=1
            return TF_dans_texte/len(texte.split())*IDF(val)
def min_idf():# question 1 renvoie la liste de tout les mots avec un IDF de 0 !attendre un peu car ça met du temps! 
    liste_pas_important=[]
    dico=TF_idf()
    for key,valeurs in dico.items():
        if dico[key] == 0.0:
            liste_pas_important.append(key)
    return liste_pas_important
def max_td_idf():#question 2 renvoie les mots avec les TD-idf les plus haut 
    liste_max=[]
    val_max=0
    dico=TF_idf()
    for key,valeurs in dico.items():
        if dico[key] > val_max:
            val_max = dico[key]
    for key,valeurs in dico.items():
        if dico[key] == val_max:
            liste_max.append(key) 
    return liste_max
def mot_rep(file_name):# donne le mot qui a ete le plus prononcer par un president selectionner
    dico_count={}
    val_max=0
    clef=""
    for fichier in list_of_files("./speeches",".txt") :
        if file_name in fichier :
            f = open(f"cleaned/{fichier}","r",encoding="utf8")
            texte = f.read()
            for mot in texte.split():
                if mot in dico_count:
                    dico_count[mot]+=1
                else:
                    dico_count[mot]=1
    for key,valeurs in dico_count.items():
        if dico_count[key] > val_max:
            val_max = dico_count[key]
            clef=key
        
    return("Le mot le plus dit par '{}' est '{}' et il est dit {} fois".format(file_name,clef,val_max))          
def Nation():#question 4 renvoie les presidents parlant de Nation et celui qui parle le plus de nation
    liste_des_presidents=[]
    L=[]
    dico_count={}
    val_max=0
    clef=""
    for fichier in list_of_files("./speeches",".txt") :
        f = open(f"cleaned/{fichier}","r",encoding="utf8")
        texte = f.read()
        if "nation" in texte.split():
            L.append(fichier)
            for element in L:
                element = element [11:]
                element = element.replace(".txt","").replace("1","").replace("2","")
            liste_des_presidents.append(element)
            for mot in texte.split():
                if mot == "nation":
                    if element in dico_count:
                        dico_count[element]+=1
                    else:
                        dico_count[element]=1
            liste_pres = list(set(liste_des_presidents))  
            for key,valeurs in dico_count.items():
                if dico_count[key] > val_max:
                    val_max = dico_count[key]
                    clef=key  
    return ("Les presidents qui ont parler de 'Nation' sont {} et celui qui en a le plus parler est {} avec {} occurences.".format(liste_pres,clef,val_max))
def climat():# question 5 renvoie le nom du president qui parle le premier du climat 
    premier=""
    liste_des_presidents=[]
    L=[]
    val=7
    pres = {"Giscard dEstaing":1,"Mitterrand":2,"Chirac":3,"Sarkozy":4,"Hollande":5,"Macron":6}
    for fichier in list_of_files("./speeches",".txt") :
        f = open(f"cleaned/{fichier}","r",encoding="utf8")
        texte = f.read()
        if ("climatique" or "ecologie") in texte.split():
            L.append(fichier)
            for element in L:
                element = element [11:]
                element = element.replace(".txt","").replace("1","").replace("2","")
            liste_des_presidents.append(element)
            liste_pres = list(set(liste_des_presidents))  
            for key,valeurs in pres.items():
                if key in liste_pres :
                    if val > pres[key]:
                        val=pres[key]
                        premier=key
    return ("Le premier president a avoir parler du climat est {}".format(premier))
def mot_evoque():# renvoie les mots qui ont ete prononcer par tout les presidents
    liste_non_importants=min_idf()
    tab_des_mots=TF()
    pres = {"Giscard dEstaing":[],"Mitterrand":[],"Chirac":[],"Sarkozy":[],"Hollande":[],"Macron":[]}
    L=[]
    for fichier in list_of_files("./speeches",".txt") :
        f = open(f"cleaned/{fichier}","r",encoding="utf8")
        texte = f.read()
        file=fichier
        file = file[11:]
        file = file.replace(".txt","").replace("1","").replace("2","")
        for key,value in tab_des_mots.items():
            if key in texte.split() :
                for keys,values in pres.items():
                    if key not in pres[file]:
                        pres[file].append(key)
    for i in pres["Chirac"]:
        cpt=0
        for clef,valeurs in pres.items():
            if i in pres[clef] and i not in liste_non_importants:
                cpt+=1
        if cpt==len(pres):
            L.append(i)         
    return L
#----------------------------------------------------------------------------PARTIE_2----------------------------------------------------------------------------------------
def Creation_Question_Globale():
    global Question_Globale
    Question_Globale = input("rentre ta Question : ")
    return Question_Globale
def random_answer():
    Question = Question_Globale
    question_starters = {"Comment": "Après analyse, ","Pourquoi": "Car, ","Peux-tu": "Oui, bien sûr!","a" : "saloperie"}
    for key,valeur in question_starters.items():
        if key in Question :
            return valeur
    return ("Voici le mieux que je puisse faire : ")
def Creation_Question():# renvoie les mots qui ont ete prononcer par tout les presidents
    Question = Question_Globale
    Question = Question.lower()
    Question = modification(Question)      
    return Question
def Creation_TF_IDF_Question():
    Question = Creation_Question()
    pres = {}
    TF_Question={}
    for mot in Question.split() :
        if mot not in TF_Question:
            TF_Question[mot] = 1
        else:
            TF_Question[mot] += 1
    for clef,valeur in TF_Question.items():
        TF_Question[clef]=(valeur/len(Question.split())*IDF(clef))
    for fichier in list_of_files("./speeches",".txt") :
        f = open(f"cleaned/{fichier}","r",encoding="utf8")
        texte = f.read()
        pres[fichier]={}
        for mot_question in Question.split():
            if mot_question not in pres[fichier]:
                pres[fichier][mot_question]=0
        for words in texte.split():
            for keys,values in pres.items():
                if words in Question.split():
                    pres[fichier][words]+=1
    return TF_Question
def creation_TF_IDF_Question_dans_corpus():
    Question = Creation_Question()
    pres = {}
    for fichier in list_of_files("./speeches",".txt") :
        f = open(f"cleaned/{fichier}","r",encoding="utf8")
        texte = f.read()
        file=fichier
        file = file[11:]
        file = file.replace(".txt","")
        pres[file]={}
        for mot in Question.split():
            for key,value in pres.items():
                if mot not in pres[key]:
                    pres[key][mot] = TF_IDF_mot(mot,key)
    return pres
def produit_scalaire():
    vecteur_similaires = {}
    matrice_corpus = creation_TF_IDF_Question_dans_corpus()
    matrice_question = Creation_TF_IDF_Question()
    for key,val in matrice_corpus.items():
        cpt=0
        for clef,valeurs in matrice_corpus[key].items():
            cpt = cpt+valeurs*matrice_question[clef]
        vecteur_similaires[key] = cpt
    return vecteur_similaires
def norme_vecteur(matrice):
    compteur = 0
    for key,value in matrice.items():
        compteur = compteur + value**2
    return sqrt(compteur)
def cosinus_symilaritude():
    pres = {}
    scalaire = produit_scalaire()
    Question = Creation_TF_IDF_Question()
    matrice_textes = creation_TF_IDF_Question_dans_corpus()
    for fichier in list_of_files("./speeches",".txt") :
        f = open(f"cleaned/{fichier}","r",encoding="utf8")
        texte = f.read()
        file=fichier
        file = file[11:]
        file = file.replace(".txt","")
        if norme_vecteur(Question) != 0 and norme_vecteur(matrice_textes[file]) != 0 :
            pres[file] = scalaire[file]/(norme_vecteur(Question)*norme_vecteur(matrice_textes[file]))
        else :
            pres[file] = 0
    return pres
def max_cos(matrice1,matrice2):
    maxi1 = -100000
    clef1 = ""
    for key1,value1 in matrice1.items():
        if matrice1[key1] >= maxi1 :
            maxi1 = matrice1[key1]
            clef1 = key1
    maxi2 = -100000
    clef2 = ""
    for key2,value2 in matrice2.items():
        if matrice2[key2] >= maxi2 :
            maxi2 = matrice2[key2]
            clef2 = key2
    for fichier in list_of_files("./speeches",".txt") :
            if clef1 in fichier : 
                f = open(f"speeches/{fichier}","r",encoding="utf8")
                texte = f.read()
                phrase = ""
                for lettre in texte :
                    if lettre != ".":
                        phrase = phrase + lettre
                    else :
                        if clef2 in phrase :
                            return "Dans les textes c'est {} qui a le plus de ressemblance avec votre question avec un score de {} et le mot avec le plus grand TF-IDF est {} avec un score de {} est voici la premiere phrase ou il a été dit {}.".format(clef1,maxi1,clef2,maxi2,phrase)
                        else :
                            phrase = ""
    return "ALED"
