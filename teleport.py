import GameField
import Screen
import Soldier
import consts
import random

import main

tplist =[]
pixel_teleport_mid_pos = []

def create_teleports():
    mine_pos = GameField.put_mines_instead_grass()
    while len(tplist) != consts.TELEPORTATION_AMOUNT:
        tp_pos = [(random.randint(3, consts.MATRIX_ROWS-1)), (random.randint(0, consts.MATRIX_COLS-1))]

        x = (tp_pos[1] * consts.CELL_SIZE) + consts.MINE_WIDTH / 2
        y = (tp_pos[0] * consts.CELL_SIZE) + consts.MINE_HEIGHT
        pixel_convert = [x, y]


        if tuple(tp_pos) not in mine_pos and GameField.field[tp_pos[0]][tp_pos[1]] == 'free':
            tplist.append(tp_pos)
            pixel_teleport_mid_pos.append(pixel_convert)


def is_on_tp():
    legs = Soldier.soldier_legs_position()
    if list(legs) in pixel_teleport_mid_pos:
        return True
    return False

def random_teleport():
    soldier_legs = random.choice(pixel_teleport_mid_pos)
    Soldier.soldier_pos = [soldier_legs[0] - consts.MINE_WIDTH /2, soldier_legs[1] - consts.SOLDIER_HEIGHT]
    Screen.create_screen(main.state["is_loaded"])

