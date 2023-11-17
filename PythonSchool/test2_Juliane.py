'''
Je comprends l'importance de l'intégrité professionnelle dans mes études et ma future carrière en génie, 
informatique ou autre. Je certifie par la présente que j'ai fait et ferai tout le travail pour cet examen
entièrement par moi-même, sans assistance extérieure ni utilisation de sources d'information non autorisées.
De plus, je ne fournirai aucune assistance aux autres. 
'''

# AJOUTEZ VOTRE NOM ET NUMERO D'ETUDIANT ICI
# pour confirmer que vous etes d'accord avec la declaration ci-dessus et avec les regles decrites dans TEST 2
# NOM: Juliane Bruck
# NUMERO D'ETUDIANT: --------


def list_work(l):  # 10 points
    '''(list of int)->list of int

    La fonction retourne une nouvelle liste avec la somme de chaque paire des elements
    consecutifs de la liste l si les elements de la paire sont tous les deux paires ou
    tous les deux impaire. Si une des deux valeurs est paire et l'autre impaire,
    un zero est ajoute dans la nouvelle liste.
    Par exemple, si la liste l=[1, 7, 5, 4, 12],
    1 et 7 sont impaires, donc on ajoute leur somme, 8, a la nouvelle liste
    7 et 5 sont impaires, donc on ajoute leur somme, 12, a la nouvelle liste
    5 et 4 sont un impaire et un paire, dons on ajute zero dans la nouvelle liste
    4 et 12 sont paires, donc on ajoute leur somme, 16, a la nouvelle liste
    La fonction retourne la liste [8, 12, 0, 16]

    Si la liste 1 a un seul element ou est vide, une copie de la liste l est retournee.

    >>> list_work([1, 7, 5, 4, 12, -33, 6])
    [8, 12, 0, 16, 0, 0]
    >>> list_work([1])
    [1]
    >>> list_work([])
    []
    >>> list_work([1,2,3,4,5])
    [0, 0, 0, 0]
    >>> list_work([100,20,30])
    [120, 50]

    Les memes commentaires en anglais si quelqun a besoin: 
    The function returns a new list where for every pair of consecutive elements in l
    if both are odd or both are even then the sum of the two elements is added to the new list
    otherwise zero is added to the new list. For example, in a list l=[1, 7, 5, 4, 12],
    1 and 7 are both odd, so we add their sum, 8, to the new list
    7 and 5 are both odd, so we add their sum, 12, to the list
    5 and 4 are neither both odd nor both even, so we add zero to the list
    4 and 12 are both even, so we add their sum, 16,  to the list.
    Thus the function returns the list [8, 12, 0, 16]
    If l has at most 1 element, then a copy of list l is returned
    '''

    # VOTRE CODE ICI
    sumList = []

    if(len(l) == 1):
        return list(l)

    for i in range(0, len(l)-1):
        first = l[i]
        second = l[i+1]
        if(first % 2 == 0 and second % 2 == 0) or (first % 2 == 1 and second % 2 == 1):
            sumList.append(first + second)
        else:
            sumList.append(0)
    return sumList


