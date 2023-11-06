# Juliane Bruck
# 8297746
# Devoir 6

# Q2 - A
'''fonction recursive qui prends un (int) et fera un dessin d'etoiles (none)'''


def triangle(starCount: int) -> None:
    if(starCount <= 1):
        print("*")
    else:
        triangle(starCount - 1)
        print('*' * starCount)


# triangle(9)

# Q2 - B
'''fonction recursive qui prends une (liste) et un (int) et retournera le produit d' elements positifs (int)'''


def prodListePos_rec(l: list, numElements: int) -> int:

    if numElements <= 0:
        return 0

    elif numElements == 1:
        if l[0] > 0:
            return l[0]
        else:
            return 1

    if l[0] > 0:
        return l[0] * prodListePos_rec(l[1:], numElements-1)

    return prodListePos_rec(l[1:], numElements - 1)


# l = [1, -2, 5, 0, 6, -5]
# print(prodListePos_rec(l, len(l)))


# Q2 - C
'''fonction recursive qui prends un (str) et retourne un (bool). Cette fonction verifie si le str est un palindrome (True) ou non (False)
'''


def palindrome(word: str) -> bool:

    if(len(word) <= 1):
        return True

    return word[0] == word[-1] and palindrome(word[1: len(word)-1])


# print(palindrome("abcba"))
# print(palindrome("anna"))
# print(palindrome([]))
# print(palindrome("abcdabcd"))
