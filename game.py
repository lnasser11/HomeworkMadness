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
bg = pygame.image.load('assets/bg.png')
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

        self.fonte = pygame.font.Font('fonte.ttf', 24)

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
        self.alvo_rect.centerx = WIDTH//2+70
        self.alvo_rect.top = 48


    def update(self):
        self.frame_count += 1
        if self.frame_count == FPS:
            self.round_time += 1
            self.frame_count = 0
        self.colisao()
    def draw(self):
        #desenha as partes da tela 
        WHITE = (255,255,255)
        AZUL = (50, 115, 168)
        ROXO = (129, 50, 168)
        VERDE = (50, 168, 70)
        LARANJA = (201, 126, 34)

        cores = [AZUL,ROXO,VERDE,LARANJA]

        txt_entrega = self.fonte.render('Entrega atual:', True, WHITE)
        entrega_rect = txt_entrega.get_rect()
        entrega_rect.centerx = WIDTH//2 - 50
        entrega_rect.top = 60

        txt_pontos = self.fonte.render('Pontos: ' + str(self.pontos), True, WHITE)
        pontos_rect = txt_pontos.get_rect()
        pontos_rect.topleft = (95,60)

        txt_vidas = self.fonte.render('Vidas: ' + str(self.player.vidas), True, WHITE)
        vidas_rect = txt_vidas.get_rect()
        vidas_rect.topleft = (865,60)

        txt_rounds = self.fonte.render('Round atual: ' + str(self.round), True, WHITE)
        rounds_rect = txt_rounds.get_rect()
        rounds_rect.topleft = (95,95)

        txt_time = self.fonte.render('Tempo: ' + str(self.round_time), True, WHITE)
        time_rect = txt_time.get_rect()
        time_rect.topright = (WIDTH-95, 55)

        txt_warp = self.fonte.render('Sair da sala: ' + str(self.player.warps) + ' usos', True, WHITE)
        warp_rect = txt_warp.get_rect()
        warp_rect.topright = (WIDTH-140, 95)

        #Colocar os textos no jogo
        display.blit(txt_entrega, entrega_rect)
        display.blit(txt_pontos, pontos_rect)
        display.blit(txt_vidas, vidas_rect)
        display.blit(txt_rounds, rounds_rect)
        display.blit(txt_time, time_rect)
        display.blit(txt_warp, warp_rect)
        display.blit(self.alvo, self.alvo_rect)

        pygame.draw.rect(display, cores[self.alvo_escolha], (WIDTH//2+38, 48, 64, 64), 2)

    def colisao(self):
        #checa as colisoes dos monstros e do jogador 
        #colisoes entre o jogador e um professor
        prof_coli = pygame.sprite.spritecollideany(self.player, self.grp_ini)
        if prof_coli:
            if prof_coli.type == self.alvo_escolha:
                self.pontos += 10*self.round
                prof_coli.remove(self.grp_ini) #remove o professor que recebeu a tarefa do grupo
                if (self.grp_ini):
                    self.player.som_entrega.play()
                    self.novo_alvo()
                else:
                    self.player.reset()
                    self.new_round()
            else:
                self.player.som_morte.play()
                self.player.vidas -= 1
                if self.player.vidas <= 0:
                    self.pause("Pontuação: " + str(self.pontos), "Aperte 'ENTER' para jogar novamente!")
                    self.restart()
                self.player.reset()

    def new_round(self):
        #spawna os monstros 
        self.pontos       += int(10000*self.round/(1 + self.round_time))
        self.round_time    = 0
        self.frame_count   = 0
        self.round        += 1
        self.player.warps += 1

        player.vidas = 3
        
        for prof in self.grp_ini:
            self.grp_ini.remove(prof)
        
        for i in range(self.round):
            self.grp_ini.add(Inimigo(random.randint(11, WIDTH - 75), random.randint(155, HEIGHT-394), self.alvos[0], 0))
            self.grp_ini.add(Inimigo(random.randint(11, WIDTH - 75), random.randint(155, HEIGHT-394), self.alvos[1], 1))
            self.grp_ini.add(Inimigo(random.randint(11, WIDTH - 75), random.randint(155, HEIGHT-394), self.alvos[2], 2))
            self.grp_ini.add(Inimigo(random.randint(11, WIDTH - 75), random.randint(155, HEIGHT-394), self.alvos[3], 3))

        self.novo_alvo()
        self.prox_level.play()

    def novo_alvo(self):
        #escolhe um novo monstro para ser o alvo
        alvo_prof = random.choice(self.grp_ini.sprites())
        self.alvo_escolha = alvo_prof.type
        self.alvo = alvo_prof.image

    def pause(self, textao, textinho):
        #pausa o jogo
        global game

        BRANCO = (255,255,255)
        textao = self.fonte.render(textao, True, BRANCO)
        textao_rect = textao.get_rect()
        textao_rect.center = (WIDTH//2, HEIGHT//2)

        textinho = self.fonte.render(textinho, True, BRANCO)
        inho_rect = textinho.get_rect()
        inho_rect.center = (WIDTH//2, HEIGHT//2 + 64)

        display.fill((0,0,0))
        display.blit(textao, textao_rect)
        display.blit(textinho, inho_rect)
        pygame.display.update()

        pausado = True
        while pausado:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pausado = False
                if event.type == pygame.QUIT:
                    pausado = False
                    game = False

    def restart(self):
        #reseta o jogo
        self.pontos = 0
        self.round = 0
        player.vidas = 3
        player.warps = 2
        self.player.reset()

        self.new_round()


class Player(pygame.sprite.Sprite):
    #Classe que o jogador controla
    def __init__(self):
        #inicializa o jogador
        super().__init__()
        self.image = pygame.image.load("assets/mc2.png")
        self.image = pygame.transform.scale(self.image, (35, 55)) # codigo tirado de: https://stackoverflow.com/questions/20002242/how-to-scale-images-to-screen-size-in-pygame
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH//2
        self.rect.bottom = HEIGHT - 23
        
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

        if keys[pygame.K_LEFT] and self.rect.left > 23:
            self.rect.x -= self.velocidade
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH-23:
            self.rect.x += self.velocidade
        if keys[pygame.K_UP] and self.rect.top > 150:
            self.rect.y -= self.velocidade
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT - 185:
            self.rect.y += self.velocidade

    def tp(self):
        #teletransporta o jogador para a safe zone (corredor)
        if self.warps > 0:
            self.warps -= 1
            self.som_warp.play()
            self.rect.bottom = HEIGHT - 23

    def reset(self):
        #reseta a posição do jogador
        self.rect.centerx = WIDTH//2
        self.rect.bottom = HEIGHT - 23
    
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

        if self.rect.left <= 23 or self.rect.right >= WIDTH-23:
            self.dx = self.dx*(-1)
        if self.rect.top <= 150 or self.rect.bottom >= HEIGHT-175:
            self.dy = self.dy*(-1)

#Criação do jogador
player_group = pygame.sprite.Group()
player = Player()
player_group.add(player)

#Criação dos monstros
monster_group = pygame.sprite.Group()

#Game object
game_obj = Game(player, monster_group)
game_obj.pause('Homework Madness', "Aperte 'ENTER' para começar")
game_obj.new_round()

#Game loop
game = True

while game:
    for event in pygame.event.get():
        #Se o jogador clicar no X a tela do jogo fecha
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.tp()


    #tela do jogo
    display.fill((0,0,0))
    pygame.draw.rect(display, (0,0,0), (19, 155, WIDTH-30, HEIGHT-330), 4)
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
