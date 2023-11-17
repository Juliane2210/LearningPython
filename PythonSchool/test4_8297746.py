'''
Je comprends l'importance de l'intégrité professionnelle dans mes études et ma future carrière en génie,
informatique ou autre. Je certifie par la présente que j'ai fait et ferai tout le travail pour cet examen
entièrement par moi-même, sans assistance extérieure ni utilisation de sources d'information non autorisées.
De plus, je ne fournirai aucune assistance aux autres.
'''

# AJOUTEZ VOTRE NOM ET NUMERO D'ETUDIANT ICI
# pour confirmer que vous etes d'accord avec la declaration ci-dessus et avec les regles decrites dans TEST 2
# NOM: Juliane Bruck
# NUMERO D'ETUDIANT: -------

#########################
# QUESTION 1
#########################
# Compeletez dans les classes suivantes dans les endroit indiquees
# Voir deux exemples d’exécution du programme principal dans les
# fichiers exemple_run1.txt et exemple_run2.txt


class Livre:
    ''' Un livre a un titre et un auteur'''

    def __init__(self, titre, auteur):
        '''
        (str,str)-> None
        constructeur
        '''
        self.titre = titre
        self.auteur = auteur

    def __repr__(self):
        '''
        (None)->str
        retourne une representation de l'objet: titre et auteur

        En anglais: return a string that describes the object by title and author
        '''

        # VOTRE CODE ICI
        return 'Titre:' + self.titre + ', Auteur:' + self.auteur

    def __eq__(self, autre):
        '''
        (Livre)->bool
        self == autre si le titre et auteur sont les memes
        Retourne True si les deux objets ont le meme titre et auteur

        En anglais: return True if the two objects have teh same title and author
        '''
        # VOTRE CODE ICI
        return self.titre == autre.titre and self.auteur == autre.auteur


class Personne:
    '''Une Personne a un nom, un prenom, un numero de carte de membre
    au club de lecture, et une liste des livres lu
    '''

    def __init__(self, nom, prenom, nr):
        '''(str,str,int)->None
        initialise les attributs de la classe Personne
        la liste de livre est initialise a la liste vide
        '''
        self.nom = nom
        self.prenom = prenom
        self.cardNo = nr
        self.listLivres = []

    def __repr__(self):
        '''(None)->str
        retourne une representation de l'objet: nom, prenom et numero de carte

        En anglais: return a string that describes the object by last name, first name
        and card number'''

        # VOTRE CODE ICI
        return 'Prenom:' + self.prenom + ', Nom:' + self.nom + ', CardNo:' + str(self.cardNo)

    def __eq__(self, autre):
        '''(Personne)->bool
        self == autre si le nom, le prenom, et le numero de carte sont les memes
        Retourne True si les deux objets ont le meme nom, prenom, et numero de carte

        En anglais: return True if the two objects have the same last name, first name and card number
        '''

        # VOTRE CODE ICI
        return self.prenom == autre.prenom and self.nom == autre.nom and self.cardNo == autre.cardNo

    def ajouteLivre(self):
        '''
        (None)-> bool
        ajoute un livre a la liste des lives lu par la personne.
        Lit du clavier le titre et l'auteur d'un livre et cree un object de type Livre.
        Ajoute l'objet a la liste s'il n'y a pas deja un livre avec le meme titre et
        auteur dans la liste (utilisez __eq__ pour tester ca).
        Retourne True si le livre a ete ajoute et False sinon.

        En anglais: Add a book to the list of books read by the person. The title and
        author are read from the keyboard. If another book with the same title and author
        exists in the list, it shoud not add it. Returns True if the book was added and False if not.
        '''

        # VOTRE CODE ICI
        auteur = input("Entrez l'auteur: ")
        titre = input("Entrez le titre: ")
        livre = Livre(titre, auteur)
        ajout = False

        # Note:  "in" will execute __eq__ internally. no need to call it explicitly
        if livre not in self.listLivres:
            self.listLivres.append(livre)
            ajout = True
        return ajout

    def afficheLivresLu(self):
        '''
        (None)-> None
        Affiche tous les livres lu par la personne, un livre sur chaque ligne

        En anglais: prints the books read by the person, one per line
        '''

        # VOTRE CODE ICI
        for livre in self.listLivres:
            print(livre)


