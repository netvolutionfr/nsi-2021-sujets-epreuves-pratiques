def recherche(tab):
    couples = []
    for i in range(len(tab)-1):
        if tab[i] + 1 == tab[i+1]:
            couples.append((tab[i], tab[i+1]))
    return couples


print(recherche([1, 4, 3, 5]))
print(recherche([1, 4, 5, 3]))
print(recherche([7, 1, 2, 5, 3, 4]))
print(recherche([5, 1, 2, 3, 8, -5, -4, 7]))
