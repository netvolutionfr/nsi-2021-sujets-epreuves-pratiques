def recherche(elt, tab):
    liste = []
    i = 0
    for e in tab:
        if elt == e:
            liste.append(i)
        i = i + 1
    return liste


assert(recherche(3, [3, 2, 1, 3, 2, 1]) == [0, 3])
assert(recherche(4, [1, 2, 3]) == [])
