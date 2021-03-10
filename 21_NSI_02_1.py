def moyenne(l):
    total = 0
    nb = 0
    for i in range(len(l)):
        total = total + l[i]
        nb = nb + 1
    if nb == 0:
        print('erreur')
    else:
        moy = float(total) / nb
        print(moy)


moyenne([5, 3, 8])
moyenne([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
moyenne([])
