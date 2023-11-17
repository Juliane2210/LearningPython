
# Labo 7
# Juliane Bruck

# Tuples et dictionnaires
#
#  Q1
def histogramme(s: str) -> dict:
    """ fonction qui prend une chaire de caractères et retourne un
        histogramme sous la forme d’un dictionnaire """
    histogram = {}
    for character in s:
        histogram[character] = histogram.get(character, 0) + 1
    return histogram


def mainQ1(s: str) -> None:
    resultHistogramme: dict = histogramme(s)
    sortedKeys = list(resultHistogramme.keys())
    sortedKeys.sort()

    for key in sortedKeys:
        value = resultHistogramme[key]
        print(f" key: {key}  - value: {value}")


# mainQ1("bcdae uliane rucaak")


# Q2
def histo_n(x: tuple) -> dict:
    '''  fonction qui prends un tupleet retourne un dictionnaire qui est une 
    histogramme pour compter combien de fois chaque nombre arrive dans le tuple:  '''
    resultDictionary = {}
    for item in x:
        resultDictionary[item] = resultDictionary.get(item, 0) + 1
    return resultDictionary


def mainQ2(x: tuple) -> None:
    dictionary = histo_n(x)
    sortedItems = list(dictionary.items())
    sortedItems.sort()

    print(sortedItems)


# mainQ2((1, 2, -3, 3, 4, -3, 3, 3))


# Q3
def somme_de_trois(x: tuple) -> bool:
    '''(tuple)->bool
    Retourne Truesi la somme de 3 elements
    consecutiveest zero
    Precondition: le tuplea au moins 3elements
     '''
    for i in range(0, len(x)):
        # sum of next 3 elements
        sum = x[i]
        for j in range(i+1, 3):
            sum += x[j]
        if (sum == 0):
            return True
    return False


def mainQ3(t: tuple) -> None:
    print(somme_de_trois(t))


mainQ3((1, 2, -3, 4, -1, 3))


# Q4
def move_zeros_v1(x: list) -> list:
    tmp = []

    # add in the non zero elements
    for item in x:
        if(item != 0):
            tmp.append(item)

    # add in the zero elements at the end
    for item in x:
        if(item == 0):
            tmp.append(item)

    return tmp


# x = [1, 0, 3, 0, 0, 5, 7]
# y = move_zeros_v1(x)
# print(x, y)


def move_zeros_v2(x: list) -> None:
    for item in x:
        if(item == 0):
            x.remove(item)
            x.append(item)


# x = [1, 0, 3, 0, 0, 5, 7]
# z = move_zeros_v2(x)
# print(x, z)


def move_zeros_v3(x: list) -> None:

    totalIterations = 0
    i = 0
    while i < len(x) and totalIterations < len(x):
        if(x[i] == 0):
            # keep swapping and jump the zero down to end of list
            for j in range(i, len(x)-1):
                x[j], x[j+1] = x[j+1], x[j]

        # only increment the index if we didn't swap a zero previously.
        # if we did swap a zero, that needs to be jumped to the end
        if (x[i] != 0):
            i += 1
        totalIterations += 1


# x = [0, 0]
# x = [1, 0, 3, 0, 0, 5, 7]
# t = move_zeros_v3(x)
# print(x, t)
