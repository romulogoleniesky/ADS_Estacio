## Criando um jogo com a biblioteca Pygame.


## Importando a biblioteca Pygame.
## Importanto a biblioteca Random.
import pygame, random

from pygame.locals import*

## Correção do alinhamento dos pixels.
def on_grid_random():
    x = random.randint(0,49)
    y = random.randint(0,49)
    return (x * 10, y * 10)

## Colisão da cobra com a maçã:
def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

## Movimentos:
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

## Iniciando o Pygame:
pygame.init()

## Configuração da tela.
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Snake")

## Tempo de mudança:
clock = pygame.time.Clock()

## Criando a Snake:
Snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255)) ##branco

my_direction = LEFT
font = pygame.font.Font("freesansbold.ttf",18)
score = 0

## Criando a Maçã.
apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255, 0, 0)) ##Vermelho

## Laço infinito:
game_over = False
while not game_over:

    ## Velocidade de troca de frame:(Quanto maior o valor, mais rápido fica).
    clock.tick(10)

    ## Evento de fechar.
    for event in pygame.event.get():
        if event.type == quit:
            pygame.quit()
            exit()

        ## Comandos de Movimento:
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT

    if collision(Snake[0], apple_pos):
        apple_pos = on_grid_random()
        Snake.append((0,0))
        score = score +1

    ##Colisões com a parede:
    if Snake[0][0] == 500 or Snake[0][1] == 500 or Snake[0][0] < 0 or Snake[0][1] <0:
        game_over = True
        break

    ## Colisão com o corpo:
    for i in range(1, len(Snake) - 1):
        if Snake[0][0] == Snake[i][0] and Snake[0][1] == Snake[i][1]:
            game_over = True
            break

    if game_over:
        break




    for i in range(len(Snake) -1, 0, -1):
        Snake[i] = (Snake[i-1][0], Snake[i-1][1])

    if my_direction == UP:
        Snake[0] = (Snake[0][0], Snake[0][1] - 10)
    if my_direction == DOWN:
        Snake[0] = (Snake[0][0], Snake[0][1] + 10)
    if my_direction == RIGHT:
        Snake[0] = (Snake[0][0] + 10, Snake[0][1])
    if my_direction == LEFT:
        Snake[0] = (Snake[0][0] - 10, Snake[0][1])




    screen.fill((0,0,0))
    screen.blit(apple,apple_pos)

    ##Colocando grade no fundo da tela.
    for x in range(0, 500, 10):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 500))
    for y in range(0, 500, 10):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (500, y))

    ## Tela do Score:
    score_font = font.render('Score:%s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (500-120, 10)
    screen.blit(score_font, score_rect)

    for pos in Snake:
        screen.blit(snake_skin,pos)

    pygame.display.update()


while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Gamer Over', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (500/2, 10)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == quit():
                pygame.quit()
                exit()


