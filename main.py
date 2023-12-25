from fun_joueurs import *
from time import time

def test1():# gagnant : 1, 4.43258810043335 166.5157072544098
    t=time()
    def j1(grid,j1,case):
        return alphabeta(grid,j1,case,5)
    jeu(j1,j1)
    t1=time()-t
    t=time()
    def j1(grid,j1,case):
        return minmax(grid,j1,case,5)
    jeu(j1,j1)
    t2=time()-t
    print(t1,t2)
test1()