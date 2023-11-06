# Devoir 4 - Question 3
# Juliane Bruck
# 8297746

# Cette fct retourne la longueur de la plus grande sequence d'elements consecutifs egaux de la liste 'numberList' (liste de int)
# Elle compare les entrees consecutives avec deux boucles for  (premier index est i et deuxieme index est j=i+1)
#  Si les indexs consecutifs ont la meme valeur alors la premiere boucle compte la longueur ('consecutiveCount' ->int)
# Ensuite la boucle principale compare tous les compteurs: ' consecutiveCount'(int) avec ' longestConsecutiveCount' (int)
# pour retourner la longueur la plus grande
#
#
def sequenceMax(numberList):
    longestConsecutiveCount = 1
    for i in range(0, len(numberList)):
        consecutiveCount = 1
        for j in range(i+1, len(numberList)):
            if (numberList[i] == numberList[j]):
                consecutiveCount += 1
            else:
                break
        if (longestConsecutiveCount < consecutiveCount):
            longestConsecutiveCount = consecutiveCount
    return longestConsecutiveCount

# Cette fonction transforme des chiffres donnees par l'usager 'userList' (str) et les transforme en une liste de float
#  'numberList' (liste de float) qui sera utilise par la fct 'sequenceMax'
#
#


def main():

    userList = input(
        "Veuillez entrer une liste des entiers par des espaces: ").strip().split()
    numberList = []
    for item in userList:
        numberList.append(float(item))

    result = sequenceMax(numberList)
    print(result)


main()
