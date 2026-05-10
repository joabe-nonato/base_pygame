import os
from systems.settings import FPS, LOCAL_IMAGES, TELA_LARGURA, TELA_ALTURA, DEBUG

def modo_debug(self, pg):
    # if DEBUG:
    #     draw rect
    pass

def escrever(screen, pg, texto, s, y, x):
    font = pg.font.Font(None, size=s)
    escreve = font.render(texto, True, (0,0,0,))
    screen.blit(escreve, (y,x))
    
def desenhar_simples(self, pg, imagem, y, x, w, h):        
    imagem = pg.image.load(os.path.join(self.local_imagens, imagem)).convert()                
    imagem = pg.transform.scale(imagem, (w, h))        
    self.screen.blit(imagem, (y, x))
    
def desenhar_recorte(self, pg, imagem, oY, oX, oW, oH, d_Y, d_X, d_W, d_H):        
    imagem = pg.image.load(os.path.join(self.local_imagens, imagem)).convert()                
    imagem = pg.transform.scale(imagem, (oW, oH))        
    self.screen.blit(imagem, (oY, oX))
    modo_debug()