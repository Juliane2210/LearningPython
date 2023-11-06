# Juliane Bruck
# Devoir 5- Question 2
# 8297746


# Q2


import math


def modifierMat(matrice: list) -> None:
    ''' permet de modifier seulement les nombres paires par leurs racine carrée'''

    for subList in matrice:
        for j in range(0, len(subList)):
            item = subList[j]
            if(item % 2 == 0):
                subList[j] = math.sqrt(item)

# programme principal qui apelle la fct modifierMat pour une matrice donnee (matrice)


def main():
    matrice = [[5, 3, 8], [7, 4, 6], [1, 9, 2],
               [8, 7, 1], [3, 2, 9], [4, 6, 5]]
    modifierMat(matrice)
    print(matrice)


main()
