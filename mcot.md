# Jeu de Méga-Morpion
Après avoir été séduite par les différents paramètres à prendre en considération lorsque l'on joue au Méga-morpion, contrairement au morpion simple, et bien que les règles soient simples à appréhender, j'ai entrepris d'explorer l'implémentation algorithmique de stratégies optimales. J'ai donc décidé de réaliser cette implémentation en prenant en compte différents paramètres comme la complexité et l'efficacité de mes algorithmes.
Le jeu rentre de par sa nature dans le cadre du thème de cette année, puisqu'il constitue une version améliorée, et intéressante dans le cadre de notre problème du jeu auquel chaque enfant a déjà joué : le morpion. 

## Positionnements thématiques:
INFORMATIQUES (Jeux), INFORMATIQUES (Structures de données : arbres) INFORMATIQUE (Algorithmie), INFORMATIQUES (Optimisation)

### Mots-clés (en français) : 
Méga-morpion
Algorithme Alpha-Bêta
Élagage
Algorithme MinMax
Recherche arborescente Monte-Carlo

### Mots clés (en anglais) : 
Ultimate Tic-Tac-Toe
Minimax algorithm
Alpha-Beta algorithm
Pruning
Monte-Carlo Tree Search (MCTS)

## Bibliographie commentée : 
L'objectif de ce projet est de tester plusieurs algorithmes de résolution de jeu, et examiner leurs performances et leurs résultats, en ajustant les paramètres et dans la limite des capacités de l'ordinateur à disposition. Pour celà il faudrait tout d'abord comprendre le jeu et ses règles. Le jeu se joue sur un grand plateau de morpion, où chaque case est un plateau de morpion traditionnel. La condition de victoire est la même que pour le morpion classique, à savoir aligner trois cases (ici, grandes) du signe du joueur. Pour gagner une grande case, il faut gagner son morpion, avec la même règles d'alignement. Là où le jeu commence à se compliquer c'est par rapport à l'endroit où nous avons le droit de jouer. Le premier joueur à la liberté de choisir la case où il aimerait jouer. Supposons qu; il ait joué dans la petite case i de la grande case j, le joueur qui suit doit jouer dans la grande case i si la case n'est pas bloquée (déjà gagnée ou entièrement remplie), sinon il possède le choix total de la case où il jouera (si l'on enlève les cases bloquées). Pour pouvoir adopter la meilleure stratégie possible, j'ai pu comparer des études déjà réalisées sur le sujet. Une étude [1] comparant notamment l'exécution de l'algorithme MCTS et Alpha Zéro montre que ce dernier est beaucoup plus efficace que MCTS. Malgré la documentation [2] et l'explication du fonctionnement de Alpha Zero, j'ai décidé de ne pas m'y attarder de part sa difficulté, et le rajout d'autres algorithmes en dehors de l'étude. La deuxième étude consultée [3], sur laquelle le projet est largement inspiré, utilise l'algorithme Minmax et MCTS. L'algorithme minmax, et son optimisation avec élagage, l'algorithme Alpha Bêta étant au programme, il n'y a donc pas plus de documentation sur l'explication de l'algorithme. L'algorithme MCTS quant à lui repose sur des simulations aléatoires, et contient plusieurs étapes [4]. Les résultats diffèrent selon la profondeur maximale pour le minmax et le nombre d'itérations utilisées pour le MCTS. Le meilleur résultat s'obtient avec le Minmax de profondeur 5 [3]. Le projet contiendra donc l'implémentation du jeu avec la stratégie aléatoire, la stratégie alpha beta avec plusieurs profondeurs différentes et la stratégie MCTS avec plusieurs itérations différentes. 

## Problématique retenue : 
Quelle est la meilleure stratégie pour gagner un maximum de parties de Méga Morpion?

## Objectifs du TIPE : 
1. Trouver les meilleures stratégies pour gagner aux jeux

2. Optimiser les algorithmes

3. Faire plusieurs simulations entre les différentes stratégies

4. Permettre à un joueur lambda de s'entraîner contre ces algorithmes afin de s'améliorer au jeu

## Références bibliographiques : 
[1] Addison, B., Peeler, M., & Alvin, C. (2022, May). Ultimate Tic-Tac-Toe Bot Techniques. In The International FLAIRS Conference Proceedings (Vol. 35).

[2] Stanford, A Simple Alpha(Go) Zero Tutorial, https://web.stanford.edu/~surag/posts/alphazero.html

[3] Lilian Bichot, Julien Bienvenu, Marie Bienvenu, Astrid Nilsson and Josselin Somerville, Reinforcement Learning Project: Ultimate Tic-Tac-Toe, https://josselinsomervilleroberts.github.io/papers/Report_INF581.pdf

[4] John Levine, Monte Carlo Tree Search, https://www.youtube.com/watch?v=UXW2yZndl7U&t=805s

[5] Josselin Somerville, UltimateTicTacToe RL, https://github.com/JosselinSomervilleRoberts/UltimateTicTacToe-RL
