def recherche(a, t):
    compteur = 0
    for i in t:
        if a == i:
            compteur = compteur + 1
    return compteur


assert recherche(5, []) == 0
assert recherche(5, [-2, 3, 4, 8]) == 0
assert recherche(5, [-2, 3, 1, 5, 3, 7, 4]) == 1
assert recherche(5, [-2, 5, 3, 5, 4, 5]) == 3
