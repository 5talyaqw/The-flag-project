import GameField
import pygame
import consts

soldier = "soldier.png"
soldier_image = pygame.image.load(soldier)
soldier_image = pygame.transform.scale(soldier_image, (consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT))

def create():
    HEIGHT =0
    WIDTH =0
    WIDTH, HEIGHT = soldier_image.get_size()
