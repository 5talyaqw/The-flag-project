import GameField
import pygame
import consts
import Screen

soldier = consts.SOLIDER_IMG
soldier_image = pygame.image.load(soldier)
soldier_image = pygame.transform.scale(soldier_image, (consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT))
soldier_pos = [0,0]


def create():
    Screen.screen.blit(soldier_image, soldier_pos)


def move_soldier(event):
    if event == pygame.K_DOWN:
        if soldier_pos[1] + consts.SOLDIER_BOTTOM <= consts.SCREEN_HEIGHT:
            soldier_pos[1] += consts.SOLDIER_SPEED

    elif event == pygame.K_UP:
        if soldier_pos[1] - 1 >= 0:
            soldier_pos[1] -= consts.SOLDIER_SPEED

    elif event == pygame.K_LEFT:
        if soldier_pos[0] - 1 >= 0:
            soldier_pos[0] -= consts.SOLDIER_SPEED

    else: # soldier moves right
        if soldier_pos[0] + consts.SOLDIER_SPEED * 2 < consts.SCREEN_WIDTH:
            soldier_pos[0] += consts.SOLDIER_SPEED

    Screen.create_screen()
    Screen.screen.blit(soldier_image, soldier_pos)

