from environment import *
from math import inf,sqrt,log

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

def minmax(grid:Grid,j1:Joueur,case:int,profondeur = 4):
    """En réalité c'est un Negamax"""
    assert not grid.fini
    def aux1(grid:Grid,j1:Joueur,case:int,plage = 4):
        joueur = j1.id
        if grid.fini or plage == 0:
            return grid.evaluation*joueur
        c=-inf
        #parcours des fils
        if case == -1: #si nous avons le choix total de la case
            for i in range(9):
                if grid.gros[i] == 0: #verification que la grande case est vide
                    for j in range(9):
                        if grid.get_petite_case(i,j) == 0 : #verification que la petite case est vide
                            g = grid.copy()
                            g.set(i,j,j1)
                            if g.gros[j]== 0:
                                place = j
                            else:
                                place = -1
                            j2 = Joueur(j1.fun,-j1.id)
                            value = aux1(g,j2,place,plage-1) #on simule l'appel de la fonction par le joueur opposé
                            if c < -value:
                                c = -value 
                                couple = (i,j)
        else: #la grande case est spécifiée (j'aurais pu faire une fonction commune car c'est sensiblement la même chose, sauf qu'il aurait fallu rendre certaines variables comme c et couple, globales)
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
        if plage == profondeur : 
            assert c != -inf, "je ne peux aller nulle part"
            return couple #il est toujours defini car c != inf, donc c à été changé et couple a été defini 
        return c
    return aux1(grid,j1,case,profondeur)

def alphabeta(grid:Grid,j1:Joueur,case:int,profondeur = 4):
    """En réalité c'est un Negamax"""
    assert not grid.fini
    def aux1(grid:Grid,j1:Joueur,case:int,plage = 4,alpha = -inf,beta = inf):
        joueur = j1.id
        if grid.fini or plage == 0:
            return grid.evaluation*joueur
        #parcours des fils
        if case == -1: #si nous avons le choix total de la case
            for i in range(9):
                if grid.gros[i] == 0: #verification que la grande case est vide
                    for j in range(9):
                        if grid.get_petite_case(i,j) == 0 : #verification que la petite case est vide
                            g = grid.copy()
                            g.set(i,j,j1)
                            if g.gros[j]== 0:
                                place = j
                            else:
                                place = -1
                            j2 = Joueur(j1.fun,-j1.id)
                            value = aux1(g,j2,place,plage-1,-beta,-alpha) #on simule l'appel de la fonction par le joueur opposé
                            if -value>=beta:
                                return beta
                            elif alpha < -value:
                                alpha = -value 
                                couple = (i,j)
        else: #la grande case est spécifiée (j'aurais pu faire une fonction commune car c'est sensiblement la même chose, sauf qu'il aurait fallu rendre certaines variables comme c et couple, globales)
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
                    value = aux1(g,j2,place,plage-1,-beta,-alpha) #on simule l'appel de la fonction par le joueur opposé
                    if -value>=beta:
                        return beta
                    elif alpha < -value:
                        alpha = -value 
                        couple = (i,j)
        if plage == profondeur : 
            assert alpha != -inf, "je ne peux aller nulle part"
            return couple #il est toujours defini car c != inf, donc c à été changé et couple a été defini 
        return alpha
    return aux1(grid,j1,case,profondeur)

N=0
def montecarlo(grid:Grid,j1:Joueur,case:int,n_iter = 500,c:int=sqrt(2)):
    """At least n_iter = 81"""
    joueur = j1.id
    class Arbre:
        def __init__(self,val:Grid,j=j1,cas=case) -> None:
            global N
            self.grille:Grid=val
            self.nb_passage=0
            self.val=0
            self.fils:list[Arbre]=[]
            self.chemin_fils:list[tuple]=[]
            self.case_suivante=cas
            self.joueur=j
            self.id=N+1
            N+=1
        def genere_fils(self):
            case = self.case_suivante
            if case == -1: #si nous avons le choix total de la case
                for i in range(9):
                    if grid.gros[i] == 0: #verification que la grande case est vide
                        for j in range(9):
                            if grid.get_petite_case(i,j) == 0 : #verification que la petite case est vide
                                g = grid.copy()
                                g.set(i,j,self.joueur)
                                if g.gros[j]== 0:
                                    place = j
                                else:
                                    place = -1
                                self.fils.append(Arbre(g,Joueur(self.joueur.fun,-self.joueur.id),place))
                                self.chemin_fils.append((i,j))
            else: #la grande case est spécifiée (j'aurais pu faire une fonction commune car c'est sensiblement la même chose)
                i = case
                assert grid.gros[i] == 0, "on ne m'a pas donné une case valable"
                for j in range(9):
                    if grid.get_petite_case(i,j) == 0 :
                        g = grid.copy()
                        g.set(i,j,self.joueur)
                        if g.gros[j]== 0:
                            place = j
                        else:
                            place = -1
                        self.fils.append(Arbre(g,Joueur(self.joueur.fun,-self.joueur.id),place))
                        self.chemin_fils.append((i,j))
        def est_feuille(self):
            return not bool(self.fils)
        
    racine:Arbre = Arbre(grid)
    racine.genere_fils()
    def choix_fils(self):
        assert not self.est_feuille()
        m=-inf
        for fils in self.fils:
            if fils.nb_passage == 0:
                return fils
            ucb=(fils.val/fils.nb_passage)+c*sqrt(log(racine.nb_passage)/fils.nb_passage)
            if ucb>m :#UCB1
                f=fils
                m=ucb
        return f
    Arbre.choix_fils=choix_fils
    
    current:Arbre = racine
    def rollout(arbre:Arbre):
        return jeu(jeu_random,jeu_random,arbre.grille.copy(),arbre.joueur.id,affichage_gagnant=False,affichage_grille=False)*joueur

    chemin = [racine]
    for i in range(n_iter):
        while not current.est_feuille():
            current = current.choix_fils()
            assert 0<current.id <=len(racine.fils) or not current in [a.id for a in chemin]
            chemin.append(current)
        if current.nb_passage == 0 :
            resultat=rollout(current)
        else:
            current.genere_fils()
            if not current.est_feuille():
                current=current.fils[0]
            resultat=rollout(current)
        current = racine
        for arbre in chemin:
            arbre.nb_passage+=1
            arbre.val+=resultat
    m=-inf
    i=0
    n=-1
    somme = 0
    for a in racine.fils:
        somme+=a.nb_passage
        if a.val/a.nb_passage > m :
            m = a.val/a.nb_passage
            arbre = a
            n = i
        i+=1
    print(somme)
    return racine.chemin_fils[n]