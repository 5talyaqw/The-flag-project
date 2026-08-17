import consts
import GameField
import Soldier
import pandas as pd
from pathlib import Path

fieldDF = []
soldierDF = []


def save(num):
    global fieldDF
    global soldierDF

    game_field_path = Path(f"game_fields\\gameField{num+1}.csv")
    soldier_path = Path(f"game_fields\\soldier_position{num+1}.csv")
    # creating data frames for each
    fieldDF = pd.DataFrame(GameField.field)
    soldierDF = pd.DataFrame(Soldier.soldier_pos)

    # creating csv file and writing to it
    fieldDF.to_csv(game_field_path, index=False)
    soldierDF.to_csv(soldier_path, index=False)


def print_field():
    for row in range(consts.MATRIX_ROWS):
        for col in range(consts.MATRIX_COLS):
            print(GameField.field[row][col], end=' ')
        print()
    print('\n\n\n')


def load(num):
    game_field_path = Path(f"game_fields\\gameField{num+1}.csv")
    soldier_path = Path(f"game_fields\\soldier_position{num+1}.csv")

    if game_field_path.exists():
        game_csv = pd.read_csv(game_field_path)
        for row in range(consts.MATRIX_ROWS):
            for col in range(consts.MATRIX_COLS):
                GameField.field[row][col] = game_csv.iloc[row,col]
        soldier_csv = pd.read_csv(soldier_path)
        Soldier.soldier_pos[0] = soldier_csv.iloc[0,0]
        Soldier.soldier_pos[1] = soldier_csv.iloc[1,0]

    else:
        print("File doesn't exists")