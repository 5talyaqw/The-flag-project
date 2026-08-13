import pygame
import consts
import Soldier
import random
import Screen

field = []
mine = consts.BUSH_IMG
grass_positions = consts.GRASS_POSITIONS


def unique_grass_positions():
    mines = consts.TOTAL_GRASS
    while len(grass_positions) < mines:
        row = random.randint(3, consts.MATRIX_ROWS)
        col = random.randint(0, consts.MATRIX_COLS)
        grass_positions.add((row, col))
    return grass_positions


def create_empty_field():
    global field
    field = [[0 for col in range(consts.MATRIX_COLS)] for row in range(consts.MATRIX_ROWS)]
    create_field()


def create_field():
    global field
    grass_pos = unique_grass_positions()
    for row in range(consts.MATRIX_ROWS):
        for col in range(consts.MATRIX_COLS):
            x = col * (consts.CELL_SIZE + consts.MARGIN) + consts.MARGIN
            y = row * (consts.CELL_SIZE + consts.MARGIN) + consts.MARGIN
            if (row, col) in grass_pos:
                field[row][col] = mine

def put_mines_instead_grass():
    mine_positions = consts.MINE_POSITIONS
    while len(mine_positions) < consts.TOTAL_MINES:
        pos = random.choice(list(grass_positions))
        mine_positions.add(pos)
    return mine_positions

def get_mine_pixels(): # gets mine positions, returns the mine pixel positions
    mine_pos = put_mines_instead_grass()
    pixel_convert = ()
    true_mine_pos = set()
    true_mine_pos.add((20,80))
    for mine in mine_pos:
        x = mine[0] * consts.CELL_SIZE
        y = mine[1] * consts.CELL_SIZE
        pixel_convert = (x, y)
        true_mine_pos.add(pixel_convert)
    return true_mine_pos
def update_grass_mines():
    global field
    mine_pos = put_mines_instead_grass()
    for row in range(len(field) - 1):
        for col in range(len(field[0]) - 1):
            if (row, col) in mine_pos:
                field[row][col] = consts.MINE_IMG

def draw_soldier(soldier_Image, soldier_pos):
    global field
    field[soldier_pos[0]][soldier_pos[1]] = soldier_Image
