# Devoir 4 - Question 2
# Juliane Bruck


# Cette fct retourne True si il n'y a pas deux nombres consecutifs dans la liste ('numberList'->liste de float)
# Elle compare les entrees consecutives soient ' item1'  (float) et ' item2' (float) a l'aide d' une boucle for
#

def sequenceDesDeux(numberList):
    for i in range(0, len(numberList)-1):
        item1 = numberList[i]
        item2 = numberList[i+1]
        if(item1 == item2):
            return True
    return False


# Cette fonction transforme des chiffres donnees par l'usager 'userList' (str) et les transforme en une liste de float
#  'numberList' (liste de float) qui sera utilise par la fct 'sequenceDesDeux'
#
#
def main():

    userList = input(
        "Veuillez entrer une liste des entiers par des espaces: ").strip().split()
    numberList = []
    for item in userList:
        numberList.append(float(item))

    result = sequenceDesDeux(numberList)
    print(result)


main()
