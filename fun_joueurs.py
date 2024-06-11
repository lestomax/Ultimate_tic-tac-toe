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
    """En réalité c'est un Negamax Alpha beta"""
    assert not grid.fini
    def aux1(grid:Grid,j1:Joueur,case:int,plage = 4,alpha = -inf,beta = inf):
        joueur = j1.id
        if grid.fini or plage == 0: #on a atteint une feuille (la profondeur)
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
        if plage == profondeur : #on a fini l'exploration et on est à la racine, dans ce cas on envoie où aller
            assert alpha != -inf, "je ne peux aller nulle part"
            return couple #il est toujours defini car c != inf, donc c à été changé et couple a été defini 
        return alpha #si on n'a pas fini on renvoie le meilleur coup trouvé jusque maintenant
    return aux1(grid,j1,case,profondeur)

def alpha_beta_opti(grid:Grid,j1:Joueur,case:int,profondeur = 4):
    """En réalité c'est un Negamax Alpha beta"""
    assert not grid.fini
    def aux1(grid:Grid,j1:Joueur,case:int,plage = 4,alpha = -inf,beta = inf):
        """Renvoie """
        joueur = j1.id
        if grid.fini or plage == 0:
            return grid.evaluation*joueur
        
        #tri des fils (OPTIMISATION)
        def val_coup(i,j):
            """Compare la valeur de la grille entre 2 coups pour un joueur donné"""
            g1 = grid.copy()
            g1.set(i,j,j1)
            return g1.evaluation*joueur
        
        #parcours des fils
        if case == -1: #si nous avons le choix total de la case
            t = [(i,j,val_coup(i,j)) for i in range(9) for j in range(9) if grid.gros[i] ==0 and grid.get_petite_case(i,j) == 0]
            t.sort(key=(lambda tup : tup[2]),reverse=True)
            for (i,j,_) in t:
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
            t = [(i,j,val_coup(i,j)) for j in range(9) if grid.get_petite_case(i,j) == 0]
            t.sort(key=(lambda tup : tup[2]),reverse=True)
            for (i,j,_) in t:
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

def montecarlo(grid:Grid,j1:Joueur,case:int,n_iter = 500,c:int=sqrt(2),strategie:callable=jeu_random):
    assert n_iter >= 81, "minimum n_iter = 81 (nombre de cases)"
    joueur = j1.id
    class Arbre:
        def __init__(self,val:Grid,j=j1,cas=case) -> None:
            self.grille:Grid = val
            self.nb_passage = 0
            self.val = 0
            self.fils:list[Arbre] = []
            self.chemin_fils:list[tuple] = [] #coup menant aux fils
            self.case_suivante=cas
            self.joueur=j
        def genere_fils(self) -> None:
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
        def est_feuille(self) -> bool:
            return not bool(self.fils)
        
    racine:Arbre = Arbre(grid)
    racine.genere_fils()
    def choix_fils(self) -> Arbre:
        assert not self.est_feuille()
        m = -inf
        for fils in self.fils:
            if fils.nb_passage == 0:
                return fils
            ucb=(fils.val/fils.nb_passage)+c*sqrt(log(self.nb_passage)/fils.nb_passage)
            if ucb>m :#UCB1
                f=fils
                m=ucb
        return f
    Arbre.choix_fils=choix_fils
    
    current:Arbre = racine

    def rollout(arbre:Arbre) -> int:
        resultat = jeu(strategie,strategie,arbre.grille.copy(),arbre.joueur.id,affichage_gagnant=False,affichage_grille=False)
        if joueur ==-1:
            resultat = -resultat
        return (resultat + 1)//2

    chemin:list[Arbre] = [racine]
    for i in range(n_iter):

        #Selection
        while not current.est_feuille():
            current:Arbre = current.choix_fils()
            chemin.append(current)
        #Expansion
        if current.nb_passage != 0 :
            current.genere_fils() 
            if not current.est_feuille():
                current=current.fils[0]
                chemin.append(current)
        #Simulation
        resultat=rollout(current)
    
        current = racine
        #Backpropagation
        for arbre in chemin:
            arbre.nb_passage+=1
            arbre.val+=resultat
        
        chemin = [racine]
    
    #Choix de la meilleure option
    m=-inf
    i=0
    n=-1
    for a in racine.fils:
        if a.val/a.nb_passage > m :
            m = a.val/a.nb_passage
            arbre = a
            n = i
        i+=1
    return racine.chemin_fils[n]