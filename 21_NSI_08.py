Pieces = [100,50,20,10,5,2,1]


def rendu_glouton(arendre, solution=None, i=0):
    if solution is None:
        solution = []
    if arendre == 0:
       return solution
    p = Pieces[i]
    if p <= arendre:
        solution.append(p)
        return rendu_glouton(arendre - p, solution,i)
    else:
        return rendu_glouton(arendre, solution, i+1)


print(rendu_glouton(100,[],0))
print(rendu_glouton(68,[],0))
print(rendu_glouton(291,[],0))
