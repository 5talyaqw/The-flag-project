import consts
import GameField
import Screen
import Soldier
import pandas as pd
gameFieldSavesList = []
soldierSavesList = []
# creating 9 slots
for gameField in range(0, 8):
    gameFieldSavesList.append("Empty Slot")
for soldier in range(0, 8):
    soldierSavesList.append("Empty Slot")
fieldDF = []
soldierDF = []

def Save(num):
    global gameFieldSavesList
    global soldierSavesList
    gameFieldSavesList[num-1] = GameField.field()
    soldierSavesList[num-1] = Soldier.soldier_pos
    fieldDF = pd.DataFrame(gameFieldSavesList)
    soldierDF = pd.DataFrame(soldierSavesList)
    fieldDF.to_csv("gameFieldSavesList.csv", index=False)
    soldierDF.to_csv("soldierSavesList.csv", index=False)
# def get_Save(num):
