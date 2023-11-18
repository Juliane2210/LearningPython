# Juliane Bruck
# Devoir 5 -Question 1


inventory = {"bureau": 9, "chaise": 25, "imprimante": 46, "scanneur": 17}
prices = {"bureau": 75.9, "chaise": 50.9, "imprimante": 32.5, "scanneur": 28.0}


# Q1-a
# Cette fonction prends le nom de l'article et la quantite et rtourne le cout total (finalCost) a l'aide du dictionnaire (prices)
def calculPrix(article: str, quantite: int) -> float:
    ''' str, int -> float '''
    finalCost = prices[article] * quantite
    return finalCost


# print(calculPrix("bureau", 1))


# Q1-b
# utilise la fct du 1-a pour calculer le prixTotal de 3 articles (avec les 3 quantites correspondantes)
def calculTotal(article1: str, quantite1: int, article2: str, quantite2: int, article3: str, quantite3: int) -> float:
    ''' calc the total '''
    return calculPrix(article1, quantite1) + calculPrix(article2, quantite2) + calculPrix(article3, quantite3)


# print(calculTotal("chaise", 2, "bureau", 1, "scanneur", 1))


# Q1-c
# fct prend 3 articles (avec les 3 quantites respectives) et retourne True si l'article apparait dans le dictionaire 'inventory'
# et verifie si la quantité correspondante (selon la cle) est >= que celle entree
# retourne False sinon
# si la comande est valide (valeur retourne est True), alors la cle de 'inventory' est actualise

def validerCommande(article1: str, quantite1: int, article2: str, quantite2: int, article3: str, quantite3: int) -> bool:
    ''' validate .. '''
    isOrderValid = inventory.get(article1, 0) >= quantite1 and inventory.get(
        article2, 0) >= quantite2 and inventory.get(article3, 0) >= quantite3

    if(isOrderValid):
        inventory[article1] -= quantite1
        inventory[article2] -= quantite2
        inventory[article3] -= quantite3

    return isOrderValid


# print(validerCommande("bureau", 15, "imprimante", 2, "scanneur", 3))
# print(validerCommande("bureau", 1, "imprimante", 2, "scanneur", 3))
# print(validerCommande("bureau", 1, "souris", 2, "scanneur", 3))


# Q1-d
# programme principal demande au client d'entrer 3 articles avec quantites associes
# utilise les fcts du 1-a, 1-b et 1-c pour caluler le prix, valider la commande et modifier la liste 'inventory'
#

def main():

    firstArticle = input("Entrez le premier article: ")
    firstQuantity = int(input("Entrez la quantité de votre 1ere article: "))
    secondArticle = input("Entrez le deuxième article: ")
    secondQuantity = int(input("Entrez la quantité de votre 2eme article: "))
    thirdArticle = input("Entrez le troisième article: ")
    thirdQuantity = int(input("Entrez la quantité de votre 3eme article: "))

    validOrder = validerCommande(
        firstArticle, firstQuantity, secondArticle, secondQuantity, thirdArticle, thirdQuantity)

    if(not validOrder):
        print("\nVotre commande est annulée. SVP, vérifier les articles ou les quantités.")
    else:
        price = calculTotal(firstArticle, firstQuantity, secondArticle,
                            secondQuantity, thirdArticle, thirdQuantity)

        print(
            f"\nLe prix total de votre commande est: {price}$. Merci et à la prochaine")

    print(f"\nLes quantités disponibles après l'achat sont: {inventory} ")


main()
