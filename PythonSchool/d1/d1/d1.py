# Juliane Bruck
#8297746
#Devoir 1

#Exécuter avec "python -i d1.py"




# 1. Cette fonction sert à calculer l'aire d'un triangle: (base*hauteur*1\2)
# paramètres:
#   base: float - la base du triangle
#   hauteur: float - la hauteur du triangle
# retourne
#   aire: float - l'aire du triangle 
 

def aireDuTriangle (base : float,hauteur : float) -> float:
    aireDuTriangle = (base * hauteur)/2
    return(aireDuTriangle)

# 2. Une fonction qui demande la base et la hauteur du triangle
# et qui affiche l'aire 
# memes variables que la Q1

def aireDuTrianglePrint() -> None :
    base = float(input("SVP entrez la valeur de la base: "))
    hauteur = float(input("SVP entrez la valeur de la hauteur: "))
    aire = aireDuTriangle(base, hauteur)
    print("Un triangle de base ", base, " et hauteur", hauteur, " a l'aire ", aire )

# 3. Une fonction qui convertit les kilogrammes d'un poids donné
#  en livres et en onces
# Variables: 
# livres - float
# onces - float
# retourne: le poids (en kilo) - float

def loEnKilos(livres: float, onces: float) -> float : 
    LIVRES_PAR_KILO = 2.2046226218
    OUNCES_PAR_KILO = 35.27396195   
    return (livres / LIVRES_PAR_KILO) + (onces / OUNCES_PAR_KILO)

# 4. Avec l'information de 5 variables 
# cette fonction retourne une chaine de characteres sous format bibliographique
# Variables:
# auteur - string
# titre - string
# ville -string
# maisonEdition -string
# annee -string
# Retourne: le format bibliographique - string
def bibformat(auteur, titre, ville, maisonEdition, annee) :
    return f"{auteur} ({annee}). {titre}. {ville.capitalize()}: {maisonEdition}" 

# 5. Cette fonction affiche l'information bibliographique du livre 
# sous le format donne par la fonction precedenteself. Memes variables que Q4.

def bibformatPrint() :
        auteur = input("SVP entez l'auteur: ")
        titre = input("SVP entez le titre: ")
        ville = input("SVP entez la ville: ")
        maisonEdition = input("SVP entez la maison d'edition: ")
        annee = input("SVP entez l'annee de publication: ")
        print(bibformat(auteur, titre, ville, maisonEdition, annee))
# 6. Cette fonction calcule la racine carrée de l'entier donné - 10 et affiche la solution
# l'entier donné doit être supérieur ou égal à 10 sinon la racine est négative
# le type de fonction est  (int) -> (float)
# Variables:
# p - int
# r - float

import math as m
def funct(p) : 
    if( p >= 10) : 
        r = m.sqrt(p-10)
        print("La solution est", r)
        return (r)
    else : 
        print ("invalid input")
    return (-1)

# 7. Cette fonction prend comme entrée un entier positif  de trois chiffres
# La fonction retourne True si l'entier est un nombre magique, et False sinon
# Un nombre est magique si deux chiffres consécutifs sont égaux à 3, ou si le dernier chiffre se divise par 4
#  Le contrat de type de la fonction est: (int) -> boolean
# Variables:
# nombreMagique - int
# retourne: True ou False - bool

def magique(nombreMagique) :
    NOMBRE_MAGIQUE = 3
    #verification de l'entree.  Ne peut avoir plus de trois chiffres
    if (nombreMagique > 999 or nombreMagique < -999) :
        return False
  
    centaines = nombreMagique // 100
    dizaines = ( nombreMagique % 100) // 10
    unites = ( nombreMagique % 10)

    unitesDivisiblesParQuatre = ((unites % 4 )  == 0 ) 

    # test si deux chiffres consecutifs sont egal a 3
    if (     ((centaines == NOMBRE_MAGIQUE)  and (dizaines == NOMBRE_MAGIQUE))
         or  ((dizaines == NOMBRE_MAGIQUE ) and (unites == NOMBRE_MAGIQUE))
         or  (unitesDivisiblesParQuatre)
        ) :
        return True
    
    return False



# 8. Cette fonction retourne un nombre minimal de pieces de monnaie
#
# Parametres: 
#   montantDollar: float - montant total en dollars
# return:
#   nombre minimum de pieces - int
def numMonnaies(montantDollar: float) -> int:
    centimesMontant = montantDollar * 100

    # total possible de pieces de 25sous (utiiser operateur "floor")
    total25sous = centimesMontant // 25
    centimesMontant = centimesMontant - (total25sous * 25)

    
    # total possible piece de 10sous
    total10sous = centimesMontant // 10
    # on peut aussi utiliser modulo '%' au lieu
    centimesMontant = centimesMontant - (total10sous * 10)

    # total possible piece de 5sous
    total5sous = centimesMontant // 5
    centimesMontant = centimesMontant - (total5sous * 5)

     # total possible pieces de 1sous
    total1sous = centimesMontant // 1
    centimesMontant = centimesMontant - (total1sous * 1)

    print(f"{total25sous:.0f} pieces de 25 cents, {total10sous:.0f} pieces de 10 cents, {total5sous:.0f} pieces de 5 cents, {total1sous:.0f} pieces de 1 cent")

    return int(total25sous + total10sous + total5sous + total1sous)






