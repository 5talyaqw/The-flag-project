import consts
import GameField
import Screen
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


def load(num):
    game_field_path = Path(f"game_fields\\gameField{num+1}.csv")
    soldier_path = Path(f"game_fields\\soldier_position{num+1}.csv")

    if game_field_path.exists():
        game_df = pd.read_csv(game_field_path)
        for i in range(consts.MATRIX_ROWS):
            for j in range(consts.MATRIX_COLS):
                GameField.field[i][j] = "field"
    else:
        print("File doesn't exists")