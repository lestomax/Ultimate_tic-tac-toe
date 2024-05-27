from fun_joueurs import *
from time import time
from functools import partial
import sys

def determine_c():
    original = sys.stdout
    f=open("Determine la constante","w")
    sys.stdout=f
    print("Determination de la constante C dans montecarlo")
    d={}
    for const in [0,0.5,sqrt(2),3,5]:
        d[const]=0
        for j in range(100):
            if jeu(partial(montecarlo,c=const,n_iter=1000),partial(alphabeta,profondeur=2),affichage_gagnant=False,affichage_grille=False) ==1:
                d[const]+=1
    print(d)
    sys.stdout=original
    f.close()

def calcul_temps(fun):
    t=time()
    jeu(fun,fun,affichage_gagnant=False,affichage_grille=False)
    dt=time()-t
    return dt

def temps_de_calcul():
    original = sys.stdout
    f=open("Temps de calcul","w")
    sys.stdout=f
    print("Voici le temps de calcul des différents algorithmes :")
    print("Aléatoire :", calcul_temps(jeu_random))
    for i in range(1,6,2):
        print("Minmax","profondeur",i, ":", calcul_temps(partial(minmax,profondeur=i))/2)
    for i in range(1,8,2):
        print("AlphaBeta","profondeur",i, ":", calcul_temps(partial(alphabeta,profondeur=i))/2)
    for i in range(1,8,2):
        print("AlphaBeta (avec tri des enfants)","profondeur",i, ":", calcul_temps(partial(alphabeta,profondeur=i))/2)
    for i in [100,500,1000,2000]:
        print("MCTS",i,"itérations :", calcul_temps(partial(montecarlo,n_iter=i))/2)
    sys.stdout=original
    f.close()

def duels():
    joueurs = [jeu_random,partial(montecarlo,n_iter=100),partial(montecarlo,n_iter=500),partial(montecarlo,n_iter=1000),partial(alphabeta,profondeur=1),partial(alphabeta,profondeur=3),partial(alphabeta,profondeur=5)]
    w=[[0]*7 for i in range(7)]
    l=[[0]*7 for i in range(7)]
    e=[[0]*7 for i in range(7)]
    for i in range(len(joueurs)):
        for j in range(len(joueurs)): #pour prendre en compte qui commence
            for k in range(100):
                resultat = jeu(joueurs[i],joueurs[j],affichage_gagnant=False,affichage_grille=False)
                if resultat == 0:
                    e[i][j]+=1
                elif resultat == 1:
                    w[i][j]+=1
                else:
                    l[i][j]+=1
    return w,l,e


def main():
    determine_c()
    temps_de_calcul()
#main()