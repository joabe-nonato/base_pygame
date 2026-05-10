# src\entities\player_game\player_base
from entities.base import basic

class player_base(basic):
    def __init__(self, idp):
        super().__init__()
        self.id = idp
        self.eventos = None
        self.cor_fundo = None
        self.pulo = None        
        self.player_pos = None
        self.tecla_start = None
        self.tecla_esquerda = None
        self.tecla_cima = None
        self.tecla_direita = None
        self.tecla_baixo = None
        self.tecla_soco = None
        self.tecla_chute = None
        self.tecla_magia = None

        if idp == 0:
            self.cor_fundo = "red"
        else:
            self.cor_fundo = "blue"
                
    def Entradas(self, pg, dt):
        if  self.id == 0:
            self.tecla_start = pg.K_0
            self.tecla_esquerda = pg.K_a
            self.tecla_cima = pg.K_w
            self.tecla_direita = pg.K_d
            self.tecla_baixo = pg.K_s
            self.tecla_soco = pg.K_p
            self.tecla_chute = pg.K_k
        else:
            self.tecla_start = pg.K_1
            self.tecla_esquerda = pg.K_LEFT
            self.tecla_cima = pg.K_UP
            self.tecla_direita = pg.K_RIGHT
            self.tecla_baixo = pg.K_DOWN
            self.tecla_soco = pg.K_m
            self.tecla_chute = pg.K_n
    
        keys = pg.key.get_pressed()
        if keys[self.tecla_cima]:
            self.player_pos.y -= 300 * dt
        if keys[self.tecla_baixo]:
            self.player_pos.y += 300 * dt
        if keys[self.tecla_esquerda]:
            self.player_pos.x -= 300 * dt
        if keys[self.tecla_direita]:
            self.player_pos.x += 300 * dt