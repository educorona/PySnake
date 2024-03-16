#tamanho da janela
class Config:
    def __init__(self):
        self._LARGURA, self._ALTURA = 600, 400
        self._AREA_ELEMENTO = 50
        self.VELOCIDADE = 3  # FPS
        self._pos_inicial_cobra = [[self._LARGURA/2, self._ALTURA/2]]
