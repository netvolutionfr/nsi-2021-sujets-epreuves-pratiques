def rendu(somme_a_rendre):
    n1 = 0
    n2 = 0
    n3 = 0
    reste = somme_a_rendre
    while reste >= 5:
        n1 += 1
        reste -= 5
    while reste >= 2:
        n2 += 1
        reste -= 2
    while reste >= 1:
        n3 += 1
        reste -= 1
    return [n1, n2, n3]

