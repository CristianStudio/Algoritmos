# Sumas de las combinaciones de una lista
import itertools as it

comb=list(it.combinations([4,5,7,9], 2))

print(comb)
sumas=[]
for i in range(len(comb)):
    sumas.append(sum(comb[i]))
    # print(sum(comb[i]))

print(sumas)
