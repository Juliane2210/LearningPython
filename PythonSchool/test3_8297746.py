'''
Je comprends l'importance de l'intégrité professionnelle dans mes études et ma future carrière en génie, 
informatique ou autre. Je certifie par la présente que j'ai fait et ferai tout le travail pour cet examen
entièrement par moi-même, sans assistance extérieure ni utilisation de sources d'information non autorisées.
De plus, je ne fournirai aucune assistance aux autres. 
'''

# AJOUTEZ VOTRE NOM ET NUMERO D'ETUDIANT ICI
# pour confirmer que vous etes d'accord avec la declaration ci-dessus et avec les regles decrites dans TEST 2
# NOM: Juliane Bruck
# NUMERO D'ETUDIANT: 8297746


def dragonfly(y, b):
    y[1] = 0
    b = 700
    z = y
    z[0] = 1000
    print("bye dragonfly")


x = [1, 2, 3]
a = 200
dragonfly(x, a)


#########################
# QUESTION 1:
#########################
# QUESTION 1A)
#########################
# Imaginez que ce programme s'execute et l'execution est
# juste avant la ligne print("bye dragonfly").
# Laquelle des propositions suivantes est vrais au sujet des variables x, y, z?
# (reference au meme objet signifie la meme adresse dans la memoire)
# A) les trois variables x, y, z sont des references au meme objet
# B) x et y sont des references au meme objet et z a un objet different
# C) x et z sont des references au meme objet et y a un objet different
# D) y et z sont des references au meme object et x a un objet different
# E) les trois 3 variables sont des references a tois objets differents

# ECRIVEZ A, B, C, D ou E comme votre reponse dans la ligne suivante:
# REPONSE: A

# A


# Les memes commentaires en anglais si quelqun a besoin:
# Imagine this program is running and it is about the print "bye dragonfly".
# Which of the follow is true about variables x, y and z
# A) all three variables x, y and z refer to a same object
# B) x and y refer to a same object and z to a different object
# C) x and z refer to a same object and y to a different object
# D) y and z refer to a same object and x to a different object
# E) the 3 variables refer to three distinct objects


#########################
# QUESTION 1B)
#########################
# Imaginez que ce programme s'execute et l'execution est
# juste avant la ligne print("bye dragonfly").
# Laquelle des propositions suivantes est vrais au sujet des variables a, b?
# A) les deux variables a et b ont des references au meme objet
# B) a et b sont des references a deux objets differents
#
# ECRIVEZ A ou B comme votre reponse dans la ligne suivante:
# REPONSE: B

# B

# Les memes commentaires en anglais si quelqun a besoin:
# Imagine this program is running and it is about the print "bye dragonfly".
# Which of the follow is true about variables a and b
# A) both a and b refer to a same object
# B) a and b refer to two distinct objects


def mantis(L):
    '''(list of int)->None'''
    n = len(L)
    for i in range(n):
        L[i] = L[i]**2
    print("Les elements de L sont:")
    for i in range(n):
        print(L[i])

#########################
# QUESTION 2:
#########################
# QUESTION 2A)
#########################
# Quel est l'ordre de complexite (le nombre approximatif des operations executes)
# pour la fonction mantis si la liste a n elements?
# A) O(1)
# B) O(log n)
# C) O(n)
# D) O(n*log n)
# E) O(n^2)

# ECRIVEZ A, B, C, D ou E comme votre reponse dans la ligne suivante:
# REPONSE: C


# C


# Les memes commentaires en anglais si quelqun a besoin:
# What is the running-time (i.e., a rough number of operations) of
# function mantis on a list with n elements

#########################
# QUESTION 2B)
#########################

# Imaginez qu'on remplace n dans la deuxieme fonction range avec le nombre 10.
# Quel est l'ordre de complexite de la fonction mantis apres ce changement?
# A) O(1)
# B) O(log n)
# C) O(n)
# D) O(n*log n)
# E) O(n^2)

# ECRIVEZ A, B, C, D ou E comme votre reponse dans la ligne suivante:
# REPONSE: A

# A

# Les memes commentaires en anglais si quelqun a besoin:
# What is the running-time of function mantis with that change?

#########################
# QUESTION 3
#########################


