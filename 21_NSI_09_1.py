def moyenne(l):
    total = 0
    coef = 0
    for couple in l:
        total = total + float(couple[0]) * couple[1]
        coef = coef + couple[1]
    if coef > 0:
        moy = total / coef
        print(moy)
    else:
        print('erreur')


moyenne([(15,2),(9,1),(12,3)])
