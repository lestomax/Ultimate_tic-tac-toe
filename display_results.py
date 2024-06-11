import pygame
#from main import duels

display = True

WINS=[[45, 43, 2, 0, 0, 0,    0], [67, 100, 0, 0, 65, 31, 13], [97,100,100,0,92,78,69], [99,100,100,100,96,79,72], [98,35,7,3,44,6,4   ], [100,70,24,22,92,55,20], [100,86,29,32,94,78,50]]
EQUALITIES=[[25, 4, 2, 3,2,0, 0], [31, 0, 100, 100, 10, 8, 7], [2, 0, 0, 0, 2, 10, 12], [0, 0, 0, 0, 0,     9,10], [2, 10,3,4,11,6,8   ], [0,5,10,10,4,5,8      ], [0,2,10,6,1,4,10]]
LOSSES=[[30,53,96,97,98,100,100], [2, 0, 0,    0, 25, 61, 80], [1, 0, 0, 100, 6,12,19], [1, 0, 0, 0, 4, 12,   18], [0,55,90,96,45,88,88], [0,25,66,68,4,40,72   ], [0,12,61,62,1,18,40]]

NAMES = ["Random Agent", "1-step Minimax Agent (random)", "3-step Minimax Agent (random)", "5-step Minimax Agent (random)", "MCTS Agent (N=100)", "MCTS Agent (N=500)", "MCTS Agent (N=1000)"]
n = len(WINS)
N = 100

CELL_SIZE = 80
LINE_SIZE = 7
PADDING = 60
LEGEND_SIZE = 700
SIZE = PADDING + n*(CELL_SIZE + LINE_SIZE) + LINE_SIZE
pygame.init()
screen = pygame.display.set_mode((SIZE+LEGEND_SIZE, SIZE))

# Small grid lines
screen.fill((0,20,50))
font = pygame.font.Font(None, 50)
for i in range(n+1):
    pos = PADDING + int(LINE_SIZE*0.5) + i*(CELL_SIZE+LINE_SIZE)
    pygame.draw.line(screen, (255,255,255), (pos,PADDING), (pos,PADDING+n*(CELL_SIZE+LINE_SIZE)+LINE_SIZE), width = LINE_SIZE) # Vertical
    pygame.draw.line(screen, (255,255,255), (PADDING,pos), (PADDING+n*(CELL_SIZE+LINE_SIZE),pos), width = LINE_SIZE) # Horizontal

for i in range(n):
    for j in range(n):
        w = WINS[i][j]
        l = LOSSES[i][j]
        e = EQUALITIES[i][j]

        w = int(round(w*CELL_SIZE/float(N)))
        l = int(round(l*CELL_SIZE/float(N)))
        e = int(round(e*CELL_SIZE/float(N)))

        px = PADDING + int(LINE_SIZE) + j*(CELL_SIZE+LINE_SIZE)
        py = PADDING + int(LINE_SIZE) + i*(CELL_SIZE+LINE_SIZE)

        pygame.draw.rect(screen, (100,200,110), (px, py, w, CELL_SIZE))
        pygame.draw.rect(screen, (150,150,150), (px+w, py, e, CELL_SIZE))
        pygame.draw.rect(screen, (224,80,100), (px+w+e, py, CELL_SIZE-w-e, CELL_SIZE))

        # Text
        score = int(round(100 * (w + 0.5*e) / (w+e+l)))
        text = font.render(str(score), True, (255,255,255))
        text_rect = text.get_rect(center=(px + CELL_SIZE / 2., py + CELL_SIZE/ 2.))
        screen.blit(text, text_rect)

for i in range(n):
    text = font.render("(" + str(1+i) + ")", True, (255,255,255))
    p1 = PADDING / 2.
    p2 = LINE_SIZE + PADDING + (i+0.5) * (CELL_SIZE + LINE_SIZE)
    text_rect = text.get_rect(center=(p1, p2))
    screen.blit(text, text_rect)
    text_rect = text.get_rect(center=(p2, p1))
    screen.blit(text, text_rect)

    text2 = font.render("(" + str(1+i) + ") " + NAMES[i], True, (255,255,255))
    text_rect = text.get_rect(center=(SIZE + 2*p1, p2))
    screen.blit(text2, text_rect)

if __name__ == '__main__':
    game = True
    while game:
        if display:
            # Render the environment

            # Check for pygame event (to close the window)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Quit cross
                    game = False

            # Delay to not spam
            pygame.time.delay(1)
            pygame.display.flip()

    pygame.quit()