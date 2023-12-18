# Readme                      
Chou-A-Wean Alias Lee-Hung-Hing  Alexandre; Djelassi-Doublet Théotim
Lien git : https://github.com/TheOnlyChou/pychatbot-chou-a-wean-djelassi-E.git
## Les fonctions
- La fonction list_of_files() fait la liste de tous les fichiers ".txt" de speeches
- La fonction modification() supprime tout caractère de ponctuation, si deux mots ont un tiret entre eux "-", si un mot est séparé par un "-" ex : modifi-cation on le laisse, si on a un " ' " on le remplace par un "e" ou un "a".
- La fonction copie_minuscule() permet de coller le texte qu'on a copié du dossier speeches dans cleaned on lui appliquant les modifications.
- La fonction creation_Nomination_cleaned() crée des nouveaux fichiers dans cleaned avec   le nom que ceux de speeches.
- La fonction creation_folder_cleaned() crée un dossier cleaned s'il n'existe pas.
- La fonction ext_pres() extrait le du nom du président de chaque fichier texte.
- La fonction assoc() permet d'associer à chaque président un prénom (en reprenant la liste de nom des présidents sans les doublons).
- La fonction TF() permet de mettre dans un dico tous les mots avec leurs nombre d'occurrence.
- La fonction IDF() revoie la fréquence (logarithme) de chaque mot.
- La fonction TF_idf() revoie le TF-IDF de chaque mot sous forme de dictionnaire.
- La fonction min_idf() renvoie la liste de tout les mots avec un IDF de 0. 
- La fonction max_td_idf() renvoie les mots avec les TD-idf les plus haut. 
- La fonction mot_rep(file_name) donne le mot qui a été le plus prononcer par un président.
- La fonction Nation() renvoie les présidents qui ont parlé de la nation et celui qui a le plus parler de nation.
- La fonction climat() renvoie le nom du président qui parle le premier du climat.
- La fonction mot_evoque() renvoie les mots qui ont été prononcer par tous les présidents.
- La fonction Creation_Question_Globale() demande à l'utilisateur de rentrer sa question.
- La fonction random_answer() affiche du texte un plus en fonction de la formulation de l'auteur.
- La fonction Creation_Question() modifie la question saisie par l'utilisateur (Creation_Question_Globale()) et applique des modifications (modification()).
- La fonction Creation_TF_IDF_Question() crée un dictionnaire indiquant la fréquence de chaque mot dans la question.
- La fonction creation_TF_IDF_Question_dans_corpus() crée un dictionnaire associant les mots de la question à leurs TF-IDF dans le corpus en lien avec la fonction.
- La fonction produit_scalaire() donne une matrice associant les noms des textes de nomination à la somme pondérée des TF-IDF des mots dans le texte d'un président par les TF-IDF correspondants dans la question.
- La fonction norme_vecteur(matrice) calcule la norme d'une matrice en prenant la racine carrée de la somme des carrés de toutes ses valeurs.
- La fonction cosinus_symilaritude() calcule la similarité entre le vecteur de la question et chaque ligne (vecteur) parmi les N vecteurs de la matrice TF-IDF. Identifie ensuite le document avec lequel la question a la plus grande similarité.

## La fonction principale
- Le main est comme une petite interface ou on exécute les fonction d'un autre fichier en rentrant des commandes cela permet d'optimiser la visibilité de l'utilisateur et de savoir ce qui s'exécute. 
- Le 1 : Renvoie les mots avec un TF-IDF de 0.
- Le 2 : Les mots ayant le plus grand TF-IDF.
- Le 3 : Après avoir rentré une partie du nom d’un président français renvoie le mot qui a été le plus dit par celui-ci .
- Le 4 : Donne une liste des noms de tous les présidents ayant parlé de “Nation” ainsi que le nom de celui qui en a le plus parlé avec le nombre de fois qu’il l’a dit.
- Le 5 : Renvoie le nom du président ayant chronologiquement parler en premier du climat (en l'occurrence ici des mots ‘climatique’ ou ‘ecologie’).
- Le 6 : Renvoie une liste de tous les mots ayant été dit par tous les présidents au moins une fois.
- Le 7 : Renvoie le dictionnaire du TF-IDF de tous les mots du corpus.
- e 8 : Vous demande de poser une question et renvoie le nom du président avec le plus de compatibilité entre votre question et son texte de Nomination ainsi que la phrase dans lequel le mot a été dit pour la première fois par ce président.  
- Le 9 : Renvoie toutes les questions précédentes dans le même ordre.
