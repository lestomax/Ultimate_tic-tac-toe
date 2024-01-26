from fun_joueurs import *
from time import time

def ab_ab_5__min_min_5():# gagnant : 1, 4.43258810043335 166.5157072544098
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
def ab_ab_6(): #gagnant : 0, 15.775174856185913
    t=time()
    def j1(grid,j1,case):
        return alphabeta(grid,j1,case,6)
    jeu(j1,j1)
    t2=time()-t
    print(t2)
def ab_ab_7(): #gagnant : -1, 67.22728395462036
    t=time()
    def j1(grid,j1,case):
        return alphabeta(grid,j1,case,7)
    jeu(j1,j1)
    t2=time()-t
    print(t2)
def ab_7_ab_6(): #gagnant : 0, 84.43180680274963
    t=time()
    def j1(grid,j1,case):
        return alphabeta(grid,j1,case,7)
    def j2(grid,j1,case):
        return alphabeta(grid,j1,case,6)
    jeu(j1,j2)
    t2=time()-t
    print(t2)
def ab_7_ab_5(): #gagnant : 1, 32.7816641330719
    t=time()
    def j1(grid,j1,case):
        return alphabeta(grid,j1,case,7)
    def j2(grid,j1,case):
        return alphabeta(grid,j1,case,5)
    jeu(j1,j2)
    t2=time()-t
    print(t2)
def ab_rand():
    dico = {}
    for i in range(3,8):
        dico[i]=[]
        def j1(grid,j1,case):
            return alphabeta(grid,j1,case,i)
        for j in range(10):
            t=time()
            g=jeu(j1,jeu_random)
            t2=time()-t
            dico[i].append((g,t2))
    print(dico)
def ab_3_rand__1000(): #96.45
    c=0
    def j1(grid,j1,case):
        return alphabeta(grid,j1,case,3)
    for i in range(1000):
        c+=jeu(j1,jeu_random)+1
    print(c/20)
def ab_4_rand__1000(): #96.45
    c=0
    def j1(grid,j1,case):
        return alphabeta(grid,j1,case,4)
    for i in range(1000):
        c+=jeu(j1,jeu_random)+1
    print(c/20)
ab_ab_6()