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
    #Classe para controlar a gameplay do jogo 
    def __init__(self):
        pass

    def update(self):
        #Classe para atualizar o objeto 
        pass

    def draw(self):
        #desenha as partes da tela 
        pass

    def colisao(self):
        #checa as colisoes dos monstros e do jogador 
        pass

    def new_round(self):
        #spawna os monstros 

        pass

    def inimigo(self):
        #escolhe um novo monstro para ser o alvo
        pass

    def pause(self):
        #pausa o jogo
        pass

    def restart(self):
        #reseta o jogo
        pass


class Player(pygame.sprite.Sprite):
    #Classe que o jogador controla
    def __init__(self):
        #inicializa o jogador
        pass

    def update(self):
        #atualiza o jogador
        pass

    def tp(self):
        #teletransporta o jogador para a safe zone
        pass

    def reseta(self):
        #reseta a posição do jogador
        pass

class Inimigo(pygame.sprite.Sprite):
    #classe para criar os inimigos
    def __init__(self):
        #inicializa os monstros
        pass

    def update(self):
        #atualiza o monstro
        pass


#Criação do jogador
player_group = pygame.sprite.Group()
player = Player()
player_group.add(player)

#Criação dos monstros
monster_group = pygame.sprite.Group()

#Game object
game_obj = Game()
#Game loop
game = True

while game:
    for event in pygame.event.get():
        #Se o jogador clicar no X a tela do jogo fecha
        if event.type == pygame.QUIT:
            game = False


    #tela do jogo
    display.fill((0,0,0))

    #Atualização dos sprites
    player_group.update()
    player_group.draw(display)

    monster_group.update()
    monster_group.draw(display)

    game_obj.update()
    game_obj.draw()
    
    #Atualiza a tela do jogo
    pygame.display.update()
    clock.tick(FPS)

#Finaliza o jogo
pygame.quit()
