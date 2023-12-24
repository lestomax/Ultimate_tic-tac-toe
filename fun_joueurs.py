from environment import *
from math import inf

def jeu_random(g:Grid,skip,case):
    if case ==-1 : 
        i,j = (randint(0,8),randint(0,8))
        print(case)
        while g.get_case(i,g.gros)!=0 or g.get_petite_case(i,j)!=0:
            i,j = (randint(0,8),randint(0,8))
        return i,j
    i = randint(0,8)
    while g.get_petite_case(case,i)!=0:
        i = (randint(0,8))
    return case, i

def jeu_player(_,skip,case):
    if case ==-1 :
        return (int(input("Grande case numero: ")),int(input("Petite case numero: ")))
    return (case,int(input("Petite case numero: ")))

# def minmax(grid:Grid,joueur:int,case:int,plage = 4):
#     if grid.fini or plage == 0:
##         return grid.evaluation*joueur
    