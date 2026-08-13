import pygame
import consts
import Screen

soldier = consts.SOLIDER_IMG
soldier_image = pygame.image.load(soldier)
soldier_image = pygame.transform.scale(soldier_image, (consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT))

origin_x, origin_y = 0, 0

width = soldier_image.get_width()
height = soldier_image.get_height() # the image's total height is 512; https://www.photopea.com/
slice_height = 110
soldier_image = pygame.transform.scale(soldier_image, (consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT))

def split_soldier(soldier_image):
    legs_rect = pygame.Rect(0, 0, width, 110)
    legs = soldier_image.subsurface(legs_rect)

    body_rect = pygame.Rect(0, 110, width, 512 - 110)
    body = soldier_image.subsurface(body_rect)
def create():
    # Screen.screen.blit(soldier_image, (0, 0))

    soldier_rect = soldier_image.get_rect()
    soldier_rect.midbottom = (0, 110)
    Screen.screen.blit(soldier_image, soldier_rect)
