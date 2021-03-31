def recherche(caractere, mot):
    nombre = 0
    for lettre in mot:
        if lettre == caractere:
            nombre += 1
    return nombre


assert(recherche('e', "sciences")) == 2
assert(recherche('i',"mississippi")) == 4
assert(recherche('a',"mississippi")) == 0