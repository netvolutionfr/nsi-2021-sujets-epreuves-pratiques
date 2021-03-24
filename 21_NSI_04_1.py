def moyenne(tab):
    total = 0
    count = 0
    for n in tab:
        total = total + n
        count = count + 1
    if n > 1:
        moy = total / n
    else:
        moy = total
    return moy


assert moyenne([1]) == 1
assert moyenne([1, 2, 3, 4, 5, 6, 7]) == 4
assert moyenne([1, 2]) == 1.5
