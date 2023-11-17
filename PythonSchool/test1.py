# Test 1
# Juliane Bruck


# 1
# Contrat de la fonction:
# (string)->(string)
# Variables:
# sn (string)

def atlantic(sn):
    if(len(str(sn)) >= 9):
        return ("nouveau")
    else:
        return("vieux")


# 2
# Contrat de la fonction:
# (int)->(string)
# Variable: n (int)
# Variables intermediaires:
# livres (float)
# onces (float)
# resultatPoids (float)
# nom (string)
# numeroEtudiant (int)
# resultat (string)
# Fonction intermediaire:
# atlantic(sn) {voir numero 1}
def southern(n):
    if(n == 1):
        livres = float(input("Entrez le poids en livres: "))
        onces = float(input("Entrez le poids en onces: "))
        resultatPoids = (livres*16 + onces) * 0.02835
        print(
            f"{livres} livres et {onces} onces est (approx.) {resultatPoids} kilogrammes.")

    elif (n == 2):
        nom = str(input("Quel est ton nom?"))
        numeroEtudiant = input("Quel est ton numero d'etudiant?")
        resultat = atlantic(numeroEtudiant)
        print(f"{nom} ton numero d'etudiant est {resultat}")

    else:
        print("Invalide")


# 3
# Contrat de la fonction:
# (float,float,float)->bool
# Variables: g1 (float), g2 (float), g3 (float)
# Variables intermediaires:
# passG1 (int)
# passG2 (int)
# passG3 (int)
# isG1A (int)
# isG2A (int)
# isG3A (int)
def pacific(g1, g2, g3):

    passG1 = g1 // 50
    passG2 = g2 // 50
    passG3 = g3 // 50

    isG1A = g1 // 80
    isG2A = g2 // 80
    isG3A = g3 // 80

    return bool(((passG1 and passG2 and passG3) and isG1A) or
                ((passG1 and passG2 and passG3) and isG2A) or
                ((passG1 and passG2 and passG3) and isG3A))
# 4
# Contrat de la fonction:
# (int)-> bool
# Variables: n (int)
# Variables intermediaires:
# firstDigit (int)
# secondDigit (int)
# thirdDigit (int)
# fourthDigit (int)
# fifthDigit (int)
# sixthDigit (int)


def arctic(n):

    firstDigit = n % 10
    secondDigit = (n // 10) % 10
    thirdDigit = (n // 100) % 10
    fourthDigit = (n // 1000) % 10

    if (n <= 9999):
        return (bool(firstDigit == fourthDigit and secondDigit == thirdDigit))
    else:
        fifthDigit = (n // 10000) % 10
        sixthDigit = (n // 100000) % 10
        return (bool(firstDigit == sixthDigit and secondDigit == fifthDigit and thirdDigit == fourthDigit))
