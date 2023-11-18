# Juliane Bruck

# Devoir 2

import random

# 2-La fonction prend comme paramètre un entier qui indique l’opération: 0 pour soustraction et 1 pour exponentiation.
# Le résultat donné par la fonction est le nombre de bonnes réponses.
# Elle appelle les fonctions subtractionTest et powerTest

# Contrat de la fonction:
# (int) -> (int)
# Variables: operation (int)
# Parametres : numQuestions : il y a 10 questions dans le test


def effectuezTest(operation: int) -> int:
    numQuestions = 10

    if(operation == 0):
        return subtractionTest(numQuestions)
    elif (operation == 1):
        return powerTest(numQuestions)

    return -1

# Cette fonction est une boucle qui retourne le nombre de bonnes reponses suite au test de soustractions
# Contrat de la fonction:
# (int)->(int)
# Variables: totalCorrect (int) , numQuestions (int)
# Variables intermediaires:
# n1 (int)
# n2(int)
# bonneReponse (int)
# studentResponse(int)


def subtractionTest(numQuestions: int) -> int:
    totalCorrect = 0
    for i in range(0, numQuestions):
        n1 = random.randint(0, 9)
        n2 = random.randint(0, 9)
        bonneReponse = n1 - n2
        studentResponse = int(input(f"{n1} - {n2} = "))
        if(bonneReponse == studentResponse):
            totalCorrect = totalCorrect + 1
        else:
            print(f"Incorrect – la reponse est {bonneReponse}")

    return totalCorrect


# Cette fonction est une boucle qui retourne le nombre de bonnes reponses suite au test exponentiel
# Contrat de la fonction:
# (int)->(int)
# Variables: totalCorrect (int) , numQuestions (int)
# Variables intermediaires:
# n1 (int)
# n2(int)
# bonneReponse (int)
# studentResponse(int)


def powerTest(numQuestions: int) -> int:
    totalCorrect = 0
    for i in range(0, numQuestions):
        n1 = random.randint(0, 9)
        n2 = random.randint(0, 9)
        bonneReponse = n1 ** n2
        studentResponse = int(input(f"{n1} ** {n2} = "))
        if(bonneReponse == studentResponse):
            totalCorrect = totalCorrect + 1
        else:
            print(f"Incorrect – la reponse est {bonneReponse}")

    return totalCorrect


# Cette fonction est la partie principale du programme qui interragit avec l'usager et qui appelle effectuezTest
# Contrat de la fonction:
# (int)-> (none)
# Variables: operation (int),
# Variables intermediaires:
# numCorrect (int)


def main():
    operation = int(input(
        "Ce logiciel va effectuez un test avec 10 questions.  SVP choisisser l'operation 0) soustraction 1) exponentiation (0 ou 1): "))

    if(operation == 0 or operation == 1):
        numCorrect = effectuezTest(operation)
        print(f"{numCorrect} reponses correctes.")
        if(numCorrect >= 6):
            print("Félicitations!")
        else:
            print("Demandez à votre enseignant(e) de vous aider.")
    else:
        print("Operation incorrecte.")


main()
