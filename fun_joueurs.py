from environment import *
from math import inf

def jeu_random(g:Grid,skip,case:int):
    if case ==-1 : 
        i,j = (randint(0,8),randint(0,8))
        while g.get_case(i,g.gros)!=0 or g.get_petite_case(i,j)!=0:
            i,j = (randint(0,8),randint(0,8))
        return i,j
    i = randint(0,8)
    while g.get_petite_case(case,i)!=0:
        i = (randint(0,8))
    return case, i

def jeu_player(_,skip,case:int):
    if case ==-1 :
        return (int(input("Grande case numero: ")),int(input("Petite case numero: ")))
    return (case,int(input("Petite case numero: ")))

def minmax(grid:Grid,j1:Joueur,case:int,p1 = 4):
    assert not grid.fini
    def aux1(grid:Grid,j1:Joueur,case:int,plage = 4):
        joueur = j1.id
        if grid.fini or plage == 0:
            return grid.evaluation*joueur
        c=-inf
        if case == -1:
            for i in range(9):
                if grid.gros[i] == 0:
                    for j in range(9):
                        if grid.get_petite_case(i,j) == 0 :
                            g = grid.copy()
                            g.set(i,j,j1)
                            if g.gros[j]== 0:
                                place = j
                            else:
                                place = -1
                            j2 = Joueur(j1.fun,-j1.id)
                            value = aux1(g,j2,place,plage-1)
                            if c < -value:
                                c = -value 
                                couple = (i,j)
        else:
            i = case
            assert grid.gros[i] == 0, "on ne m'a pas donné une case valable"
            for j in range(9):
                if grid.get_petite_case(i,j) == 0 :
                    g = grid.copy()
                    g.set(i,j,j1)
                    if g.gros[j]== 0:
                        place = j
                    else:
                        place = -1
                    j2 = Joueur(j1.fun,-j1.id)
                    value = aux1(g,j2,place,plage-1)
                    if c < -value:
                        c = -value
                        couple = (i,j)
        if plage == p1 : 
            assert c != -inf, "je ne peux aller nulle part"
            return couple
        return c
    return aux1(grid,j1,case)