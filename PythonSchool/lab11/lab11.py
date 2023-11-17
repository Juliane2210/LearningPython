
# Juliane Bruck

# Lab11
#
# Excercice #1
#
#

def verifyChiffre(a: list, n: int) -> bool:
    if n > 0:
        return (a[n-1] in range(0, 9 + 1)) and verifyChiffre(a[0:n-1], n-1)
    return True


# def main1():
#     a = [3, 4, 5, 6, 9]
#     print(verifyChiffre(a, len(a)))
# main1()

#
#
# Excercice #2
#
#
def creerList(l: list, n: int) -> list:

    if(n >= 0):
        creerList(l, n-1)
        l.append(n)
    return l


# def main2():
#     l = []
#     n = int(input(" enter a value: "))
#     print(creerList(l, n-1))


# main2()

#
# Excercice #3
#


def pgcd(x: int, y: int) -> int:
    if x >= y and x % y == 0:
        return y

    if x < y:
        return pgcd(y, x)

    return pgcd(y, x % y)


# def main3():
#     print(pgcd(1234, 4321))
#     print(pgcd(8192, 192))


# main3()