class ClubLecture():
    '''represente une classe club de lecture avec une liste des Personnes inscrites'''

    def __init__(self):
        '''(None)->None
        initialise la classe
        la liste de personnes est initialise a la liste vide
        '''
        self.listMembres = []

    def ajoutePersonne(self):
        '''
        (None)-> bool
        Ajoute un membre au club de lecture.
        Lit du clavier le nom, prenom, et numero de carte de membre.
        Cree un object de type Personne.
        Ajoute l'objet a la liste s'il n'y a pas deja une personne avec le meme nom,
        prenom, et nuemro de carte dans la liste (utilisez __eq__ pour tester ca).
        Retourne True si le livre a ete ajoute et False sinon.

        En anglais: Add a person to the list of club members.
        The last name, first name and card number are read from the keyboard. If another person
        with the same last name, first name and card number exists in the list, it shoud not add it.
        Returns True if the person was added and False if not.
        '''

        # VOTRE CODE ICI

        nom = input("Entrez le nom: ")
        prenom = input("Entrez le prenom: ")
        nr = int(input("Entrez votre numero de carte: "))
        person = Personne(nom, prenom, nr)

        ajout = False

        # Note:  "in" will execute __eq__ internally. no need to call it explicitly
        if person not in self.listMembres:
            self.listMembres.append(person)
            ajout = True
        return ajout

    def livreLePlusPopulaire(self):
        '''
        (None)-> None
        Cette fonction est plus diffcile a ecrire. C'est bon resoudre Questions 2 et 3 et revenir.

        La fonction trouve le livre qui a ete lu par le plus grand nombre des membres au club.
        S'il y a plusieurs livres avec le meme nombre des lecteurs, choisissez le premier livre.
        Affichez le titre et l'auteur de ce livre dans quel format vous preferez.
        Vous avez besoin d'une structure de donnee pour compter le nombre des lecteurs de
        chaque livre, par exemple un dictionnaire avec des cled titre+"/"+auteur

        En anglais: This function is more difficult to implement. You can solve questions 2
        and 3 first.
        The function looks for the book that was read by te highest number of club members and
        prints its title and author in any format you prefer.
        If there are several books with the same number of readers, print the first book.
        You may need a data structure to count how many persons read each book, for example a dictionary.
        '''

        # VOTRE CODE ICI

        readersDict = {}

        for person in self.listMembres:
            for book in person.listLivres:
                readersDict[person.cardNo] = book

        for cardNo in readersDict:
            print(f"{cardNo}  { readersDict[cardNo]}")


# programme principal
c = ClubLecture()
print("On ajoute des membres au club")
# ajoute 3 membres et affiche le club
c.ajoutePersonne()
c.ajoutePersonne()
c.ajoutePersonne()
for v in c.listMembres:
    print(v)

print("Ajoutez des livres pour chaque membre")
for v in c.listMembres:
    print(v)
    encore = "oui"
    while encore == "oui":
        v.ajouteLivre()
        encore = input("Encore un livre? (oui/non) ")

for v in c.listMembres:
    v.afficheLivresLu()

c.livreLePlusPopulaire()


#########################
# QUESTION 2
#########################
def sommeLRec(l, n):
    ''' (list, int) -> number
    La fonction prend une liste et sa taille comme parametres
    et retourne la somme des elements avec de valeurs paire.
    La focntion doit etre recursive (sinon la note sera zero pour la fonction).
    Exemples:
    >>> l=[1,2,5,6,4]
    >>> sommeLRec(l, len(l))
    12
    >>> l=[1,3]
    >>> sommeLRec(l, len(l))
    0
    >>> l=[]
    >>> sommeLRec(l, len(l))
    0
    >>> l=[2,4,8]
    >>> sommeLRec(l, len(l))
    14

    Les memes commentaires en anglais si quelqun a besoin:
    The function takes a list and its lenghts as parameters
    and returns the sum of the elements of even values.
    The fonction should be recursive (or the number of points will be zero)
    '''

    # VOTRE CODE ICI
    if (n == 0):
        sum = 0
    else:
        if l[n-1] % 2 == 0:
            sum = sommeLRec(l, n-1) + l[n-1]
        else:
            sum = sommeLRec(l, n-1)

    return sum


# l = [2, 4, 8]
# print(sommeLRec(l, len(l)))


#########################
# QUESTION 3
#########################

def drawStarsUp(n):
    for i in range(3, n+1, 2):
        starCount = i
        print('*' * starCount)


# This is the recursive part.
def drawStarsDown(n):
    if (n >= 1):
        print('*' * n)
        drawStarsDown(n-2)


def draw_stars_rec(n):
    '''(int)->None
    Preconditions: n est un entier positive impaire
    La fonction imprime un dessin comme decrit dans la Question 3
    avec n etoiles dans la premiere ligne et dans la derniere ligne,
    n-2 etoiles dans la ligne prochaine, etc.
    La fonction doit etre recursive (sinon zero points)

    Les memes commentaires en anglais si quelqun a besoin:
    This fonction draws a pattern of stars. n is a positive integer of odd value.
    For example, if n is 9, it prints 9 stars on the first line, followed by 7,5,3,1,3,5,7,9 stars
    The function should be recursive (or the number of points will be zero)
    '''

    # VOTRE CODE ICI
    drawStarsDown(n)
    drawStarsUp(n)
