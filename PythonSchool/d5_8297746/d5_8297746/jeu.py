
# Juliane Bruck
# Devoir5- jeu



def verifierLigne(grille, row, num):
    '''
        (list, int, int) -> Bool
        Vérifier si la case à ajouter n'existe pas sur la ligne.
        Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    # A COMPLETER
    rowList = grille[row]
    for rowItem in rowList:
        if(rowItem == num):
            return False
    return True


# print(verifierLigne(grille, 0, 3))


def verifierCol(grille, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la colonne.
            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    # A COMPLETER
    columnList = []
    for rowList in grille:
        columnList.append(rowList[col])

    for colItem in columnList:
        if(colItem == num):
            return False
    return True


# print(verifierCol(grille, 0, 6))


def verifierSousGrille(grille, row, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la sous-grille.


            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''

    # A COMPLETER

    # could use this also
    # subGridRow = row // 3
    # subGridCol = col // 3

    subGridList = []

    subRow1 = grille[row * 3]
    subRow2 = grille[(row*3) + 1]
    subRow3 = grille[(row*3) + 2]

    subCol1 = subRow1[col*3: (col*3) + 3]
    subCol2 = subRow2[col*3: (col*3) + 3]
    subCol3 = subRow3[col*3: (col*3) + 3]

    subGridList = subCol1 + subCol2 + subCol3

    if(num in subGridList):
        return False
    return True


# print(verifierSousGrille(grille, 0, 1, 2))


def verifierGagner(grille) -> bool:
    '''(list) ->  bool
    * Preconditions: grille est une reference a une matrice 9x9 qui contient de nombres de 1 à 9
    * Verifie si la grille est completement remplie.
    '''

    # A COMPLETER

    for rowList in grille:
        for item in rowList:
            if item > 9 or item < 1:
                return False
    return True


def verifierValide(grille, row, col, num):
    ''' (list, int, int, int) ->  bool
    * verifie si le nombre proposé est bon sur la ligne et colonne et la sous-grille donné en parametre.
    * Preconditions: tab est une reference a une matrice 9 x 9 qui contient des chiffres entre 1 et 9
    '''

    # A COMPLETER

    rowValid = verifierLigne(grille, row, num)
    columnValid = verifierCol(grille, col, num)

    subGridRow = row // 3
    subGridCol = col // 3
    subGridValid = verifierSousGrille(grille, subGridRow, subGridCol, num)

    return rowValid and columnValid and subGridValid


# grille = [[5, 3, 8, 6, 9, 1, 0, 4, 7],
#           [7, 4, 6, 5, 3, 2, 8, 1, 9],
#           [1, 9, 2, 7, 8, 4, 3, 5, 6],
#           [8, 7, 1, 2, 6, 3, 4, 9, 5],
#           [3, 2, 9, 4, 5, 7, 1, 6, 8],
#           [4, 6, 5, 9, 1, 8, 7, 2, 3],
#           [6, 1, 4, 3, 7, 9, 5, 8, 2],
#           [9, 8, 3, 1, 2, 5, 6, 7, 4],
#           [2, 5, 0, 8, 4, 6, 9, 3, 1]]

# print(verifierValide(grille, 0, 6, 2))
