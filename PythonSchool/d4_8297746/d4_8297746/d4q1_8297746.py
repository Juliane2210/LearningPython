
# Devoir 4- Question 1
# Juliane Bruck


# Cette fct retourne le nombre total d'elements qui sont divisibles par n donne ('divisor' -> int)
# dans la liste de nombres donnee ('numberList'->liste de int)
#
def nombreDivisibles(numberList, divisor):
    count = 0
    for item in numberList:
        if(item % divisor == 0):
            count += 1
    return count


# Cette fonction transforme des chiffres donnees par l'usager 'userList' (str) et les transforme en une liste de int
#  qui sera utilise par la fct 'nombreDivisibles' (int)
#
#
def main():
    userList = input(
        "Veuillez entrer une liste des entiers par des espaces: ").strip().split()
    numberList = []
    for item in userList:
        numberList.append(int(item))

    divisor = int(input("Veuillez entrer un entier positif: "))

    count = nombreDivisibles(numberList, divisor)
    print(f"Le nombredes éléments divisibles par {divisor} est {count}")


main()
