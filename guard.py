import Screen
import Soldier
import pygame
import consts

guard_img = pygame.image.load(consts.GUARD_IMG).convert_alpha()
guard_img = pygame.transform.scale(guard_img, (consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT))
guard_topleft_pos = [240,0]
guard_direction = 'bottom'

guard_caught = pygame.image.load(consts.LOSE_BY_GUARD).convert_alpha()
guard_caught = pygame.transform.scale(guard_caught, (consts.SOLDIER_WIDTH * 2, consts.SOLDIER_HEIGHT * 2))

state_guard = False


def change_direction():
    global guard_direction

    if guard_direction == 'left':
        guard_direction = 'right'

    elif guard_direction == 'right':
        guard_direction = 'left'
    # incase the guard direction is down
    else:
        guard_direction = 'right'

def move_guard():
    global guard_topleft_pos
    guard_top_right = [guard_topleft_pos[0] + consts.SOLDIER_WIDTH,0]
    guard_bottom_mid = [guard_topleft_pos[0] + consts.SOLDIER_WIDTH / 2,guard_topleft_pos[1] + consts.SOLDIER_HEIGHT]
    if guard_direction == 'left' and guard_topleft_pos[0] + consts.GUARD_SPEED >= 0:
        guard_topleft_pos[0] -= consts.GUARD_SPEED

    elif guard_direction == 'right' and guard_top_right[0] + consts.GUARD_SPEED <= consts.SCREEN_WIDTH:
        guard_topleft_pos[0] += consts.GUARD_SPEED

    elif guard_direction == 'bottom' and guard_bottom_mid[1] + consts.GUARD_SPEED <= consts.SCREEN_HEIGHT // 2:
        guard_topleft_pos[1] += consts.GUARD_SPEED
    else:
        change_direction()


def is_touch_soldier():
    global state_guard

    soldier_top_right = [Soldier.soldier_pos[0] + consts.SOLDIER_WIDTH, Soldier.soldier_pos[1]]
    soldier_bottom_left = [Soldier.soldier_pos[0], Soldier.soldier_pos[1] + consts.SOLDIER_HEIGHT]
    soldier_bottom_right = [Soldier.soldier_pos[0] + consts.SOLDIER_WIDTH, Soldier.soldier_pos[1] + consts.SOLDIER_HEIGHT]

    guard_top_right = [guard_topleft_pos[0] + consts.SOLDIER_WIDTH,guard_topleft_pos[1]]
    guard_bottom_left = [guard_topleft_pos[0],guard_topleft_pos[1] + consts.SOLDIER_HEIGHT]
    guard_bottom_right = [guard_topleft_pos[0] + consts.SOLDIER_WIDTH,guard_topleft_pos[1] + consts.SOLDIER_HEIGHT]

    if soldier_top_right == guard_topleft_pos and soldier_bottom_right == guard_bottom_left:
        state_guard = True
        return True
    elif Soldier.soldier_pos == guard_top_right and soldier_bottom_left == guard_bottom_right:
        state_guard = True
        return True

    return False

