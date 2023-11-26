from function import *
import os 
intro()
print("Rentre la commande que tu veux entre :")
acces=int(input("1:mots les moins importants,2:mots les plus importants,3:mot le plus reter par un president,4:les presidents ayants parler de nation,5:le premier president qui a parler du climat,6:les mots dit par tout les presidents"))
while acces <1 or acces > 6:
    acces=int(input("1:mots les moins importants,2:mots les plus importants,3:mot le plus reter par un president,4:les presidents ayants parler de nation,5:le premier president qui a parler du climat,6:les mots dit par tout les presidents"))
    
if acces ==1:
    print(min_idf())
elif acces==2 :
    print(max_td_idf())
elif acces==3 :
    valeur=input("nom ou partie du nom du president souhaiter")
    print(mot_rep(valeur))
elif acces ==4:
    print(Nation())
elif acces == 5 :
    print(climat())
"""elif acces==6:
    print(mot_evoque())"""