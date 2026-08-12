import game_field
import pygame
import consts
def create():
    HEIGHT =0
    WIDTH =0
    soldier_img = pygame.image.load('soldier.png').convert_alpha()
    WIDTH, HEIGHT = soldier_img.get_size()
