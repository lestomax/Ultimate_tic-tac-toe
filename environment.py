from random import randint

class Grid:
    def __init__(self):
        self.entiere=[[0 for i in range(9)]for j in range(9)]
        self.gros = [0 for i in range(9)]
        self.evaluation = 0
        self.fini = False

    def copy(self):
        g = Grid()
        for i in range(9):
            for j in range(9):
                g.entiere[i][j] = self.entiere[i][j]
            g.gros[i] = self.gros[i]
        g.evaluation = self.evaluation
        g.fini = self.fini
        return g
    
    def get_case(self,case:int, tab:list[int]):
        assert 0 <= case <= 8, "pas une case"
        return tab[case]
    
    def get_petite_case(self,grande_case:int,petite_case:int):
        assert 0<=grande_case<=8 and 0<=petite_case<=8, "pas une case"
        return self.entiere[grande_case][petite_case]
    
    def ligne_gagnante(self, case:int, tab:list[int]):
        joueur:int = self.get_case(case, tab)
        for i in range((case//3)*3,(case//3)*3+3):
            if joueur != tab[i]:
                return False
        return True
    
    def col_gagnante(self, case:int, tab:list[int]):
        joueur:int = self.get_case(case, tab)
        for i in range(case%3,case%3+7,3):
            if joueur != tab[i]:
                return False
        return True
    
    def diag_gagnante(self, case:int, tab:list[int]):
        assert case%2 == 0 , "pas dans la diagonale"
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
    
    def gagnant(self,case:int,tab:list[int]):
        return self.ligne_gagnante(case,tab) or self.col_gagnante(case,tab) or (case%2==0 and self.diag_gagnante(case,tab))

    def rempli(self,tab:list[int]):
        for i in tab:
            if i == 0 :
                return False
        return True
    
    def set(self,grande_case:int,petite_case:int,joueur):
        assert self.get_case(grande_case,self.gros)==0, "case déjà finie"
        assert self.get_petite_case(grande_case,petite_case)==0, "case déjà remplie"
        j = joueur.id
        assert j in [-1,1], "ce n'est pas un joueur"
        assert not self.fini
        self.entiere[grande_case][petite_case]=j
        if self.gagnant(petite_case,self.entiere[grande_case]):
            self.gros[grande_case] = j
            self.evaluation+= j*10
            if self.gagnant(grande_case,self.gros) :
                self.fini = True
                self.evaluation = j*100
            elif self.rempli(self.gros):
                self.fini = True
                self.evaluation = 0
        else:
            if self.rempli(self.entiere[grande_case]) :
                self.gros[grande_case]=2
                if self.rempli(self.gros):
                    self.fini = True
                    self.evaluation = 0

    def affiche_entiere(self):
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

    def affiche_tic_tac_toe(self,tab:list[int]):
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
        self.fun = fun
        self.id = id
    
    def joue(self,grid:Grid,case:int):
        g,p=self.fun(grid,self,case)
        grid.set(g,p,self)
        if grid.gros[p]== 0:
            return p
        return -1

def jeu(j1:callable,j2:callable):
    j1=Joueur(j1,1)
    j2=Joueur(j2,-1)
    grid = Grid()
    case = -1
    while not grid.fini :
        case = j1.joue(grid,case)
        grid.affiche_entiere()
        grid.affiche_tic_tac_toe(grid.gros)
        if not grid.fini:
            case = j2.joue(grid,case)
            grid.affiche_entiere()
            grid.affiche_tic_tac_toe(grid.gros)
    assert grid.evaluation % 100 == 0, "La partie n'est pas finie"
    print("Gagnant :",grid.evaluation//100)


