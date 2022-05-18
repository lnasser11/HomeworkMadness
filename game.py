import pygame
import random

pygame.init()

#Dimensões da janela
width = 1200
height = 700

#Criação da janela
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Teste")

#FPS e Velocidade do jogo
FPS = 60
clock = pygame.time.Clock() 

#Classes

class Game():
    '''Classe para controlar a gameplay do jogo'''
    def __init__(self):
        pass

    def update(self):
        '''Classe para atualizar o objeto'''
        pass


#Game loop
game = True

while game:
    for event in pygame.event.get():
        #Se o jogador clicar no X a tela do jogo fecha
        if event.type == pygame.QUIT:
            game = False

    #Atualiza a tela do jogo
    pygame.display.update()
    clock.tick(FPS)

#Finaliza o jogo
pygame.quit()