def diff_start_end(l, q):
    '''(list of int, list of int) -> (int, int)

    l et q sont deux listes qui ne sont pas identiques (elles n'ont pas les
    memes elements) mais elles ont la meme taille, len(l)==len(q)
    La fonction retourne un tuple avec deux entiers:
      - le premier entier et l'index ou l et q sont differents pour la premiere fois
      - le deuxieme entier et l'index ou l et q sont differents pour la derniere fois.
        Cet index devrait etre NEGATIVE (commence a la fin des listes)

    Preconditions: len(l)==len(q)>=1, et l != q

    >>> diff_start_end([0,1,6,0,7,2,3,4], [0,1,8,0,9,2,3,4])
    (2, -4)
    >>> diff_start_end([6],[8])
    (0, -1)
    >>> diff_start_end([0,0,0,1,0],[0,0,0,22,0])
    (3, -2)
    >>> diff_start_end([0,1,1],[1,1,1])
    (0, -3)
    >>> diff_start_end([0,1,1,0],[0,0,0,0])
    (1, -2)

    Les memes commentaires en anglais si quelqun a besoin: 
    l and q are two parallel lists i.e., len(l)==len(q)
    The function returns the following two integers (i.e. a tuple with
    the following two integers).
      - the index where l and q first differ, and
      - the index where l and q last differ. This index should be NEGATIVE
    '''

    # YOUR CODE GOES HERE

    firstDifferIndex = 0
    lastDifferentIndex = 0

    for i in range(0, len(q)):
        if l[i] != q[i]:
            firstDifferIndex = i
            break

    backCount = 1
    backIndex = len(q) - 1
    while backIndex >= 0:
        if l[backIndex] != q[backIndex]:
            lastDifferentIndex = backCount
            break
        backIndex -= 1
        backCount += 1

    result = (firstDifferIndex, -1 * lastDifferentIndex)

    return result


# print(diff_start_end([6], [8]))


#########################
# QUESTION 4
#########################
def make_teams(players, num_teams):
    '''(list of str, int)->2D list 
    La fonction produit num_teams equipes a partir des jouers de la liste donnee players,
    comme dans les exemples suivantes.
    Players est une liste de noms des jouers et num_teams est le nombre d'equipes a former.
    La fonction retourne une liste 2D ou chaque sou-liste represente une equipe.
    Preconditions: num_teams>= 1

    >>> make_teams(["pele", "maradona", "serena", "venus", "fed", "rafa", "lionel"], 3)
    [['pele', 'venus', 'lionel'], ['maradona', 'fed'], ['serena', 'rafa']]
    >>> make_teams(["pele", "maradona", "serena", "venus", "fed", "rafa", "lionel"], 2)
    [['pele', 'serena', 'fed', 'lionel'], ['maradona', 'venus', 'rafa']]
    >>> make_teams(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 3)
    [['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9']]
    >>> make_teams(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 1)
    [['1', '2', '3', '4', '5', '6', '7', '8', '9']]
    >>> make_teams(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 4)
    [['1', '5', '9'], ['2', '6'], ['3', '7'], ['4', '8']]
    >>> make_teams(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 7)
    [['1', '8'], ['2', '9'], ['3'], ['4'], ['5'], ['6'], ['7']]
    >>> make_teams(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 11)
    [['1'], ['2'], ['3'], ['4'], ['5'], ['6'], ['7'], ['8'], ['9'], [], []]
    >>> make_teams( [] , 3)
    [[], [], []]

    Les memes commentaires en anglais si quelqun a besoin:
    Make num_teams teams out of the players in list players by counting off.
    Players is a list of players' names and num_teams is the desired number of teams
    Return a 2D list where each sublist is representing a team.
    Preconditions: num_teams>= 1
    '''

    # YOUR CODE GOES HERE

    finalTeam = [[] for r in range(num_teams)]
    for i in range(0, len(players)):
        player = players[i]
        team = i % num_teams
        finalTeam[team].append(player)

    return finalTeam


# print(make_teams([], 3))


#########################
# QUESTION 5
#########################
def draw_w_stars(n):
    '''(int)->None
    Preconditions: n est un entier positive impaire
    La fonction imprime un dessin comme decrit dans la Question 5
    avec n etoiles dans la premiere ligne et dans la derniere ligne

    Les memes commentaires en anglais si quelqun a besoin:
    Draws a figure as depicted in Question 5 with n stars in top and bottom raws
    '''

    # YOUR CODE GOES HERE

    starCount = 0
    for i in range(0, n//2):
        starline = '*' * (n - starCount)
        blanks = ' ' * i
        starCount += 2
        finalLine = blanks + starline + blanks
        print(finalLine)

    numStars = 1
    for i in range(0, n//2+1):
        starline = '*' * numStars
        numStars += 2
        blanks = ' ' * (n//2 - i)
        finalLine = blanks + starline + blanks
        print(finalLine)


draw_w_stars(1)
