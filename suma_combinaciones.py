# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import itertools as it

comb=list(it.combinations([4,5,7,9], 2))

print(comb)
sumas=[]
for i in range(len(comb)):
    sumas.append(sum(comb[i]))
    print(sum(comb[i]))

print(sumas)
