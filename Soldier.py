import GameField
import pygame
import consts
import Screen
pygame.mixer.init()
soldier = consts.SOLIDER_IMG
soldier_image = pygame.image.load(soldier)
soldier_image = pygame.transform.scale(soldier_image, (consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT))

soldier_pos = [0,0]
soldier_injury = consts.INJURY_IMG
soldierINJURYYYY_image = pygame.image.load(soldier_injury)
soldierINJURYYYY_image = pygame.transform.scale(soldierINJURYYYY_image, (consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT))
explosionImg = pygame.image.load(consts.EXPLOSION_IMG).convert_alpha()

def create(image, position):
    Screen.screen.blit(image, position)

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
def soldier_legs_position(soldier_position):
    soldier_rect = soldier_image.get_rect()
    soldier_pos_mid_bottom = soldier_rect.midbottom
    soldier_position_bottom = (soldier_pos_mid_bottom[0] + soldier_position[0], soldier_pos_mid_bottom[1] + soldier_position[1])
    return soldier_position_bottom


def is_on_mine():
    soldier_pos_bottom = soldier_legs_position(soldier_pos)
    mine_pos = GameField.get_mine_pixels()
    if soldier_pos_bottom in mine_pos:
        explosion = pygame.mixer.Sound("EXPLOSIONN.wav")
        explosion.play()
        injured_soldier()
        return True
    return False

def is_on_flag():
    flag_pos = get_flag_pos()
    bottom_right = [soldier_pos[0] + consts.SOLDIER_WIDTH, soldier_pos[1] + consts.SOLDIER_HEIGHT]
    top_right = [soldier_pos[0] + consts.SOLDIER_WIDTH, soldier_pos[1]]
    if (bottom_right[0] >= flag_pos[0] and bottom_right[1] >= flag_pos[1]) and (top_right[1] + 20 >= flag_pos[1]):
        return True
    return False


def get_flag_pos():
    flag_x = (len(GameField.field[0]) - 1) * consts.CELL_SIZE - consts.FLAG_MARGIN_X
    flag_y = (len(GameField.field) - 1) * consts.CELL_SIZE - consts.FLAG_MARGIN_Y
    return [flag_x,flag_y]

def injured_soldier():
    Screen.screen.blit(soldierINJURYYYY_image, ((soldier_pos[0]) , (soldier_pos[1])))

