import pygame
import consts
import Soldier
import random
import Screen

field = []
mine_image = pygame.image.load(consts.MINE_IMG)
mine_image = pygame.transform.scale(mine_image, (consts.MINE_WIDTH, consts.MINE_HEIGHT))

def unique_mine_positions():
    mines = consts.TOTAL_MINES
    positions = consts.MINE_POSITIONS
    while len(positions) < mines:
        row = random.randint(0, consts.MATRIX_ROWS - 1)
        col = random.randint(0, consts.MATRIX_COLS - 1)
        positions.add((row, col))
    return positions

def create_field():
    global field
    mine_positions = unique_mine_positions()
    for row in range(consts.MATRIX_ROWS):
        for col in range(consts.MATRIX_COLS):
            x = col * (consts.CELL_SIZE + consts.MARGIN) + consts.MARGIN
            y = row * (consts.CELL_SIZE + consts.MARGIN) + consts.MARGIN

            if (row, col) in mine_positions:
                Screen.screen.blit(mine_image, (x, y))