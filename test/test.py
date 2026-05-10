import pygame
import os

pygame.init()

screen = pygame.display.set_mode((800, 600))

# caminho da imagem
caminho = os.path.join(
    os.path.dirname(__file__),
    "assets",
    "images",
    "cenario.png"
)

imagem = pygame.image.load("D:\\Projetos\\pessoal\\jsn\\src\\assets\\images\\cenario.png").convert()

rodando = True

while rodando:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    # desenha fundo
    screen.blit(imagem, (0, 0))

    pygame.display.update()

pygame.quit()