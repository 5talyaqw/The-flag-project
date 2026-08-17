import consts
import Soldier
import random

field = []
grass = consts.BUSH_IMG
grass_positions = consts.GRASS_POSITIONS

def unique_grass_positions():
    mines = consts.TOTAL_GRASS
    while len(grass_positions) < mines:
        row = random.randint(3, consts.MATRIX_ROWS - 1)
        col = random.randint(0, consts.MATRIX_COLS - 1)
        while field[row][col] == "flag" and ([col * consts.CELL_SIZE ,row * consts.CELL_SIZE] == Soldier.soldier_pos):
            row = random.randint(3, consts.MATRIX_ROWS)
            col = random.randint(0, consts.MATRIX_COLS)
        grass_positions.add((row, col))
    return grass_positions


def create_empty_field():
    global field
    field = [[0 for col in range(consts.MATRIX_COLS)] for row in range(consts.MATRIX_ROWS)]
    put_flag_in_matrix()
    create_field()


def create_field():
    global field
    grass_pos = unique_grass_positions()
    for row in range(consts.MATRIX_ROWS):
        for col in range(consts.MATRIX_COLS):
            x = col * consts.CELL_SIZE
            y = row * consts.CELL_SIZE
            if (row, col) in grass_pos:
                field[row][col] = grass

def put_mines_instead_grass():
    mine_positions = consts.MINE_POSITIONS
    while len(mine_positions) < consts.TOTAL_MINES:
        pos = random.choice(list(grass_positions))
        mine_positions.add(pos)
    return mine_positions

def put_flag_in_matrix():
    for row in range(consts.MATRIX_ROWS - 3,len(field)):
        for i in range(4):
            field[row][consts.MATRIX_COLS - i - 1] = "flag"


def get_mine_pixels(): # gets mine positions, returns the mine pixel positions
    mine_pos = put_mines_instead_grass()
    true_mine_pos = set()
    for mine in mine_pos:
        x = (mine[1] * consts.CELL_SIZE) + consts.MINE_WIDTH / 2
        y = (mine[0] * consts.CELL_SIZE) + consts.MINE_HEIGHT
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