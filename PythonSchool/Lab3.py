# Juliane Bruck
# 8297746
# Blessed
# Labo 3


# Exercice 1
def verificationAge():
    age = int(input("Quel age avez-vous?"))
    if(age >= 18 and age <= 55):
        print("Transaction acceptee")
        return True
    else:
        print("Transaction refusee")
    return False


verificationAge()

# Exercice 2


def quoiTemp():
    temp = float(input("Quelle est la temperature en Fahrenheit?"))

    if (temp >= 80.0):
        print("Natation")
        return (1)
    elif (temp >= 60.0 and temp < 80.0):
        print("Soccer")
        return (2)
    elif (temp >= 40.0 and temp < 60.0):
        print("Volleyball")
        return(3)
    else:
        print("Ski")
    return(4)


quoiTemp()


# Exercice 3
def estDivisible():
    entier = int(input("SVP entrez un entier:"))
    if (entier % 2 == 0 and entier % 3 == 0):
        print(1)
        return (1)
    elif (entier % 2 == 0 or entier % 3 == 0):
        print(2)
        return(2)
    else:
        print(0)
    return(0)


estDivisible()


# Exercie 4
def nombRacinesReelles
