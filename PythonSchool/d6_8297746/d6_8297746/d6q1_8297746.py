# Juliane Bruck
# 8297746
# Devoir 6


# !! The UML diagram in the question is wrong on 2 counts
#  1. the arrows showing inheritance are backwards
#  2. The arrow tip is incorrect - doesn't show inheritance
#     https://en.wikipedia.org/wiki/Class_diagram#/media/File:KP-UML-Generalization-20060325.svg


class Personne:
    '''represente une classe Personne'''

    def __init__(self, nom: str, prenom: str, identifiant: int):
        '''(str,str, int)->None
        initialise les attributs de la classe Personne'''
        # A completer
        self.nom = nom
        self.prenom = prenom
        self.identifiant = identifiant

    def __repr__(self):
        '''(Personne)->str
        retourne une representation de l'objet'''
        # A completer
        return f"{{nom:{self.nom}, prenom:{self.prenom}, identifiant:{self.identifiant}}}"

    def __eq__(self, autre) -> bool:
        '''(Personne, Personne)->bool
        self == autre si le même nom, le même prénom et le même identifiant'''
        # A completer
        return self.nom == autre.nom and self.prenom == autre.prenom and self.identifiant == autre.identifiant


#
# Etudiant
#
#
class Etudiant(Personne):
    '''represente une classe Etudiant'''
    # solde est un attribut de la classe Etudiant
    # cours est une liste de cours (une liste de chaine de caracteres)

    def __init__(self, nom, prenom, identifiant, solde: float, cours: list = []):
        '''(str,str, int)->None
        initialise les attributs de la classe Personne'''
        # A completer
        Personne.__init__(self, nom, prenom, identifiant)
        self.solde = solde
        self.cours = cours

    # methodes
    # A completer

    def __repr__(self):
        '''(Etudiant)->str
        retourne une representation de l'objet'''
        # A completer

        # !!! The instructions say to print the number of courses but the sample output prints the entire list
        return f"{{nom:{self.nom}, prenom:{self.prenom}, identifiant:{self.identifiant}, solde:{self.solde}, nombre cours:{len(self.cours)}}}"

    #
    # The UML diagram shows ajouterCours returning a float when it should return a bool
    #
    def ajouterCours(self, cour: str):
        ''' Un étudiant peut ajouter un cours seulement si il n’a aucun solde à payer 
            (la valeur de solde est égale à zéro). Cette fonction retourne 
            True si le cours a été ajouté dans la liste de cours et False sinon.'''
        courseAdded = False
        if self.solde == 0:
            if cour not in self.cours:
                self.cours.append(cour)
                courseAdded = True
        return courseAdded


#
# Employe
#
#
class Employe(Personne):
    '''represente un employe'''
    # tauxHoraire est un attribut de la classe Employe

    def __init__(self, nom, prenom, identifiant, tauxHoraire: float):
        '''(str,str, int)->None
        initialise les attributs de la classe Personne'''
        # A completer
        Personne.__init__(self, nom, prenom, identifiant)
        self.tauxHoraire = tauxHoraire

    # methodes
    def __repr__(self):
        '''(Employe)->str
        retourne une representation de l'objet'''
        # A completer
        return f"{{nom:{self.nom}, prenom:{self.prenom}, identifiant:{self.identifiant}, taux horaire:{self.tauxHoraire}}}"

    def calculerSalaire(self, nombreHeures: int):
        return nombreHeures * self.tauxHoraire


#
# Gestion
#
#
class Gestion:
    listEtudiant = []
    listEmploye = []

    def ajouterEtudiant(self):
        ''' none -> bool
        ajouter des etudiants dans une liste d'etudiant'''
        # A completer

        nom = str(input(" Entrez le nom: "))
        prenom = str(input(" Entrez le prenom: "))
        identifiant = int(input(" Entrez votre identifiant: "))
        solde = float(input(" Entrez le solde: "))

        courseList = str(
            input(" Entrez une liste de cours separe par des virgules: ")).lower().split(",")

        etudiant = Etudiant(nom, prenom, identifiant, solde, courseList)

        addCourse = str(input(" Veux-tu ajouter un autre cours? ")).lower()
        if addCourse == "oui":
            courseName = str(input(" Entrez le cours a ajouter: "))
            studentAdded = etudiant.ajouterCours(courseName)
            if not studentAdded:
                print(" Vous devez payer votre solde avant d'ajouter un cours.")
        else:
            print(" Vouz avez choisi de ne pas ajouter aucun cours.")

        alreadyAdded = etudiant in Gestion.listEtudiant
        if not alreadyAdded:
            Gestion.listEtudiant.append(etudiant)
            print(" Etudiant ajoute avec succes.")
            return True
        print(" Etudiant na pas ajouter.")
        return False

    def ajouterEmploye(self):
        ''' none -> bool
        ajouter des etudiants dans une liste d'etudiant'''
        # A completer

        nom = str(input(" Entrez le nom: "))
        prenom = str(input(" Entrez le prenom: "))
        identifiant = int(input(" Entrez votre identifiant: "))
        tauxHoraire = float(input(" Entrez le taux horaire: "))

        employee = Employe(nom, prenom, identifiant, tauxHoraire)

        alreadyAdded = employee in Gestion.listEmploye
        if not alreadyAdded:
            Gestion.listEmploye.append(employee)
            print(" Employe ajoute avec succes.")
            return True
        print(" Employe na pas ajouter.")
        return False

    def SoldeNonPaye(self) -> int:
        ''' none -> int
        retourner le nombre des etudiants qui ont un solde non paye'''
        # A completer
        count = 0
        for etudiant in Gestion.listEtudiant:
            if etudiant.solde != 0:
                count += 1
        return count

    # This is named differently in the UML diagram vs this file
    def salaireEmploye(self, employe, heures):
        '''(str) -> float
        retourne le salaire d'un employe'''
        # A completer

        if employe not in Gestion.listEmploye:
            return 0
        return employe.tauxHoraire * heures


# program principal
g = Gestion()
print("Ajoutez des etudiants.")
# Ajouter des etudiants
g.ajouterEtudiant()
g.ajouterEtudiant()

# Ajouter des employes
print("Ajouter des employes.")
g.ajouterEmploye()
g.ajouterEmploye()

# Afficher le nombre des employes et des etudiants
print("il y a: ", len(Gestion.listEtudiant), " etudiants.")
print("il y a: ", len(Gestion.listEmploye), " employes.")
# Afficher le nombre des etudiants qui ont un solde a payer
print("il y a ", g.SoldeNonPaye(), "etudiants qui n'ont pas paye leur solde.")
# Afficher les salaires de tous les employes
for e in Gestion.listEmploye:
    heure = int(input("Entrez le nombre des heures pour employe " +
                      e.prenom + " " + e.nom + ": "))
    print('Le salaire de:', e.nom, e.prenom,
          'est:', g.salaireEmploye(e, heure), '$.')

# Afficher toute la Gestion

# !! the sample output does not print this line.
print("Toute la gestion: ")
print(Gestion.listEtudiant)
print(Gestion.listEmploye)
