# Juliane Bruck
# Labo 8
# 8297746
# j'ai fait les exercices dans un fichier a part...donc je ne demande pas a lutilisateur
# d'entrer les matrices...j'espere que c'est correct (les fonctions fonctionnent quand meme j'ai verifie)

# Q1
# on creer une matrice vide de bonnes dimmensions, avant de la remplir
# avec les bons elements
def transpose(m: list) -> list:
    collen = len(m[0])
    ranglen = len(m)
    transpose = [[0]*ranglen for i in range(collen)]
    for i in range(0, len(m)):
        rang = m[i]
        for j in range(0, len(rang)):
            transpose[j][i] = m[i][j]
    return (transpose)


# Q2
# j'ai fait la meme chose qu'au 1 en rajoutant la somme des elements a ma nouvelle matrice(m)
def somme_matrices(A: list, B: list) -> list:
    collen = len(A[0])
    ranglen = len(A)
    m = [[0]*ranglen for i in range(collen)]
    for i in range(0, len(A)):
        row = A[i]
        for j in range(0, len(row)):
            m[i][j] = A[i][j]+B[i][j]
    return m


# Q3
# on construit la matrice vide de bonne dimmension
# ensuite j'ai utilise la definition exacte (mathematique)pour creer mes boucles
def produit_matrices(A: list, B: list) -> list:
    m = len(A)
    n = len(A[0])
    p = len(B[0])

    C = [[0]*m for i in range(p)]

    for i in range(0, m):
        for j in range(0, p):
            totalSum = 0
            for k in range(0, n):
                totalSum += A[i][k]*B[k][j]
            C[i][j] = totalSum
    return (C)
