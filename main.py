from fun_joueurs import *
from time import time
from functools import partial

def ab_ab_5__min_min_5():# gagnant : 1, 4.43258810043335 166.5157072544098
    t=time()
    j1=partial(alphabeta,profondeur=5)
    jeu(j1,j1)
    t1=time()-t
    t=time()
    j1=partial(minmax,profondeur=5)
    jeu(j1,j1)
    t2=time()-t
    print(t1,t2)
def ab_ab_6(): #gagnant : 0, 15.775174856185913
    t=time()
    j1=partial(alphabeta,profondeur=6)
    jeu(j1,j1)
    t2=time()-t
    print(t2)
def ab_ab_7(): #gagnant : -1, 67.22728395462036
    t=time()
    j1=partial(alphabeta,profondeur=7)
    jeu(j1,j1)
    t2=time()-t
    print(t2)
def ab_7_ab_6(): #gagnant : 0, 84.43180680274963
    t=time()
    j1=partial(alphabeta,profondeur=7)
    j2=partial(alphabeta,profondeur=6)
    jeu(j1,j2)
    t2=time()-t
    print(t2)
def ab_7_ab_5(): #gagnant : 1, 32.7816641330719
    t=time()
    j1=partial(alphabeta,profondeur=7)
    j2=partial(alphabeta,profondeur=5)
    jeu(j1,j2)
    t2=time()-t
    print(t2)
def ab_rand():
    dico = {}
    for i in range(3,8):
        dico[i]=[]
        j1=partial(alphabeta,profondeur=i)
        for j in range(10):
            t=time()
            g=jeu(j1,jeu_random)
            t2=time()-t
            dico[i].append((g,t2))
    print(dico)
def ab_3_rand__1000(): #96.45
    c=0
    j1=partial(alphabeta,profondeur=3)
    for i in range(1000):
        c+=jeu(j1,jeu_random)+1
    print(c/20)
def ab_4_rand__1000(): #96.45
    c=0
    j1=partial(alphabeta,profondeur=4)
    for i in range(1000):
        c+=jeu(j1,jeu_random)+1
    print(c/20)

def ab_7_ab_6_opti(): #200
    t=time()
    j1=partial(alpha_beta_opti,profondeur=7)
    j2=partial(alpha_beta_opti,profondeur=6)
    jeu(j1,j2)
    t2=time()-t
    print(t2)

def montecarlo_alpha_beta():
    d={}
    s=0
    for const in range(1000,2000,1):
        const = const/1000
        d[const]=0
        for _ in range(1000):
            if jeu(partial(montecarlo,c=const,n_iter=100,strategie=partial(alphabeta,profondeur=3)),partial(alphabeta,profondeur=5),affichage_gagnant=False,affichage_grille=False) !=-1:
                d[const]+=1
                s+=1
    print(d)
    print(s)

#montecarlo_alpha_beta()
ab_7_ab_6_opti()