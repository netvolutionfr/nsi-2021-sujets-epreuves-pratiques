def occurence_lettres(phrase):
    dict = {}
    for lettre in phrase:
        dict[lettre] = 0
    for lettre in phrase:
        dict[lettre] += 1
    return dict


def occurence_lettres_2(phrase):
    nombre_lettres = {k: phrase.count(k) for k in phrase}
    return nombre_lettres


print(occurence_lettres('Hello, World!'))
print(occurence_lettres_2('Hello, World!'))
