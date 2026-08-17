import sys
import database
import Screen
import Soldier
import consts
import pygame
import time
pygame.mixer.init()

state = {
    "is_window_open": True,
    "state" : consts.RUNNING_STATE,
    "is_soldier_moving" : False,
    "is_shown" : 0,
    "night_vision" : False
}

KEYS = [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN]
NUMBERS = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]
start_cooldown = 0.0
hold_key = 0.0

def main():
    pygame.init()
    Screen.create_screen()
    Screen.update_text()

    while state["is_window_open"]:

        handle_user()
        is_lose()
        is_win()
        if state["state"] == 1:
            pygame.display.update()
            pass
        elif state["state"] == 2:
            Screen.draw_lose_message()
            break

        elif state["state"] == 3:

            Screen.draw_win_message()
            break
    pygame.quit()


def handle_user():
    global start_cooldown
    global hold_key

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
                hold_key = time.time()

                state["is_shown"] += 1
                if state["is_shown"] == 1:
                    Screen.update_text(state["is_shown"])

                if event.key in KEYS:
                    if not state["night_vision"]:
                        Soldier.move_soldier(event.key)

                elapsed_time = time.time() - start_cooldown
                if event.key == pygame.K_RETURN and elapsed_time >= consts.COOLDOWN:
                    night_vision()
                    start_cooldown = time.time()
                    pygame.event.clear()

            if event.type == pygame.KEYUP and event.key in NUMBERS:
                end_time = time.time() - hold_key
                if end_time <= 1:
                    database.save(NUMBERS.index(event.key))
                else:
                    database.load(NUMBERS.index(event.key))


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