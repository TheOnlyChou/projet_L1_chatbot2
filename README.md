# projet_L1_chatbot2                     
Chou-A-Wean Alias Lee-Hung-Hing  Alexandre; Djelassi-Doublet Théotim
Lien git : https://github.com/TheOnlyChou/projet_L1_chatbot2.git
## Les fonctions
- La fonction list_of_file sert permet de créer le fichier cleaned. En demandant à l'utilisateur s'il a déjà créé un fichier.
- La fonction list_of_files() fait la liste de tous les fichiers ".txt" de speeches
- La fonction modification() supprime tout caractère de ponctuation, si deux mots ont un tiret entre eux "-", si un mot est séparé par un "-" ex : modifi-cation on le laisse,
si on a un " ' " on le remplace par un "e" ou un "a".
- La fonction copie()  permet de copier un texte et de le modifier
- La fonction creation_cleaned() crée le du fichier "cleaned"
- La fonction ext_pres() extrait le du nom du président
- La fonction sans_doub() permet d'enlever les doublons pour les nom des présidents
- La fonction assoc() permet d'associer à chaque président un prénom(en reprenant la liste de nom des présidents sans les doublons)
- La fonction TF() sert a mettre dans un dico tout les mots avec le nombre de leurs occurrence
- La fonction IDF() revoie le log de chaque mot
- La TF_idf() revoie le TF-IDF de chaque mot sous forme de dictionnaire
- La fonction min_idf() renvoie la liste de tout les mots avec un IDF de 0 
- La fonction max_td_idf() question 2 renvoie les mots avec les TD-idf les plus haut 
- La fonction mot_rep(file_name) donne le mot qui a été le plus prononcer par un président sélectionner
- La fonction Nation() renvoie les présidents parlant de Nation et celui qui parle le plus de nation
- La fonction climat() renvoie le nom du président qui parle le premier du climat 
- La fonction mot_evoque() renvoie les mots qui ont été prononcer par tout les présidents
## La fonction principale
- Le main est comme une petite interface ou on exécute les fonction d'un autre fichier en rentrant des commandes cela permet d'optimiser la visibilité de l'utilisateur et de savoir qui s'exécute quand pour le programmeur
