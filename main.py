from function import *
import os 
if not os.path.exists("cleaned"):
    creation_folder_cleaned()
print("Rentre la commande que tu veux entre :")
acces=int(input("1. Mots les moins importants : \n"
                "2. mots les plus importants : \n"
                "3. mot le plus reter par un president : \n"
                "4. les presidents ayants parler de nation : \n"
                "5. le premier president qui a parler du climat : \n"
                "6. les mots dit par tout les presidents : \n"
                "7. Afficher TF-IDF : \n"
                "8. Chercher la réponse a une question . : \n"
                "9. ALL : \n"))
while acces <1 or acces > 9:
    acces=int(input("1. Mots les moins importants : \n"
                "2. mots les plus importants : \n"
                "3. mot le plus reter par un president : \n"
                "4. les presidents ayants parler de nation : \n"
                "5. le premier president qui a parler du climat : \n"
                "6. les mots dit par tout les presidents : \n"
                "7. Afficher TF-IDF : \n"
                "8. Chercher la réponse a une question . : \n"
                "9. ALL : \n"))
if acces == 1:
    print(min_idf())
elif acces == 2 :
    print(max_td_idf())
elif acces == 3 :
    valeur=input("nom ou partie du nom du president souhaiter : ")
    print(mot_rep(valeur))
elif acces == 4:
    print(Nation())
elif acces == 5 :
    print(climat())
elif acces == 6:
    print(mot_evoque())
elif acces == 7 :
    print(TF_idf())
elif acces == 8:
    Creation_Question_Globale()
    print(random_answer() +" "+max_cos(cosinus_symilaritude(),Creation_TF_IDF_Question()))
elif acces == 9 :
    print(min_idf())
    print(max_td_idf())
    valeur=input("nom ou partie du nom du president souhaiter : ")
    print(mot_rep(valeur))
    print(Nation())
    print(climat())
    print(mot_evoque())
    print(TF_idf())
    Creation_Question_Globale()
    print(random_answer() +" "+max_cos(cosinus_symilaritude(),Creation_TF_IDF_Question()))

#"Peux-tu me dire comment une nation peut-elle prendre soin du climat ?"

