import GameField
import Screen
import Soldier
import consts
import main
import random
tplist =[]

def create():
    mine_pos = GameField.put_mines_instead_grass()
    tp_amount = 0
    while tp_amount != consts.TELEPORTATION_AMOUNT:
        tp_pos = [(random.randint(0, consts.MATRIX_ROWS)), (random.randint(0, consts.MATRIX_COLS))]
        if tp_pos in mine_pos:
            continue
        else:
            GameField.field[tp_pos[0]][tp_pos[1]] = consts.TELEPORT_IMG
            tplist.append(tp_pos)
            tp_amount += 1

def is_on_tp(soldier_pos, tp_list):
    Soldier.soldier_legs_position(soldier_pos)
    for tp_pos in tp_list:
        if tp_pos == soldier_pos:
            return True
    return False

def random_teleport(soldier_pos):
    soldier_pos = random.choice(tplist)
    return soldier_pos
