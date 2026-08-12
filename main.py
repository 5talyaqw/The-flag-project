from pygame import event

import Screen
import Soldier
import consts
import GameField
import pygame

state = {
    "is_window_open": True,
    "state" : consts.RUNNING_STATE,
    "is_soldier_moving" : False,
    "is_night" : False,
}

def main():
    pygame.init()
    Screen.create_screen()
    while state["is_window_open"]:

        handle_user()
        Screen.draw_soldier()
        if state["is_soldier_moving"]:
                # see where he moves in a function and move him
            pass
        if state["is_night"]:
            GameField.mine = "mine.png"
            Soldier.soldier = "soldier_nigth.png"
        else:
            GameField.mine = "grass.png"
            Soldier.soldier = "soldier.png"
        pygame.display.update()
    pygame.quit()

def handle_user():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] == consts.RUNNING_STATE:
            continue

        if event.key == pygame.K_DOWN:
            pass

        if event.key == pygame.K_UP:
            pass

        if event.key == pygame.K_LEFT:
            pass

        if event.key == pygame.K_RIGHT:
            pass

        if event.key == pygame.K_KP_ENTER:
            pass


if __name__ == '__main__':
    main()