from random import randint

class Grid:
    def __init__(self): #O(1)
        self.entiere=[[0 for i in range(9)]for j in range(9)]
        self.gros = [0 for i in range(9)]
        self.evaluation = 0 #heuristique
        self.fini = False #état final / terminal

    def copy(self): #O(1)
        #nous permettra de simuler un jeu sans perdre l'ancienne grille
        g = Grid()
        for i in range(9):
            for j in range(9):
                g.entiere[i][j] = self.entiere[i][j]
            g.gros[i] = self.gros[i]
        g.evaluation = self.evaluation
        g.fini = self.fini
        return g
    
    def get_case(self,case:int, tab:list[int]): #O(1)
        assert 0 <= case <= 8, "pas une case"
        return tab[case]
    
    def get_petite_case(self,grande_case:int,petite_case:int): #O(1)
        assert 0<=grande_case<=8 and 0<=petite_case<=8, "pas une case"
        return self.entiere[grande_case][petite_case]
    
    def ligne_gagnante(self, case:int, tab:list[int]): #O(1)
        joueur:int = self.get_case(case, tab)
        for i in range((case//3)*3,(case//3)*3+3):
            if joueur != tab[i]:
                return False
        return True
    
    def col_gagnante(self, case:int, tab:list[int]): #O(1)
        joueur:int = self.get_case(case, tab)
        for i in range(case%3,case%3+7,3):
            if joueur != tab[i]:
                return False
        return True
    
    def diag_gagnante(self, case:int, tab:list[int]): #O(1)
        assert case%2 == 0 , "pas dans une diagonale"
        joueur:int = self.get_case(case, tab)
        drap = True
        for i in [0,4,8]:
            if tab[i] != joueur:
                drap = False
        if drap :
            return True
        for i in [2,4,6]:
            if tab[i] != joueur:
                drap = True
        return not drap
    
    def gagnant(self,case:int,tab:list[int]): #O(1)
        """Vérifie si la case est gagnée sachant que l'on vient de jouer dans case"""
        return self.ligne_gagnante(case,tab) or self.col_gagnante(case,tab) or (case%2==0 and self.diag_gagnante(case,tab))

    def rempli(self,tab:list[int]): #O(1)
        """Vérifie si la case est entièrement remplie dans le tableau"""
        for i in tab:
            if i == 0 :
                return False
        return True

    def set(self,grande_case:int,petite_case:int,joueur): #O(1)
        """Fait 1 action : un joueur joue son tour"""
        assert self.get_case(grande_case,self.gros)==0, "case déjà finie"
        assert self.get_petite_case(grande_case,petite_case)==0, "case déjà remplie"
        j = joueur.id
        assert j in [-1,1], "ce n'est pas un joueur"
        assert not self.fini
        self.entiere[grande_case][petite_case]=j
        if self.gagnant(petite_case,self.entiere[grande_case]): #si on gagne une petite grille
            self.gros[grande_case] = j
            self.evaluation+= j*10
            if self.gagnant(grande_case,self.gros) : #on gagne
                self.fini = True
                self.evaluation = j*100
            elif self.rempli(self.gros): #egalité
                self.fini = True
                self.evaluation = 0
        else:
            if self.rempli(self.entiere[grande_case]) : #la petite grille est remplie sans être gagnée
                self.gros[grande_case]=2
                if self.rempli(self.gros):#egalité
                    self.fini = True
                    self.evaluation = 0

    def affiche_entiere(self): #O(1)
        """Affiche grille méga morpion"""
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        n = self.entiere[i*3+k][j*3+l]
                        if n ==-1:
                            print("O", end=" ")
                        elif n == 1:
                            print("X",end=" ")
                        else:
                            print("_",end=" ")
                    print("|",end=" ")
                print()
            print("-----------------------")
        print()

    def affiche_tic_tac_toe(self,tab:list[int]): #O(1)
        """Affiche grille morpion"""
        for i in range(3):
            for j in range(3):
                if tab[i*3+j] ==-1:
                    print("O", end=" ")
                elif tab[i*3+j] == 1:
                    print("X",end=" ")
                elif tab[i*3+j] == 0:
                    print("_",end=" ")
                else:
                    print("|",end=" ")
            print()
        print()

class Joueur:
    def __init__(self,fun:callable,id:int):
        assert id in [-1,1]
        self.fun = fun #prend une grille,un joueur et une petite grille(pg) (où l'on doit jouer), et renvoie la pg où on joue et la petite case
        self.id = id
    
    def joue(self,grid:Grid,case:int):
        g,p=self.fun(grid,self,case)
        grid.set(g,p,self)
        if grid.gros[p]== 0:
            return p
        return -1

def jeu(ja:callable,jb:callable,grid=0,ordre=1,affichage_grille=True,affichage_gagnant=True):
    if grid == 0 :
        grid = Grid()
    j1=Joueur(ja,1*ordre)
    j2=Joueur(jb,-1*ordre)
    case = -1
    while not grid.fini :
        case = j1.joue(grid,case)
        if affichage_grille:
            grid.affiche_entiere()
            grid.affiche_tic_tac_toe(grid.gros)
        if not grid.fini:
            case = j2.joue(grid,case)
            if affichage_grille:
                grid.affiche_entiere()
                grid.affiche_tic_tac_toe(grid.gros)
    assert grid.evaluation % 100 == 0, "La partie n'est pas finie"
    if affichage_gagnant:
        print("Gagnant :",grid.evaluation//100)
    return grid.evaluation//100