def pattern_to_stars(s, p):  # 10 points
    '''(str, str)->str

    Precondition: p n'est pas une chaine vide et tous les lettres sont en minuscules

    Pour les chaines des caracteres s et p, la fonction retourne une nouvelle chaine ou
    le premiere occurrance du modele p on s est remplacee par une etoile,
    la deuxieme occurrance aves deux etoiles, et on continue comme ca. 

    On fait l'hypothese qu'il n'y a pas des modeles p en s qui se chevauchent. Par exemple:
    p="aa" s="aaab" n'arrive pas parce que il y a deux modeles chevauches "aa" en s,
    il y a un "aa" en position 0 et un "aa" en position 1.

    Ce n’est pas permis d’utiliser la méthode replace du module str. 
    Si c'est utilisee, la note sera zero pour cette fonction.

    Indices: 
    - pour un entier x, x*"*" en Python donne une chaine de caracteres avec x etoiles 
    - fragments de chaines (:) peut aider dans cette question
    - une boucle while peut aider

    >>> pattern_to_stars("trabsabtt", "ab")
    'tr*s**tt'
    >>> pattern_to_stars("today123is123nice123d", '123')
    'today*is**nice***d'
    >>> pattern_to_stars("1a2b3", '123')
    '1a2b3'
    >>> pattern_to_stars("chipchip", 'chip')
    '***'
    >>> pattern_to_stars('', 'chip')
    ''

    Les memes commentaires en anglais si quelqun a besoin:
    Precondition: p is not an empty string and all letters are lower-case
                                                                                Given a string s and another string p the function returns a new string where
                                                                                the first occurrence of p is replaced with one star, the second occurance with two starts
                                                                                and so on.      
                                                                                You may assume that no two patterns p in s overlap in s. Example:
                                                                                p="aa" s="aaab" cannot happen since "aa" pattern in the first two positions
                                                                                overlaps with "aa" pattern in the next two positions in s
    You CANNOT use the replace method from str module.
    Using that method will result in receiving zero for this function.
    Hints:
    - slicing may be helpful in this question
    - it may be easier to solve this problem with a while loop
    '''

    # VOTRE CODE ICI
    numOccurences = s.count(p)

    newString = ""

    firstIndex = 0
    foundSubstringIndex = s.find(p)
    starCount = 1

    while foundSubstringIndex > -1 and firstIndex < len(s):
        newString = newString + \
            s[firstIndex:foundSubstringIndex] + ("*" * starCount)
        firstIndex = foundSubstringIndex+len(p)
        remainder = s[firstIndex:-1]
        if(remainder == ""):
            break
        remainderIndex = remainder.find(p)
        foundSubstringIndex = firstIndex + remainderIndex
        starCount += 1
    return newString


def get_list_ofint(s):  # 5 points
    '''(str)->list of int
    Precondition: s est une chaine des caracteres qui contient une sequence des entiers
    separees par une virgule suivi par un espace ou seulement par un espace. 
    La chaine s n;est pas vide et a au moins une sub-chaine qui resemble un entier

    Retourne une liste des entiers a partir de s

    >>> get_list_ofint("10 22, 7 0 -5, 1")
    [10, 22, 7, 0, -5, 1]
    >>> get_list_ofint("231, -5, 12")
    [231, -5, 12]
    >>> get_list_ofint("231 -5 -7")
    [231, -5, -7]
    >>> get_list_ofint("-7,")
    [-7]

    Les memes commentaires en anglais si quelqun a besoin:
    Precondition: s string that looks like a sequence in integers separated
    by a space or a comma followed by a space.
    More preconditions: s has at least one substring that looks like an integer
    Returns a list of integers from s
    '''

    # VOTRE CODE ICI

    newList = []

    currentNumber = ""
    for i in range(0, len(s)):
        char = s[i]
        if (char == " " or char == ","):
            if (not(currentNumber == "")):
                newList.append(int(currentNumber))
                currentNumber = ""
        else:
            currentNumber += s[i]

    if (not(currentNumber == "")):
        newList.append(int(currentNumber))
    return newList


# main
print("Entrez A ou B pour choisir une des deux options suivantes:\n")
print("A: Travailler avec des nombres?")
print("B: Ajouter des etoiles dans une chaine des caracteres?\n")

answer = input("Entrez A ou B (en majuscules ou minuscules): ")


# 5 points
# Ajoutez ici votre code pour continuer de demander a l'usager d'entrer
# "A" ou "B" jusqu'au la valeur entree est bonne. Votre solution
# doit accepter des majuscule ou des minuscule et eliminer les espaces
# supplementaires s'il y en a.
# Voir test2_RUN.txt pour des exemples d'execution.

# Les memes commentaires en anglais si quelqun a besoin:
# You should code here a part where your program keeps on asking
# the user for "A" or "B" until the user finally enters it. Your solution
# should accept lower case and upper case A or B and it should
# should remove any extra white space.


# VOTRE CODE ICI:

validInput = False
while not(validInput):
    answer = answer.lower()
    validInput = (answer == "a" or answer == "b")
    if(not (validInput)):
        print("Entree invalide")
        answer = input("Entrez A ou B (en majuscules ou minuscules): ")


if answer == "a":
    rawl = input(
        "Entrez une sequence des entiers separes par un espace ou une virgule suivi par un espace.\n")
    print("Vous avez entre:", rawl)
    givenl = get_list_ofint(rawl)
    print("La liste des entiers dans la sequence est", givenl)
    print("La liste apres le travail est", list_work(givenl))

else:
    s = input("Entrez une chaine de caracteres: ").lower()
    p = input("Entrez un modele p (pas vide): ").lower()
    print("Voici le resultat apres remplacer le modele",
          p, "en", s, "avec des etoiles:")
    print(pattern_to_stars(s, p))
