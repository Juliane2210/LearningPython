# COPYRIGHT 2020, Vida Dujmovic and Diana Inkpen. All rights reserved.
# Any unauthorised distribution will constitute an infringement of copyright.


# Devoir 4 - Question 4
# Juliane Bruck



def is_valid_file_name():
    '''()->str or None'''
    file_name = None
    try:
        file_name = input("Entrez le nom du fichier: ").strip()
        f = open(file_name)
        f.close()
    except FileNotFoundError:
        print("Il n'y a pas aucun fichier avec ce nom. Essayez encore une fois.")
        file_name = None
    return file_name


def get_file_name():
    file_name = None
    while file_name == None:
        file_name = is_valid_file_name()
    return file_name


def clean_word(word):
    '''(str)->str
    Retourne une nouvelle chaine de caracteres a partir de la chaine word,
    en minuscule, sans les caracteres specieux et sans les chiffres

    La chaine retournee ne doit pas contenir:
    ! . ? : , ' " - _ \ ( ) [ ] { } % 0 1 2 3 4 5 6 7 8 9 \t \n

    >>> clean_word("co-operation.")
    'cooperation'
    >>> clean_word("1982")
    ''
    >>> clean_word("born_y1982_m08\n")
    'bornym'
    >>> clean_word("SEO : 5 outils gratuits pour trouver des mots-cles pertinents")
    'seo   outils gratuits pour trouver des motscles pertinents'
    '''

    # VOTRE CODE ICI
    specialCharTuple = ("!", ".", "?", ":", ",", "'", "\"", "-", "_", "\\",
                        "(", ")", "[",  "]", "#", "{", "}", "%", "\t", "\n", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

    cleanWord = ""
    for char in word:
        if not(char in specialCharTuple):
            cleanWord += char

    cleanWord = cleanWord.lower()

    return cleanWord


# print(clean_word("1982"))


def test_letters(w1, w2):
    '''(str,str, list of str)->bool
    La fonction retourne True si les mots w1 et w2 ont exactement les memes
    lettres, et False sinon

    >>> test_letters("mais", "amis")
    True
    >>> test_letters("lapin", "pinla")
    True
    >>> test_letters("lapin", "alpin")
    True
    >>> test_letters("alin", "alpin")
    False
    '''

    # VOTRE CODE ICI
    sortedW1 = sorted(w1)
    sortedW2 = sorted(w2)

    return sortedW1 == sortedW2


# print(test_letters("mais", "amis"))


def create_clean_sorted_nodupicates_list(s):
    '''(str)->list of str
    Pour la chaine s qui represente le texte, la fonction retourne une liste avec ces exigences:
    - les mot ne contient pas des caracteres specieux our des chiffres)
    - il n'y a pas de mots qui se repetent dans la liste
    - la liste est triee en ordre alphabetique (vous pouvez utilser s.sort() ou sorted())

    La fonction doit applelez la fonction test_letters.

    Vous pouvez utiliser s.split() pour obtenir une liste coupee par des espaces.

    >>> create_clean_sorted_nodupicates_list("Consultez notre site de web pour tout savoir de l'actualite internationale, nationale et regionale.")
    ['consultez', 'de', 'et', 'internationale', 'lactualite', 'nationale',
        'notre', 'pour', 'regionale', 'savoir', 'site', 'tout', 'web']

    '''

    # VOTRE CODE ICI

    cleanWordList = []
    listOfWords = s.split(" ")

    for word in listOfWords:
        cleanWordList.append(clean_word(word))

    nonDuplicateCleanList = []
    for index in range(0, len(cleanWordList)):
        firstWord = cleanWordList[index]
        foundDuplicate = False
        for index2 in range(index+1, len(cleanWordList)):
            secondWord = cleanWordList[index2]
            if(test_letters(firstWord, secondWord)):
                # a dupe is found, don't add the first word.
                foundDuplicate = True
                break
        if (not(foundDuplicate)):
            nonDuplicateCleanList.append(firstWord)

    nonDuplicateCleanSortedList = sorted(nonDuplicateCleanList)
    return nonDuplicateCleanSortedList


# print(create_clean_sorted_nodupicates_list(
#     "Consultez notre site de web pour tout savoir de l'actualite internationale, nationale et regionale."))


def word_anagrams(word, wordbook):
    '''(str, list of str) -> list of str
    - word est une chaine de caractere qui represente un mot
    - wordbook est une liste des mots (sans des mots repetes)

    La fonction retourne une liste des anagrammes de mot word dans la liste wordbook

    >>> word_anagrams("liste", wordbook)
    ['lites']
    >>> word_anagrams("lapin", wordbook)
    ['alpin', 'plain']
    >>> word_anagrams("elephant", wordbook)
    []
    '''

    # VOTRE CODE ICI
    anagramList = []

    sortedWord = sorted(word)
    for searchWord in wordbook:
        if(test_letters(searchWord, sortedWord) and not(searchWord == word)):
            anagramList.append(searchWord)
    return anagramList

# french_noaccents.txt is the wordbook
# print(word_anagrams("lapin", ["alpin", "xxx", "plain"]))


def count_anagrams(l, wordbook):
    '''(list of str, list of str) -> list of int

    - l est une liste des mots (sans des mots repetes)
    - wordbook est une liste des mots (sans des mots repetes)

    La fonction retourne une liste des entiers ou l'entier de index i represente
    le nombre des anagrammes dans la liste wordbook pour le mot de index i dans liste l.

    Quand un mot dans la liste l est le meme que le mot dans la liste wordbook, on ne le compte pas.

    >>> count_anagrams(["liste","amis", "lapin", "anee", "race", "oreilles"], wordbook)
    [1, 4, 2, 0, 5, 2]
    '''

    # VOTRE CODE ICI
    anagramCountList = []
    for searchWord in l:
        wordAnagramsList = word_anagrams(searchWord, wordbook)

        numberAnagrams = len(wordAnagramsList)
        # dont include the search number itself in the count
        if(searchWord in wordAnagramsList):
            numberAnagrams -= 1
        anagramCountList.append(numberAnagrams)
    return anagramCountList


# french_noaccents.txt is the wordbook
# print(count_anagrams(["liste", "amis", "lapin", "anee", "race", "oreilles"], [
#       "alpin", "mais", "amis", "xxx", "plain"]))


def k_anagram(l, anagcount, k):
    '''(list of str, list of int, int) -> list of str

    - l est une liste des mots (sans de repetitions)
    - anagcount est une liste des entiers ou l'entier de index i dans la liste represente
    le nombre des anagrammes dans la liste wordbook pour le mot des index i dans la liste l.

    La fonction retournes tous les mots de la liste l qui ont exactement k anagrammes
    (dans la liste wordbook donnee dans le parametre anagcount)

    >>> k_anagram(["liste","amis", "lapin", "anee", "race", "oreilles"],[1, 4, 2, 0, 5, 2],2)
    ['lapin', 'oreilles']

    '''

    # VOTRE CODE ICI
    matchingAnagramCountList = []
    # sanity check since len of l must be same as len of anagcount
    if not(len(l) == len(anagcount)):
        return matchingAnagramCountList

    for i in range(0, len(anagcount)):
        if(anagcount[i] == k):
            matchingAnagramCountList.append(l[i])
    return matchingAnagramCountList


# print(k_anagram(["liste", "amis", "lapin", "anee",
#                  "race", "oreilles"], [1, 4, 2, 0, 5, 2], 2))


def max_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l est une liste des mots (pas des repetitions)
    - anagcount est une liste des entiers ou l'entier de index i dans la liste represente
    le nombre des anagrammes dans liste wordbook pour le mot de index i dans la liste l.

    La fonction retournes tous les mots de l avec le nombre maximal des anagrammes
    (dans la liste wordbook donnee dans le parametre anagcount)

    >>> max_anagram(["liste","amis", "lapin", "anee", "race", "oreilles"],[1, 4, 2, 0, 5, 2])
    ['race']
    '''

    # VOTRE CODE ICI

    # get the last digit after sorting to find the max number.
    maxNumber = sorted(anagcount)[len(anagcount)-1]
    return k_anagram(l, anagcount, maxNumber)


# print(max_anagram(["liste", "amis", "lapin", "anee",
#                    "race", "oreilles"], [1, 4, 2, 0, 5, 2]))


def zero_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l est une liste des mots (pas des repetitions)
    - anagcount est une liste des entiers ou l'entier de index i integer dans la liste
    represente le nombre des anagrammes dans wordbook pour le mot de index i en l.

    La fonction retournes tous les mots de l sans des anagrammes
    (dans la liste wordbook donnee dans le parametre anagcount)

    >>> zero_anagram(["liste","amis", "lapin", "anee", "race", "oreilles"],[1, 4, 2, 0, 5, 2])
    ['anee']
    '''

    # VOTRE CODE ICI
    return k_anagram(l, anagcount, 0)


##############################
# main
##############################


wordbook = open(
    "french_noaccents.txt").read().lower().split()
list(set(wordbook)).sort()

print("Est-ce que vous voulez:")
print("1. Analyser les anagrammes d'un texte donne dans un fichier?")
print("2. Aide pour le jeu de Scrabble?")
print("Entrez un caractere different de 1 ou 2 pour arreter: ")
choice = input()

if choice == '1':
    file_name = get_file_name()
    rawtx = open(file_name).read()
    l = create_clean_sorted_nodupicates_list(rawtx)
    anagcount = count_anagrams(l, wordbook)

    print("\nParmis les mots dans le fichier, les mots suivantes ont le plus grand nombre des anagrammes:")

    # VOTRE CODE ICI
    # use small_fr.txt as input.
    maxAnagramList = max_anagram(l, anagcount)
    print(maxAnagramList)

    print(f"\nVoici leurs anagrammes:")
    for anagramWord in maxAnagramList:
        anagramList = word_anagrams(anagramWord, wordbook)
        print(f"Les anagrammmes de {anagramWord} sont: {anagramList}")

    print("\nVoici les mots dans le fichiers qui n'ont pas des anagrammes:")
    zeroAnagramList = zero_anagram(l, anagcount)
    print(zeroAnagramList)

    print("\nSi vous etes interese s'il y a un mot dans le fichier qui a exactement k anagrammes")
    k = int(input("Entrez un entier k: "))

    print(
        f"Voici le mot (mots) dans le fichier avec exactement {k} anagrammes:")
    kAnagramList = k_anagram(l, anagcount, k)
    print(kAnagramList)

elif choice == '2':
    # VOTRE CODE ICI
    # prompt for any word.   Search for that word to get list of anagram in wordbook
    # Comme option2, l’usagerpeut demander d’aide pour le jeu de scrabble, avec toutesles lettres données ou avec ceslettres sauf uned’entreeux.
    inputWord = input("Entrez les letteres que vous avez, sans des espaces: ")

    print("Est-ce que vous voulez d'aide a former un mot avec ")
    print("1. toutes ces lettres")
    print("2. toutes sauf une des ces lettres?")
    scrabbleChoice = input()

    if scrabbleChoice == '1':
        anagramList = word_anagrams(inputWord, wordbook)
        print(f"Voici les mots avec exactement ces lettres:")

        # add in the word to the list if it exists in the wordbook since word_anagrams returns just the anagrams
        if(inputWord in wordbook):
            anagramList.append(inputWord)

        print(anagramList)

    elif scrabbleChoice == '2':
        print("Si on elimine une des ces lettres.")

        for i in range(0, len(inputWord)):
            inputWordList = list(inputWord)
            del(inputWordList[i])
            searchWord = ''.join(inputWordList)

            print(
                f"Sans la lettre en position {i+1} on a les lettres {searchWord}")

            anagramList = word_anagrams(searchWord, wordbook)

            # could use zero_anagram() here:
            if len(anagramList) > 0:
                print(
                    f"Voici les mots avec exactement ces lettres: {searchWord}")
                print(anagramList)

            else:
                print(f"Il n'y a aucun mot avec ces lettres. {searchWord}")


else:
    print("Au revoir!")
