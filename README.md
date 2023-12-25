# Mega-Morpion (Ultimate Tic-Tac-Toe)

## Français
### Introduction

Ce projet constitue mon sujet de TIPE (dont le thème de cette année est "Jeux et sports") dans le cadre de ma CPGE. (2023-2024)

Le sujet que j'ai choisi est donc celui d'essayer de trouver le meilleur jeu possible, et le plus performant pour gagner au Méga-Morpion.
#### Objectif du projet

Tester plusieurs algorithmes de résolution de jeu, et examiner leurs performances et leurs résultats, en ajustant les paramètres et dans la limite des capacités de mon ordinateur.
### Règles du jeu

![https://github.com/JosselinSomervilleRoberts/JosselinSomervilleRoberts.github.io/blob/main/images/projects/ultimate_tic_tac_toe/ultimate%20tic%20tac%20toe.png](image.png)

#### Interface
Nous avons une grille de morpion, où chaque case est un morpion.

#### Objectif
Gagner le Grand morpion (règles du morpion classique pour gagner).

#### Comment obtenir une grande case ?
Il faut gagner le morpion de cette grande case.

#### Où avons nous le droit de jouer à notre tour ?
* Premier joueur : joue là où il veut.

* Ensuite, selon le tour d'avant : 

    L'adversaire a joué dans la grande case **i**, dans sa petite case **j**
    * Si la grande case j a déjà été gagnée ou qu'elle est entièrement remplie, jouer n'importe où sur toute la grille
    * sinon, le joueur choisit de jouer nimporte où dans la grande case **j**

### Algorithmes

* MinMax 
* AlphaBeta
* Recherche arborescante Monte-Carlo (MCTS) (pas sûre)
