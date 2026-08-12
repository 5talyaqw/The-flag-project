import pygame
import consts
import Soldier
import random
import Screen

field = []
mine = consts.BUSH_IMG

def unique_mine_positions():
    mines = consts.TOTAL_MINES
    positions = consts.MINE_POSITIONS
    while len(positions) < mines:
        row = random.randint(0, consts.MATRIX_ROWS - 1)
        col = random.randint(0, consts.MATRIX_COLS - 1)
        positions.add((row, col))
    return positions


def create_empty_field():
    global field
    field = [[0 for col in range(consts.MATRIX_COLS)] for row in range(consts.MATRIX_ROWS)]
    create_field()


def create_field():
    global field
    mine_positions = unique_mine_positions()
    for row in range(consts.MATRIX_ROWS):
        for col in range(consts.MATRIX_COLS):
            x = col * (consts.CELL_SIZE + consts.MARGIN) + consts.MARGIN
            y = row * (consts.CELL_SIZE + consts.MARGIN) + consts.MARGIN
            if (row, col) in mine_positions:
                field[row][col] = mine

def update_grass_mines():
    global field
    for row in range(len(field) - 1):
        for col in range(len(field[0]) - 1):
            if field[row][col] == consts.BUSH_IMG:
                field[row][col] = consts.MINE_IMG