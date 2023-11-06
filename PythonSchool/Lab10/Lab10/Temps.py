class Temps:
    '''classe Temps'''

    def __init__(self, h=12, m=0, s=0):
        '''(Temps)-> None'''
        self.heure = h
        self.minute = m
        self.seconde = s

    def setTemps(self, h, m=0, s=0):
        '''(Temps)-> None'''
        self.heure = h
        self.minute = m
        self.seconde = s

    def affiche_heure(self):
        '''(Temps)-> None'''
        print("{0}:{1}:{2}".format(self.heure, self.minute, self.seconde))

    def __repr__(self):
        '''(Temps)-> str'''
        return (str(self.heure) + ":" + str(self.minute) + ":" + str(self.seconde))

    def __eq__(self, autre):
        '''(Temps)-> bool'''
        return self.heure == autre.heure and self.minute == autre.minute and self.seconde == autre.seconde


# Excercice #1

    def estAvant(self, t2: object):
        if self.heure < t2.heure or \
            (self.heure == t2.heure and self.minute < t2.minute) or \
                (self.heure == t2.heure and self.minute == t2.minute and self.seconde < t2.seconde):
            return True
        return False

    def duree(self, t2: object):
        dureeHeure = t2.heure - self.heure
        dureeMin = t2.minute - self.minute
        dureeSec = t2.seconde - self.seconde
        return Temps(dureeHeure, dureeMin, dureeSec)


t1 = Temps(12, 4, 0)
t2 = Temps(10, 2, 1)
print(t1.estAvant(t2))
print(t2.estAvant(t1))
t1.estAvant(t2)
t2.setTemps(12, 45, 2)
print(t1.duree(t2))
