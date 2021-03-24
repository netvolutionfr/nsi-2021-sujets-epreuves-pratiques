def recherche(tab, n):
    gauche = 0
    droite = len(tab) - 1
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if tab[milieu] == n:
            return milieu
        elif tab[milieu] > n:
            droite = milieu - 1
        else:
            gauche = milieu + 1
    return -1


print(recherche([2, 3, 4, 5, 6], 5))
print(recherche([2, 3, 4, 6, 7], 5))
