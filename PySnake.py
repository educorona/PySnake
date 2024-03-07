import pygame
from pygame.locals import *
import random
from sys import exit

# Elementos
LARGURA, ALTURA = 600, 400
AREA_ELEMENTO = 50
VELOCIDADE = 3  # FPS
fim_jogo= False
pos_cobra = [[LARGURA/2, ALTURA/2]]
crescer = False
comida = False
flag_movimento = True



class Comida (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load('imagens/rato_1.png'),
                       pygame.image.load('imagens/rato_2.png'),
                       pygame.image.load('imagens/rato_3.png'),
                       pygame.image.load('imagens/rato_4.png'),
                       pygame.image.load('imagens/rato_5.png'),
                       pygame.image.load('imagens/rato_6.png'),
                       pygame.image.load('imagens/rato_7.png'),
                       pygame.image.load('imagens/rato_8.png'),
                       pygame.image.load('imagens/rato_9.png')]

        self.comida_atual = 0

        self.image = pygame.transform.scale(self.images[self.comida_atual],(AREA_ELEMENTO, AREA_ELEMENTO))

        self.rect = self.image.get_rect()

    def update(self, comida):
        self.rect = comida
        self.comida_atual = (self.comida_atual + 1) % 9
        self.image = pygame.transform.scale(self.images[self.comida_atual],(AREA_ELEMENTO, AREA_ELEMENTO))

pygame.init()

comida_group = pygame.sprite.Group()
comida2 = Comida()
comida_group.add(comida2)

BACKGROUND = pygame.image.load('imagens/background2.png')
#BACKGROUND = pygame.transform.scale(BACKGROUND,(LARGURA, ALTURA))

def coloca_comida(area, cobra):

    x = round(random.randrange(0, (LARGURA - AREA_ELEMENTO)) / AREA_ELEMENTO) * AREA_ELEMENTO
    y = round(random.randrange(0, (ALTURA - AREA_ELEMENTO)) / AREA_ELEMENTO) * AREA_ELEMENTO

    while [x, y] in cobra:
        x = round(random.randrange(0, (LARGURA - AREA_ELEMENTO)) / AREA_ELEMENTO) * AREA_ELEMENTO
        y = round(random.randrange(0, (ALTURA - AREA_ELEMENTO)) / AREA_ELEMENTO) * AREA_ELEMENTO

    #pygame.draw.rect(tela, (255,0,0), [x, y, area, area])
    return [x,y],True

def coloca_cobra(cobra, sentido, crescer):
    if crescer:
        cobra.append(cobra[len(cobra)-1])

    for i in range(0,len(cobra)-1):
        cobra[i] = cobra[i+1];

    cobra[len(cobra) - 1] = [i+j for i, j in zip(cobra[len(cobra) - 1], sentido)]

    for pos in cobra:
        pygame.draw.rect(tela, (255, 255, 255), [pos[0], pos[1], AREA_ELEMENTO, AREA_ELEMENTO])
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


    #pygame.draw.rect(tela, (255, 0, 0), [pos_comida[0], pos_comida[1], AREA_ELEMENTO, AREA_ELEMENTO])
    flag_movimento = coloca_cobra(pos_cobra, sentido, crescer)

    crescer, comida = check_comida(pos_cobra, pos_comida)



    fim_jogo = check_fim_game(pos_cobra, fim_jogo)

    #tela

    #comida_group.update()
    if comida:
        comida_group.draw(tela)

    pygame.display.update()

    clock.tick(VELOCIDADE)