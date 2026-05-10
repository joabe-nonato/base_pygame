#src\entities\principal
from systems.helpers import escrever, desenhar_simples

class Game:
    def __init__(self, pg):
        pg.init() 
        self.evento_atual = 0
        self.screen = None
        self.clock = None
        self.running = True
        self.dt = 0
        self.local = None
        self.local_imagens = None
        self.liberado = True
        self.key_click = False
        self.player01 = None
        self.entrada_eventos = None
                
    def proximo_evento(self, pg, proximo):                
        for evento in self.entrada_eventos:
            # O KEYDOWN só acontece UMA VEZ quando você aperta a tecla
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_RETURN or evento.key == pg.K_KP_ENTER:
                    self.evento_atual = proximo  
                    break  
           
    def apresentacao(self, pg, largura, altura):                
        desenhar_simples(self, pg, "apres.png", 0, 0, largura, altura)        
        escrever(self.screen, pg, "Apresentação (splash)", 75, 300, 100)        
        self.proximo_evento(pg, 1)        
        
    def principal(self, pg, largura, altura):
        desenhar_simples(self, pg, "intro.png", 0, 0, largura, altura)
        escrever(self.screen, pg, "Menu principal", 75, 300, 100)        
        self.proximo_evento(pg, 2)                    
        
    def selecao(self, pg, largura, altura):
        desenhar_simples(self, pg, "selec.png", 0, 0, largura, altura)          
        escrever(self.screen, pg, "Tela de Seleção", 75, 300, 100)      
        self.proximo_evento(pg, 3)        
                
    def exemplo(self, pg, largura, altura):  
        desenhar_simples(self, pg, "exemp.png", 0, 0, largura, altura)        
        escrever(self.screen, pg, "Teclas (A , W , S , D) ", 75, 300, 100)    
        self.player01.entrada_eventos = self.entrada_eventos
        if self.player01.player_pos == None:
            # self.player01.player_pos = pg.Vector2(self.screen.get_width() / 2, (self.screen.get_width() / 2) / 2)         
            self.player01.player_pos = pg.Vector2(100, 100)         
        self.player01.Entradas(pg, self.dt)
        
        player = pg.Rect(self.player01.player_pos.x, self.player01.player_pos.y, 50, 50)
        bloco = pg.Rect(400, 250, 120, 120)
        pg.draw.rect(self.screen, (0, 0, 255), bloco)
                
        colidiu = player.colliderect(bloco)
        if colidiu:
            pg.draw.rect(self.screen, (0, 255, 0), bloco)
            self.player01.player_pos = pg.Vector2(100, 100)         
            # self.player01.player_pos = pg.Vector2(self.screen.get_width() / 2, (self.screen.get_width() / 2) / 2)         
        
        pg.draw.rect(self.screen, (self.player01.cor_fundo), player)
        
        
        
        
        