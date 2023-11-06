
# Excercice 3


class CompteBancaire(object):
    '''classe CompteBancaire'''

    def __init__(self, nom='Dupont', solde=1000):
        '''(CompteBancaire)-> None'''
        self.nom = nom
        self.solde = solde

    def depot(self, somme):
        self.solde += somme

    def retrait(self, somme):
        self.solde -= somme

    def affiche(self):
        print(
            f"Le solde du compte bancaire de {self.nom} est de {self.solde} dollars. ")

    def __repr__(self):
        '''(CompteBancaire)-> str'''
        return (str(self.nom) + ":" + str(self.solde))

    def __eq__(self, autre):
        '''(CompteBancaire)-> bool'''
        return self.nom == autre.nom


# compte1 = CompteBancaire('Duchmol', 800)
# compte1.depot(350)
# compte1.retrait(200)
# compte1.affiche()
# compte2 = CompteBancaire()
# compte2.depot(25)
# compte2.affiche()


class CompteEpargne(CompteBancaire):
    '''classe CompteEpargne'''

    def __init__(self,  nom='Dupont', solde=1000, taux=0.3):
        '''(CompteBancaire)-> None'''
        CompteBancaire.__init__(self, nom, solde)
        self.taux = taux

    def changeTaux(self, valeur):
        self.taux = valeur

    def capitalisation(self, nombreMois):
        self.solde += self.solde * (nombreMois * (self.taux/100))
        print(
            f"Capitalisation sur {nombreMois} mois au taux mensuel de {self.taux} %")


# c1 = CompteEpargne('Duvivier', 600)
# c1.depot(350)
# c1.affiche()
# c1.capitalisation(12)
# c1.affiche()
# c1.changeTaux(.5)
# c1.capitalisation(12)
# c1.affiche()
