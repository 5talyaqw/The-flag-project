import GameField
import pygame
import consts
import Screen

soldier = consts.SOLIDER_IMG
soldier_image = pygame.image.load(soldier)
soldier_image = pygame.transform.scale(soldier_image, (consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT))
soldier_pos = [0,0]


def create():
    Screen.screen.blit(soldier_image, soldier_pos)


def move_soldier(event):
    if event == pygame.K_DOWN:
        if soldier_pos[1] + consts.SOLDIER_BOTTOM <= consts.SCREEN_HEIGHT:
            soldier_pos[1] += consts.SOLDIER_SPEED

    elif event == pygame.K_UP:
        if soldier_pos[1] - 1 >= 0:
            soldier_pos[1] -= consts.SOLDIER_SPEED

    elif event == pygame.K_LEFT:
        if soldier_pos[0] - 1 >= 0:
            soldier_pos[0] -= consts.SOLDIER_SPEED

    else: # soldier moves right
        if soldier_pos[0] + consts.SOLDIER_WIDTH < consts.SCREEN_WIDTH:
            soldier_pos[0] += consts.SOLDIER_SPEED

    Screen.create_screen()
    Screen.screen.blit(soldier_image, soldier_pos)

def is_on_mine():
    soldier_pos_bottom = (soldier_pos[0] + consts.SOLDIER_WIDTH, soldier_pos[1] + consts.SOLDIER_BOTTOM)
    print(soldier_pos_bottom)
    mine_pos = GameField.get_mine_pixels()
    print(mine_pos)
    if soldier_pos_bottom in mine_pos:
        return True
    else:
        return False

def is_on_flag():
    flag_pos = get_flag_pos()
    if soldier_pos[0] + consts.SOLDIER_SPEED >= flag_pos[0] and soldier_pos[1] + consts.SOLDIER_SPEED >= flag_pos[1]:
        return True
    return False


def get_flag_pos():
    flag_x = (len(GameField.field[0]) - 1) * consts.CELL_SIZE - consts.FLAG_MARGIN_X
    flag_y = (len(GameField.field) - 1) * consts.CELL_SIZE - consts.FLAG_MARGIN_Y
    return [flag_x,flag_y]