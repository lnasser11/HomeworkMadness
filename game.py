import pygame
import random

pygame.init()

width = 1200
height = 700

display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Teste")

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False


pygame.quit()
