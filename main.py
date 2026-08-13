import sys

import GameField
import Screen
import Soldier
import consts
import pygame
import time
pygame.mixer.init()
from Screen import update_text

state = {
    "is_window_open": True,
    "state" : consts.RUNNING_STATE,
    "is_soldier_moving" : False,
    "is_shown" : 0,
    "night_vision" : False
}

KEYS = [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN]
start_cooldown = 0.0

def main():
    pygame.init()
    Screen.create_screen()
    update_text()

    while state["is_window_open"]:

        handle_user()
        is_lose()
        is_win()
        if state["state"] == 1:
            pygame.display.update()
            pass
        elif state["state"] == 2:
            Screen.draw_lose_message()


        elif state["state"] == 3:

            Screen.draw_win_message()
    pygame.quit()


def handle_user():
    global start_cooldown
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        if state["state"] != consts.RUNNING_STATE:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # יציאה בלחיצה על Esc
                    pygame.quit()
                    sys.exit()
        else:
            if event.type == pygame.KEYDOWN:

                state["is_shown"] += 1
                if state["is_shown"] == 1:
                    update_text(state["is_shown"])

                if event.key in KEYS:
                    if not state["night_vision"]:
                        Soldier.move_soldier(event.key)

                elapsed_time = time.time() - start_cooldown
                if event.key == pygame.K_RETURN and elapsed_time >= consts.COOLDOWN:
                    night_vision()
                    start_cooldown = time.time()
                pygame.event.clear()


def night_vision():
    state["night_vision"] = True
    Screen.night_vision_screen()
    start = time.time()

    while state["night_vision"]:
        elapsed_time = time.time() - start
        if elapsed_time >= consts.WAIT_NIGHT:
            Screen.create_screen()
            state["night_vision"] = False

def is_lose():
    if Soldier.is_on_mine():
        state["state"] = consts.LOSE_STATE

def is_win():
    if Soldier.is_on_flag():
        state["state"] = consts.WIN_STATE
        vic = pygame.mixer.Sound("VICTORY.wav")
        vic.play()


if __name__ == '__main__':
    main()