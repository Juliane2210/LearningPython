
# Excercice 2


class Voiture:
    '''classe Voiture'''

    personne = 'personne'

    def __init__(self, marque='Ford', couleur='rouge'):
        '''(Voiture)-> None'''
        self.marque = marque
        self.couleur = couleur
        self.pilote = Voiture.personne
        self.vitesse = 0

    def choix_conducteur(self, nom):
        self.pilote = nom

    def accelerer(self, taux, duree):
        if self.pilote == Voiture.personne:
            print("Cette voiture n'a pas de conducteur !")
        else:
            self.vitesse = taux * duree

    def affiche_tout(self):
        print(
            f"{self.marque} {self.couleur} pilotee par {self.pilote}, vitesse = {self.vitesse} m/s")

    def __repr__(self):
        '''(Voiture)-> str'''
        return (str(self.marque) + ":" + str(self.couleur) + ":" + str(self.pilote))

    def __eq__(self, autre):
        '''(Voiture)-> bool'''
        return self.marque == autre.marque and self.couleur == autre.couleur


a1 = Voiture('Peugeot', 'bleue')
a2 = Voiture(couleur='verte')
a3 = Voiture('Mercedes')
a1.choix_conducteur('Roméo')
a2.choix_conducteur('Juliette')
a2.accelerer(1.8, 12)
a3.accelerer(1.9, 11)
a2.affiche_tout()
a3.affiche_tout()
