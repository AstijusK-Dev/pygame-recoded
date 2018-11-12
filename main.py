import pygame
from pygame.locals import *

pygame.init()

display_width = 1920
display_height = 1080
display_default_fullscreen = True

if display_default_fullscreen == True:
    display = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)

pygame.display.set_caption("Game")
clock = pygame.time.Clock()


class Player:
    def __init__(self, xp, yp, w, h, vel):
        self.xp = xp
        self.yp = yp
        self.w = w
        self.h = h
        self.vel = vel

player_one = Player(0, 0, 32, 32, 3.5)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Managing keyboard input for players
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: player_one.yp -= player_one.vel
    if keys[pygame.K_s]: player_one.yp += player_one.vel
    if keys[pygame.K_a]: player_one.xp -= player_one.vel
    if keys[pygame.K_d]: player_one.xp += player_one.vel

    if keys[pygame.K_ESCAPE]: pygame.display.set_mode((display_width, display_height))
    if keys[pygame.K_f]: pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)

    #Drawing the player, redrawing background to make illusion of movement
    display.fill((0, 0, 0))
    pygame.draw.rect(display, (255, 0, 0), Rect(player_one.xp, player_one.yp, player_one.w, player_one.h))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
