# Juliane Bruck
# 8297746
# Devoir 2


# 1- compte le nombre de 'oui' et de 'non' dans un chaîne caractères
# Contrat de la fonction:
# (string)-> (float)
# Variable: charSequence (string)
# Variable intermediaires:
# numYes (int)
# numNo(int)
# numAbstain (int)
# percentageOui (float)
def vote_pourcentage(charSequence):
    numYes = charSequence.count("oui")
    numNo = charSequence.count("non")
    numAbstain = charSequence.count("abstention")
    percentageOui = numYes / (numYes + numNo)
    return percentageOui

# fonction principale du programme qui interragit avec l'usager et qui appelle vote_pourcentage
# (string) -> (None)


def main():
    charSequence = input(
        "Entrez les votes (oui, non, ou abstention) séparés par des espaces, et à la fin appuyez enter: ")
    percentageOui = vote_pourcentage(charSequence)
    if(percentageOui == 1):
        print("unanimité")
    elif (percentageOui >= (2/3)):
        print("majorité claire")
    elif(percentageOui >= (1/2)):
        print("majorité simple")
    else:
        print("la motion ne passe pas")


main()
