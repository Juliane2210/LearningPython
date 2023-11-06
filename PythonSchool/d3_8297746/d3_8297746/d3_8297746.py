# Juliane Bruck
# 8297746
# Devoir 3
#


# 1- fonction qui prends un entier et retourne la somme de tous ses diviseurs impairs
# Contrat de la fonction:
# (int)-> (int)
# si n=0 : (int)-> (none)
# Variables:
# n (int)
# Variables intermédiaires:
# oddDivisorsSum (int)
# allDivisors(int)


def somme_diviseurs_impaires(n):
    oddDivisorsSum = 0
    allDivisors = []
    if(n == 0):
        return None

    for i in range(1, abs(n)+1):
        if((n % i) == 0):
            allDivisors.append(i)

    for divisor in allDivisors:
        if((divisor % 2) == 1):
            oddDivisorsSum += divisor

    return oddDivisorsSum


# 2- Fonction qui prend un entier positif et retourne la somme d'une série donnée
# Contrat de la fonction:
# (int)->(float)
# Variables:
# n(int)
# Variables intermédiaires:
# sumOfSeries (float)

def somme_de_serie():
    n = int(input("SVP entrez un entier pas negatif: "))
    sumOfSeries = 1000
    if n < 0:
        return None

    for i in range(1, n+1):
        sumOfSeries = sumOfSeries + 1 / ((i)**2)

    return sumOfSeries


# 3- Fonction qui prends une liste d'entiers et fait la somme des elements de la liste divisibles par deux
# Contrat de la fonction:
# (int)->(int)
# Variables:
# l (liste de int)
# Variables intermédiaires:
# sum (int)


def somme_liste_div2(l):
    sum = 0
    for wholeNumber in l:
        if(wholeNumber % 2 == 0):
            sum = sum + wholeNumber
    return sum


# 4- Fonction qui compare une chaine de characteres avec une liste de characteres dit 'speciaux'
# et puis compte le nombre de characteres speciaux dans la chaine de characteres
# Contrat de la fonction:
# (str)-> (int)
# Variables:
# s (str)


def countMembers(s: str) -> int:
    totalSpecialCharacters = 0
    specialCharacterList = "efghijFGHIJKLMNOPQRSTUVWX23456!,\\"

    for character in s:
        if(character in specialCharacterList):
            totalSpecialCharacters = totalSpecialCharacters + 1

    return totalSpecialCharacters


# 5- Fonction qui prends une chaine de characteres et qui la transforme en l'entier que represente cette chaine
# Contrat de la fonction:
# (str)->(int)
# Variables:
# s(str)
# newString (str)
# L'on cree une nouvelle chaine de characteres en passant par chaque charactere de la chaine d'entree
# et en enlevant les espaces.
# Nous verifions aussi si il y a des - mais seulement au debut de la chaine

def nombre(s: str) -> str:

    digits = "0123456789"
    newString = ""
    lengthInput = len(s)

    # cas special avec entree vide
    if(lengthInput == 0):
        return "0"

    for i in range(0, lengthInput):
        #  "-"" valide seulement si au debut
        if((s[i] == "-") and i == 0):
            newString = newString + s[i]
        elif (s[i] in digits):
            newString = newString + s[i]
        elif (s[i] == " "):
            # ne fait rien, enleve les espaces
            pass
        else:
            return ""

    return newString


# 6- Fonction qui 'traduit' une chaine de charactere en nombres selon un tableau (language extraterrestre)
# Contrat de la fonction:
# (str)->(int)
# Variables:
# s(str)
# totalValue(int)
#


def alienNumbers(s: str) -> int:

    symbols = ['T', 'y', '!', 'a', 'N', 'U']
    values = [1024, 598, 121, 42, 6, 1]

    totalValue = 0

    for i in range(0, len(symbols)):
        totalValue += s.count(symbols[i]) * values[i]

    return totalValue


# 7- Fonction qui fait la meme chose qu'au 6 mais sans utiliser 'count'
# Contrat de la fonction:
# (str)->(int)
# Variables:
# s(str)
# totalValue (int)


def alienNumbers2(s: str) -> int:

    symbols = ['T', 'y', '!', 'a', 'N', 'U']
    values = [1024, 598, 121, 42, 6, 1]

    totalValue = 0

    for character in s:
        # verifie le nombre de fois qu'apparait un symbole extraterrestre dans l'entree s
        for i in range(0, len(symbols)):
            if(character == symbols[i]):
                totalValue += values[i]

    return totalValue


# 8- Cette fonction prends une sequence de characteres et retourne une version cryptee
# (le dernier charactere devient premier, le premier devient second, avant dernier devient 3e,
#  et 2e devient 4e...ainsi de suite)
# Contrat de la fonction:
# (str)-> (str)
# Variables:
# s(str)
# encrypted (str)


def encrypt(s: str):

    encrypted = ""
    backwardIndex = len(s) - 1
    forwardIndex = 0
    while forwardIndex <= backwardIndex:
        char1 = s[backwardIndex]
        char2 = s[forwardIndex]

        # pour un nombre impair d'elements on ne veux pas dupliquer le meme charactere et l'inserer deux fois
        if(backwardIndex == forwardIndex):
            encrypted = encrypted + char1
        else:
            encrypted = encrypted + char1 + char2

        backwardIndex -= 1
        forwardIndex += 1

    return encrypted


# 9- fonction retourne la chaine de charactere entree mais avec des o et p inserees entre les paires de characteres
# evalues si les valeurs de ces characteres sont alphanumeriques
# Contrat de la fonction:
# (str)-> (str)
# Variables:
# s(str), weave (str)

def weaveop(s):
    weave = ""

    for i in range(0, len(s)):
        char1 = s[i]

        char2 = ""
        # il faut faire attention de ne pas aller au-dela des indexs possibles pour s sinon, erreur.
        if(i < len(s) - 1):
            char2 = s[i+1]

        weave += char1

        # print(f" char1 { char1}  {char1.isalpha()} {char2} {char2.isalpha()} ")
        if (char1.isalpha() and char2.isalpha()):
            if(char1.isupper()):
                weave += "O"
            elif char1.islower():
                weave += "o"

            if(char2.isupper()):
                weave += "P"
            elif(char2.islower()):
                weave += "p"

    return weave


# 10- cette fonction trouve deux 'mots' consecutifs dans la chaine de characteres et retourne false si trouve
# Contrat de la fonction:
# (str)->(bool)
# Variables:
# s(str)
#


def squarefree(s):
    index1 = 0
    index2 = 0

    lastIndex = len(s)

    while(index1 < lastIndex):
        char1 = s[index1]
        # trouve le prochain charactere identique et onl'appelle index2

        index2 = index1 + 1
        foundSubstring = False
        while (index2 < lastIndex and not(foundSubstring)):
            # apres avoir trouve un charactere identique on determine si c'est un 'substring'
            if(char1 == s[index2]):
                substring1 = s[index1:index2]
                endIndex = index2 + (index2-index1)
                substring2 = s[index2:endIndex]
                if(substring1 == substring2):
                    #  substring1 est le 'square'
                    # print(f"{substring1}", end=' ')
                    foundSubstring = True

            index2 += 1

        if(foundSubstring):
            return False
        index1 += 1

    return True
