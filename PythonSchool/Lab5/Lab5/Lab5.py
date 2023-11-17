# Juliane Bruck

# Labo 5
#

# Q1
def moyenne(a):
    somme = 0
    for v in a:
        somme = somme + int(v)
    return (somme/len(a))


# Q2


def maximum(l):
    maxi = l[0]
    for i in range(1, len(l)):
        if l[i] > maxi:
            maxi = l[i]
    return maxi


def minimum(l):
    mini = l[0]
    for i in range(1, len(l)):
        if l[i] < mini:
            mini = l[i]
    return mini


def notes():
    l = input(' Veuillez entrer vos notes separe par des virgules:')
    realList = list(eval(l))
    m = moyenne(realList)
    maxi = maximum(realList)
    mini = minimum(realList)
    print(
        f"La moyenne est {m}, le maximum est {maxi} et le minimum est {mini}.")


notes()
