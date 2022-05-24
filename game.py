import pygame
import random

pygame.init()

#Dimensões da janela
WIDTH = 1200
HEIGHT = 700

#Criação da janela
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Homework Madness")

#fundo do jogo
bg = pygame.image.load('deco_bg.jpg')
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
#FPS e Velocidade do jogo
FPS = 60
clock = pygame.time.Clock() 

#Classes

class Game():
    #Classe para controlar a gameplay do jogo 
    def __init__(self, player, grupo_inimigo):
        self.pontos = 0
        self.round = 0

        self.round_time = 0
        self.frame_count = 0

        self.player = player
        self.grp_ini = grupo_inimigo
        
        self.prox_level = pygame.mixer.Sound('testesom.wav')

        self.fonte = pygame.font.Font('Arial', 24)

        #professores
        areia = pygame.image.load('areia.jpg')
        areia = pygame.transform.scale(areia, (64,64))
        builder = pygame.image.load('builder.jpg')
        builder = pygame.transform.scale(builder, (64,64))
        ffjr = pygame.image.load('ffjr.jpg')
        ffjr = pygame.transform.scale(ffjr, (64,64))
        mural = pygame.image.load('mural.jpg')
        mural = pygame.transform.scale(mural, (64,64))

        #Prof que precisa entregar a lição de casa
        self.alvos = [areia, builder, ffjr, mural]

        self.alvo_escolha = random.randint(0,3)
        self.alvo = self.alvos[self.alvo_escolha]

        self.alvo_rect = self.alvo.get_rect()
        self.alvo_rect.centerx = WIDTH//2
        self.alvo_rect.top = 30


    def update(self):
        self.round_time += 1
        
        self.colisao()
    def draw(self):
        #desenha as partes da tela 
        WHITE = (255,255,255)
        BLUE = (20,176,235)
        PURPLE = (226,73,243)
        GREEN = (87,201,47)
        YELLOW = (243,157,20)

        cores = [BLUE,PURPLE,GREEN,YELLOW]

        txt_entrega = self.font.render('Entrega atual:', True, WHITE)
        entrega_rect = txt_entrega.get_rect()
        entrega_rect.centerx = WIDTH//2
        entrega_rect.top = 5

        txt_pontos = self.font.render('Pontos: ' + str(self.pontos), True, WHITE)
        pontos_rect = txt_pontos.get_rect()
        pontos_rect.topleft = (5,5)

        txt_vidas = self.font.render('Vidas: ' + str(self.player.lives), True, WHITE)
        vidas_rect = txt_vidas.get_rect()
        vidas_rect.topleft = (5,35)

        txt_rounds = self.font.render('Round atual: ' + str(self.round), True, WHITE)
        rounds_rect = txt_rounds.get_rect()
        rounds_rect.topleft = (5,65)
        
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
        self.image = pygame.image.load("deco_ph.png")
        self.image = pygame.transform.scale(self.image, (64, 64)) # codigo tirado de: https://stackoverflow.com/questions/20002242/how-to-scale-images-to-screen-size-in-pygame
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH//2
        self.rect.bottom = HEIGHT//2
        
        self.vidas = 3
        self.warps = 2
        self.velocidade = 8

        self.som_entrega = pygame.mixer.Sound('testesom.wav')
        self.som_morte = pygame.mixer.Sound('testesom.wav')
        self.som_warp = pygame.mixer.Sound('testesom.wav')
        self.som_sem_warp = pygame.mixer.Sound('testesom.wav')

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
            self.rect.y += self.velocidade

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
    def __init__(self, x, y, image, professor):
        #inicializa os monstros
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
        # Professor --> decide o tipo do professor que vai spawnar atraves da lista de profs 
        self.type = professor

        # Caminho aleatorio dos professores
        self.dx = random.choice([-1,1])
        self.dy = random.choice([-1,1]) # -1 vai para a esquerda e 1 para a direita
        self.velocidade = random.randint(1,5)

    def update(self):
        #atualiza o monstro
        self.rect.x += self.dx*self.velocidade
        self.rect.y += self.dy*self.velocidade

        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.dx = self.dx*(-1)
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy = self.dy*(-1)

#Criação do jogador
player_group = pygame.sprite.Group()
player = Player()
player_group.add(player)

#Criação dos monstros
monster_group = pygame.sprite.Group()
#testes
m1 = pygame.image.load('monstro4_ph.png')
m1 = pygame.transform.scale(m1, (64, 64))
monstro = Inimigo(500, 500, m1, 1)
monster_group.add(monstro)
m2 = pygame.image.load('monstro2_ph.png')
m2 = pygame.transform.scale(m2, (64, 64))
monstro = Inimigo(100, 500, m2, 0)
monster_group.add(monstro)

#Game object
game_obj = Game(player, monster_group)
#Game loop
game = True

while game:
    for event in pygame.event.get():
        #Se o jogador clicar no X a tela do jogo fecha
        if event.type == pygame.QUIT:
            game = False


    #tela do jogo
    display.fill((0,0,0))
    display.blit(bg, (0,0))

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
