from sys import set_coroutine_origin_tracking_depth
import pygame
import consts

pygame.init()
screen = pygame.display.set_mode(size=consts.WINDOW_SIZE)

def create_screen():
    screen.fill(color=pygame.color.Color(0,255,0))
    pygame.display.set_caption('The flag game🚩')

    # set text on the top left
    font = pygame.font.Font('Ariel', 10)
    text = font.render('Welcome to the flag game! have fun🚩')