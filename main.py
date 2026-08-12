import Screen
import Soldier
import consts
import GameField
import pygame
import time

from Screen import update_text

state = {
    "is_window_open": True,
    "state" : consts.RUNNING_STATE,
    "is_soldier_moving" : False,
    "is_night" : False,
    "is_shown" : 0,
    "night_vision" : True
}

def main():
    pygame.init()
    Screen.create_screen()
    update_text()


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
            pass
        if event.type == pygame.KEYDOWN:
            state["is_shown"] += 1
            if state["is_shown"] == 1:
                update_text(state["is_shown"])

            if event.key == pygame.K_DOWN:
                pass

            if event.key == pygame.K_UP:
                pass

            if event.key == pygame.K_LEFT:
                pass

            if event.key == pygame.K_RIGHT:
                pass

            if event.key == pygame.K_RETURN:
                state["night_vision"] = True
                allocated_time = 1 # 1 second wait
                start = time.time()

                Screen.update_screen_net()
                pygame.display.update()

                while state["night_vision"]:
                    elapsed_time = time.time() - start

                    if elapsed_time >= allocated_time:
                        Screen.create_screen()
                        state["night_vision"] = False





if __name__ == '__main__':
    main()