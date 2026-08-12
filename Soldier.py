import GameField
import pygame
import consts
import Screen


soldier = "soldier.png"
soldier_image = pygame.image.load(soldier)
soldier_image = pygame.transform.scale(soldier_image, (consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT))


def create():
    Screen.screen.blit(soldier_image, (0, 0))