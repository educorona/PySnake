import pygame
from Modelos.configuracoes import Config
from pygame.locals import *
class Comida (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self._AREA_ELEMENTO = Config()._AREA_ELEMENTO

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
        self.image = pygame.transform.scale(self.images[self.comida_atual],(self._AREA_ELEMENTO, self._AREA_ELEMENTO))
        self.rect = self.image.get_rect()

    def update(self, comida_pos):
        self.rect = comida_pos
        self.comida_atual = (self.comida_atual + 1) % 9
        self.image = pygame.transform.scale(self.images[self.comida_atual],(self._AREA_ELEMENTO, self._AREA_ELEMENTO))

class Cobra (pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.AREA_ELEMENTO = Config()._AREA_ELEMENTO
        self.images = pygame.image.load('imagens/cobra_cabeca.png')
        self.image = pygame.transform.scale(self.images, (self.AREA_ELEMENTO, self.AREA_ELEMENTO))
        self.rect = self.image.get_rect()

    def update(self, cobra_pos, grupo, tel):
        for pos in cobra_pos:
            self.rect = pos
            self.image = pygame.transform.scale(self.image, (self.AREA_ELEMENTO, self.AREA_ELEMENTO))
            grupo.draw(tel)