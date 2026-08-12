from sys import set_coroutine_origin_tracking_depth
import pygame
import consts

pygame.init()
screen = pygame.display.set_mode(size=consts.SCREEN_SIZE)

def create_screen():
    screen.fill(color=pygame.color.Color(4,95,11))
    pygame.display.set_caption('The flag game')

    update_text()


def update_text(disappear=False):
    # set text on the top left
    font = pygame.font.SysFont(None, 20)
    text = font.render('Welcome to the flag game! have fun', True, (255,122,149))
    text_rect = text.get_rect()
    text_rect.topleft = (0,0)
    screen.blit(text, text_rect)

    if disappear:
        screen.fill(color=pygame.color.Color(4, 95, 11))


def update_screen_net():
    screen.fill(color=pygame.color.Color(0,0,0))

