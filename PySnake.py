import pygame
from pygame.locals import *
import random
from sys import exit
import Modelos.modelos as modelos
import Modelos.configuracoes as config


# Elementos
LARGURA, ALTURA = config.Config()._LARGURA, config.Config()._ALTURA
AREA_ELEMENTO = config.Config()._AREA_ELEMENTO
VELOCIDADE = config.Config().VELOCIDADE
fim_jogo= False
pos_cobra = config.Config()._pos_inicial_cobra
crescer = False     # indica se é para crescer ou não
comida = False  # existencia da comida
flag_movimento = True   # Flag que trava impede segundo movimento antes do clock

pygame.init()

comida_group = pygame.sprite.Group()
comida_group.add(modelos.Comida())

cobra_group = pygame.sprite.Group()
cobra_group.add(modelos.Cobra())

BACKGROUND = pygame.image.load('imagens/background2.png')

def coloca_comida(area, cobra):

    x = round(random.randrange(0, (LARGURA - AREA_ELEMENTO)) / AREA_ELEMENTO) * AREA_ELEMENTO
    y = round(random.randrange(0, (ALTURA - AREA_ELEMENTO)) / AREA_ELEMENTO) * AREA_ELEMENTO

    while [x, y] in cobra:
        x = round(random.randrange(0, (LARGURA - AREA_ELEMENTO)) / AREA_ELEMENTO) * AREA_ELEMENTO
        y = round(random.randrange(0, (ALTURA - AREA_ELEMENTO)) / AREA_ELEMENTO) * AREA_ELEMENTO

    return [x,y],True

def coloca_cobra(cobra, sentido, crescer):
    if crescer:
        cobra.append(cobra[len(cobra)-1])

    for i in range(0,len(cobra)-1):
        cobra[i] = cobra[i+1];

    cobra[len(cobra) - 1] = [i+j for i, j in zip(cobra[len(cobra) - 1], sentido)]
    cobra_group.update(cobra, cobra_group, tela)

    return True

def check_fim_game(cobra, fim_jogo):
    # Colisão nas paredes
    if ((pos_cobra[len(pos_cobra) - 1][0] >= LARGURA) or
            (pos_cobra[len(pos_cobra) - 1][1] >= ALTURA) or
            (pos_cobra[len(pos_cobra) - 1][0] < 0) or
            (pos_cobra[len(pos_cobra) - 1][1] < 0)):
        return True
    elif len(cobra)>2:
        # Colisão na própria cobra
        if (cobra[len(cobra)-1] in cobra[0:len(cobra)-1]):
            return True
    else: return fim_jogo

def check_comida(cobra, pos_comida):
    if cobra[len(cobra)-1] == pos_comida:
        return True, False
    else:
        return False, True

# Atribuir Nome da janela
pygame.display.set_caption("")

# Atribuir dimenções da janela
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Atribuir Nome da janela
pygame.display.set_caption("PySnake")

# Gerar o clock do jogo
clock = pygame.time.Clock()

#colocando a cobra
sentido = [0, 0]

while not fim_jogo:
    tela.blit(BACKGROUND,(0,0))
    for evento in pygame.event.get():
        # Clicou para sair
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        if flag_movimento:
            if evento.type == KEYDOWN:
                flag_movimento = False
                if evento.key == K_LEFT:
                    if sentido != [AREA_ELEMENTO, 0]:
                        sentido = [-AREA_ELEMENTO, 0]
                elif evento.key == K_DOWN:
                    if sentido != [0, -AREA_ELEMENTO]:
                        sentido = [0, AREA_ELEMENTO]
                elif evento.key == K_RIGHT:
                    if sentido != [-AREA_ELEMENTO, 0]:
                        sentido = [AREA_ELEMENTO, 0]
                elif evento.key == K_UP:
                    if sentido != [0, AREA_ELEMENTO]:
                        sentido = [0, -AREA_ELEMENTO]

    if not comida:
        pos_comida, comida = coloca_comida(AREA_ELEMENTO, pos_cobra)
        comida_group.update(pos_comida)

    flag_movimento = coloca_cobra(pos_cobra, sentido, crescer)
    crescer, comida = check_comida(pos_cobra, pos_comida)
    fim_jogo = check_fim_game(pos_cobra, fim_jogo)

    if comida:
        comida_group.draw(tela)

    pygame.display.update()
    clock.tick(VELOCIDADE)

