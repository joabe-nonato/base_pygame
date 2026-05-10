# src\systems\program\aplicacao
import pygame
from entities.cenario import background
from entities.player_game import player_base
from entities.principal import Game
from systems.settings import FPS, LOCAL_IMAGES, TELA_LARGURA, TELA_ALTURA

def aplicacao(raiz):    
# Example file showing a circle moving on screen
    # pygame setup
    pygame.init()
    game = Game(pygame)
    game.local = raiz
    game.local_imagens =  f"{raiz}{LOCAL_IMAGES}"    
    game.screen = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    game.clock = pygame.time.Clock()   
    
    player01 = player_base(0)
    player01.player_pos = pygame.Vector2(game.screen.get_width() / 2, (game.screen.get_width() / 2) / 2)
    
    # player02 = player_base(1)
    # player02.player_pos = pygame.Vector2((game.screen.get_width() / 2) / 2, (game.screen.get_width() / 2) / 2)

    while game.running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game.running = False
                
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                game.running = False

        # fill the screen with a color to wipe away anything from last frame
        game.screen.fill("purple")
        
        match game.evento:
            case 0:
                game.apresentacao(pygame, TELA_LARGURA, TELA_ALTURA)
            case 1:
                game.principal(pygame, TELA_LARGURA, TELA_ALTURA)
            case 2:
                game.selecao(pygame, TELA_LARGURA, TELA_ALTURA)
                
            case 99:
                game.exemplo(pygame,player01, TELA_LARGURA, TELA_ALTURA)
                # game.exemplo(pygame,player01,pygame,player02, TELA_LARGURA, TELA_ALTURA)
            
        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        game.dt = game.clock.tick(FPS) / 1000

    pygame.quit()
