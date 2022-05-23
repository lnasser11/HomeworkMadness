import pygame
import random

pygame.init()

#Dimensões da janela
WIDTH = 1200
HEIGHT = 700

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
        super().__init__()
        self.image = pygame.image.load("placeholders/deco_ph.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH//2
        self.rect.bottom = HEIGHT//2
        
        self.vidas = 3
        self.warps = 2
        self.velocidade = 8

        self.som_entrega = pygame.mixer.Sound('placeholders/entrega_ph.wav')
        self.som_morte = pygame.mixer.Sound('placeholders/morte_ph.wav')
        self.som_warp = pygame.mixer.Sound('placeholders/warp_ph.wav')
        self.som_sem_warp = pygame.mixer.Sound('placeholders/sem_warp_ph.wav')

    def update(self):
        #atualiza o jogador
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocidade
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.velocidade
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.velocidade
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.velocity

    def tp(self):
        #teletransporta o jogador para a safe zone (corredor)
        if self.warps > 0:
            self.warps -= 1
            self.som_warp.play()
            self.rect.bottom = HEIGHT

    def reseta(self):
        #reseta a posição do jogador
        self.rect.centerx = WIDTH//2
        self.rect.bottom = HEIGHT
    
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
