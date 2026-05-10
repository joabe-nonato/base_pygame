#src\entities\principal
import os

class Game:
    def __init__(self, pg):
        pg.init() 
        self.evento = 0
        self.screen = None
        self.clock = None
        self.running = True
        self.dt = 0
        self.local = None
        self.local_imagens = None
        self.liberado = True
        self.key_click = False
                
    def ciclou(self, pg):        
        for evento in pg.event.get():               
            # O KEYDOWN só acontece UMA VEZ quando você aperta a tecla
            if evento.type == pg.KEYDOWN:
                 if evento.key == pg.K_RETURN or evento.key == pg.K_KP_ENTER:
                    return True        
        return False           
           
    def Escrever(self, pg, texto):
        font = pg.font.Font(None, size=75)
        escreve = font.render(texto, True, (0,0,0,))
        self.screen.blit(escreve, (300,100))

    def apresentacao(self, pg, largura, altura):
        caminho = os.path.join(self.local_imagens,"apres.png")        
        imagem = pg.image.load(caminho).convert()        
        # recorte da imagem
        imagem = pg.transform.scale(imagem, (largura, altura))        
        self.screen.blit(imagem, (0, 0))
        
        self.Escrever(pg, "Apresentação (splash)")
        
        self.key_click = self.ciclou(pg)
        
        if self.key_click:
            self.evento = 1 #princial
            self.key_click = False
        
    def principal(self, pg, largura, altura):
        caminho = os.path.join(self.local_imagens,"intro.png")        
        imagem = pg.image.load(caminho).convert()        
        # recorte da imagem
        imagem = pg.transform.scale(imagem, (largura, altura))        
        self.screen.blit(imagem, (0, 0))
        
        self.Escrever(pg, "Menu principal")        
        
        self.key_click = self.ciclou(pg)
        
        if self.key_click:
            self.evento = 2 #SELEÇÃO
            self.key_click = False
            
        
    def selecao(self, pg, largura, altura):
        caminho = os.path.join(self.local_imagens,"selec.png")        
        imagem = pg.image.load(caminho).convert()        
        # recorte da imagem
        imagem = pg.transform.scale(imagem, (largura, altura))        
        self.screen.blit(imagem, (0, 0))
        
        self.Escrever(pg, "Tela de Seleção")      
        
        self.key_click = self.ciclou(pg)  
        
        if self.key_click:
            self.evento = 99 #exemplo
            self.key_click = False
                
    def exemplo(self, pg, ply, largura, altura):                       
        caminho = os.path.join(self.local_imagens,"exemp.png")        
        imagem = pg.image.load(caminho).convert()        
        # recorte da imagem
        imagem = pg.transform.scale(imagem, (largura, altura))        
        self.screen.blit(imagem, (0, 0))
        
        self.Escrever(pg, "Exemplo")     
        pg.draw.circle(self.screen, ply.cor_fundo, ply.player_pos, 40)
        ply.Entradas(pg, self.dt)