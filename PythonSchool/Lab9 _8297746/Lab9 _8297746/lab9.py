
# Lab 9
# Juliane Bruck


import random


# Q1

def cherche(l3: list, v: int) -> bool:
    nPas = 0
    for i in range(len(l3)):
        nPas += 1
        if(l3[i] == v):
            print(f"Nombre de pas {nPas}")
            return True
    print(f"Nombre de pas {nPas}")
    return False


def mainQ1():
    N = 100
    l3 = []
    for i in range(0, N):
        v = random.randrange(1, N+1)
        l3.append(v)

    print(f"l3 = {l3}")

    searchVal = random.randrange(1, N+1)
    print(f"cherche(l3, {searchVal})")
    inList = cherche(l3, searchVal)
    print(inList)


# mainQ1()


# Q2

def cherche_m(m: list, v: int) -> bool:

    isFound = False
    numSteps = 0

    i = 0
    while (i < len(m)) and not isFound:
        row = m[i]
        for j in range(len(row)):
            numSteps += 1
            if(m[i][j] == v):
                isFound = True
                break
        i += 1

    print(f"Nombre de pas {numSteps}")

    return isFound


def mainQ2():
    M = [[1, 2, 10], [7, 5, 6], [8, 8, 9, 10]]

    print(f"m = {M}")
    searchVal = 5
    print(f"cherche_m(M, {searchVal})")
    inList = cherche_m(M, searchVal)
    print(inList)


# mainQ2()


# Q3-1

def compter_m(m: list, v: int) -> bool:
    nPas = 0
    occurrences = 0
    for i in range(0, len(m)):
        row = m[i]
        for j in range(0, len(row)):
            nPas += 1
            if m[i][j] == v:
                occurrences += 1
    print(f"Nombre de pas {nPas}")
    return occurrences


def mainQ3():
    M = [[1, 2, 10], [7, 5, 6], [8, 8, 9, 10]]

    print(f"m = {M}")
    searchVal = 5
    print(f"compter_m(M, {searchVal})")
    inList = compter_m(M, searchVal)
    print(inList)


mainQ3()


# Q3-2

def recherche_binaire(l3: list, v: int) -> bool:

    steps = 0
    lowIndex = 0
    endIndex = len(l3)

    #  must be whole number so must use whole number division
    midIndex = (endIndex - lowIndex) // 2

    isFound = False
    while not isFound and lowIndex < endIndex and midIndex > lowIndex and midIndex < endIndex:
        if v == l3[midIndex]:
            isFound = True
        elif v > l3[midIndex]:
            lowIndex = midIndex+1
        else:
            endIndex = midIndex-1

        midIndex = lowIndex + ((endIndex - lowIndex) // 2)
        steps += 1

    print(f"Nombre de pas {steps}")
    return isFound


def mainBinary():
    N = 100
    l3 = [1, 2, 3, 4, 4, 5, 7, 9, 10, 13]
    print(f"l3 = {l3}")
    searchVal = 10
    print(f"cherche({l3}, {searchVal})")
    # inList = cherche(l3, searchVal)

    inList = recherche_binaire(l3, searchVal)
    print(inList)

    inList = recherche_binaire([1, 2, 3, 4, 4, 5, 7, 9, 10, 13], 6)


mainBinary()


# Q3-3

def trierList(L):

    numSteps = 0
    i = 0
    while i != len(L):
        numSteps += 1
        j = i
        while j != 0 and L[j - 1] >= L[i]:
            numSteps += 1
            j = j - 1
        value = L[i]
        del L[i]
        L.insert(j, value)
        i = i + 1
    print(f"num steps {numSteps}")


def mainTrie():
    L = [3, 4, 7, -1, 2, 5]
    trierList(L)
    print(L)


# mainTrie()


def tri_par_insertion(L):

    numSteps = 0
    i = 0
    while i != len(L):
        numSteps += 1

        j = i
        while j != 0 and L[j - 1] >= L[i]:
            numSteps += 1
            j = j - 1

        value = L[i]
        del L[i]
        L.insert(j, value)

        i = i + 1
    print(f" Nombre de pas {numSteps}")


def mainInsertion():
    L = [3, 4, -1, 7, 2, 5, 16, -2, 17, 7, 82, -1]
    tri_par_insertion(L)
    print(L)


# mainInsertion()
