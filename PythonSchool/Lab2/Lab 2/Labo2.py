# Juliane Bruck, 8297746, ITI-1520


#1. division de deux entiers
entier1= int(input("SVP entrez un entier : "))
entier2 = int(input("SVP entrez un autre entier : "))

def division_entiere (entier1, entier2):    
    resultat = entier1 // entier2
    return (resultat)

def restant_modulo (entier1, entier2):
    resultat2 = entier1 % entier2
    return (resultat2)
    
globalresult = division_entiere(entier1, entier2)
globalmod = restant_modulo(entier1, entier2)
print(f" resultat {globalresult} de classe modulo {globalmod} ")


# 2. Cette fonction transforme la temperature de celsius en fahrenheit
#temp_Fahrenheit est une variable locale a la fct
def celsius_en_fahrenheit (temp_Celsius):
    temp_Fahrenheit = (temp_Celsius * 9.0/5.0) + 32
    return temp_Fahrenheit

#t_fahrenheit et t_celsius sont des variables globales

t_celsius = 100
t_fahrenheit = celsius_en_fahrenheit(t_celsius) 
print(t_celsius, "Celsius est", t_fahrenheit, "Fahrenheit." )

#3. fonction qui clcule la note finale

def note_finale(devoirsMoyenne, partiel, examen):
    if (devoirsMoyenne >=0 and partiel >= 0 and examen >=0 ):
        note = (devoirsMoyenne*25/100)+(partiel*25/100)+(examen*50/100)
    return (note)

# 4. algorithme pour calculer la surface d'un triangle

from math import sqrt
def surface_triangle (cote1, cote2, cote3):
    p= cote1+cote2+cote3
    s= sqrt(p*(p-2*cote1)*(p-2*cote2)*(p-2*cote3))/4
    return (s) 
