
import random
# 1
compteur = 10
while(compteur >= 1):
    print(compteur)
    compteur = compteur - 1

# 2


def listeDeChiffres(n):
    i = 1
    while (i <= n):
        print(i)
        i = i+1


def main():
    n = input("Entrez un entier")
    listeDeChiffres(int(n))


main()


def listeDeChiffres1(n):
    for i in range(1, n+1):
        print(i)


def main1():
    n = input("Entrez un entier: ")
    listeDeChiffres1(int(n))


main1()


# 3
def devine():

    n = random.randint(1, 10)
    guess = -1
    tentatives = 0
    while (guess != n):
        guess = int(input(
            "Essayez de devinez quel entier j'ai en tete entre 1 et 10. Entrez votre reponse: "))
        tentatives = tentatives + 1
        if (guess > n):
            print("C'est un numero plus petit que ca.")
        elif (guess < n):
            print("C'est un numero plus grand que ca.")
    return (tentatives)


def main2():
    tentatives = devine()
    print(
        f"Vous avez reussi a trouver le numero apres {tentatives} essais. Bravo!")


main2()


# 4
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


def factorial(n):
    result = 1
    if n == 0:
        return 1
    for i in range(1, n+1):
        result = result * i
    return result


print(factorial(4))
