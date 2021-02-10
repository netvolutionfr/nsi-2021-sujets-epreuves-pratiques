def maxi(tab):
    position = 0
    max = tab[0]
    compteur = 0
    for elt in tab:
        if elt > max:
            max = elt
            position = compteur
        compteur = compteur + 1

    return max, position


print(maxi([1,5,6,9,1,2,3,7,9,8]))
