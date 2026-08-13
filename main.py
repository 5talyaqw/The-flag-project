import Screen
import Soldier
import consts
import pygame
import time

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
        pygame.display.update()
    pygame.quit()

def handle_user():
    global start_cooldown
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] == consts.RUNNING_STATE:
            pass
        if event.type == pygame.KEYDOWN:
            state["is_shown"] += 1
            if state["is_shown"] == 1:
                update_text(state["is_shown"])

            if event.key in KEYS:
                print(state["night_vision"])
                Soldier.move_soldier(event.key)

            elapsed_time = time.time() - start_cooldown
            if event.key == pygame.K_RETURN and elapsed_time >= consts.COOLDOWN:
                night_vision()
                start_cooldown = time.time()





def night_vision():
    state["night_vision"] = True

    Screen.night_vision_screen()

    allocated_time = 1  # 1 second wait
    start = time.time()

    while state["night_vision"]:
        elapsed_time = time.time() - start
        if elapsed_time >= allocated_time:
            Screen.create_screen()
            state["night_vision"] = False



if __name__ == '__main__':
    main()