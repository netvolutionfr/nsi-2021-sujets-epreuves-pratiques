def recherche(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = 0
    trouve = False
    while i < n - g and trouve is False:
        j = 0
        while j < g and gene[j] == seq_adn[i+j]:
            j = j+1
        if j == g:
            trouve = True
        i = i+1
    return trouve


# print(recherche("AATC", "GTACAAATCTTGCC"))
# print(recherche("AGTC", "GTACAAATCTTGCC"))

assert(recherche("AATC", "GTACAAATCTTGCC"))
assert(recherche("AGTC", "GTACAAATCTTGCC") is False)
