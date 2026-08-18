import pygame
import consts
import GameField
import Soldier
import teleport
import main
import time

pygame.init()
screen = pygame.display.set_mode(size=consts.SCREEN_SIZE)
explosionImg = pygame.image.load(consts.EXPLOSION_IMG)
explosionImg = pygame.transform.scale(explosionImg, (consts.SCREEN_WIDTH / 2, consts.SCREEN_HEIGHT))

def create_screen():
    screen.fill(consts.BACKGROUND_COLOR)
    pygame.display.set_caption('The flag game')
    if len(GameField.field) == 0:
        GameField.create_empty_field()
    draw_mine_grass(consts.BUSH_IMG)
    draw_flag()
    draw_soldier()
    teleport.create_teleports()
    draw_portal()

def draw_night_soldier():
    soldier_night = consts.SOLIDER_NIGHT_IMG
    soldier_night_image = pygame.image.load(soldier_night)
    soldier_night_image = pygame.transform.scale(soldier_night_image, (consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT))
    screen.blit(soldier_night_image, Soldier.soldier_pos)


def night_vision_screen():
    GameField.update_grass_mines()
    update_screen_net(consts.MINE_IMG)
    draw_night_soldier()
    pygame.display.update()

def update_text(disappear=False):
    # set text on the top left
    font = pygame.font.SysFont(None, 20)

    if not disappear:
        text = font.render('Welcome to the flag game! have fun', True, (255, 122, 149))
        text_rect = text.get_rect()
        text_rect.topleft = (0, 0)
        screen.blit(text, text_rect)
    else:
        create_screen()


def update_screen_net(item):
    screen.fill(color=pygame.color.Color(0,0,0))

    # vertical lines
    for x in range(0, consts.SCREEN_WIDTH, consts.CELL_SIZE):
        pygame.draw.line(screen, (4,95,11), (x,0),(x, consts.SCREEN_HEIGHT))

    # horozinal lines
    for y in range(0, consts.SCREEN_HEIGHT, consts.CELL_SIZE):
        pygame.draw.line(screen, (4,95,11), (0,y),(consts.SCREEN_WIDTH, y))
    draw_mine_grass(item)

def draw_mine_grass(item):
    field = GameField.field
    for row in range(len(field) - 1):
        for col in range(len(field[0]) -1):
            if field[row][col] == item:
                item_image = pygame.image.load(field[row][col]).convert_alpha()
                item_image = pygame.transform.scale(item_image, (consts.MINE_WIDTH, consts.MINE_HEIGHT))
                x = col * consts.CELL_SIZE
                y = row * consts.CELL_SIZE
                screen.blit(item_image, (x, y))


def draw_soldier():
    if main.is_lose():
        Soldier.injured_soldier()
    Soldier.create(Soldier.soldier_image, Soldier.soldier_pos)

def draw_explosion():
    screen.blit(explosionImg, consts.EXPLOSION_LOCATION)

def draw_flag():
    flag_img = pygame.image.load(consts.FLAG_IMG).convert_alpha()
    flag_img = pygame.transform.scale(flag_img, (consts.FLAG_WIDTH, consts.FLAG_HEIGHT))

    flag_x =(len(GameField.field[0]) - 1) * consts.CELL_SIZE - consts.FLAG_MARGIN_X
    flag_y = (len(GameField.field) - 1) * consts.CELL_SIZE - consts.FLAG_MARGIN_Y

    screen.blit(flag_img, (flag_x, flag_y))

def draw_lose_message():
    draw_explosion()
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)
    soldierINJURYYYY_image = pygame.image.load(consts.INJURY_IMG)
    soldierINJURYYYY_image = pygame.transform.scale(soldierINJURYYYY_image, (consts.SCREEN_WIDTH // 2,
                                                                             consts.SCREEN_HEIGHT))
    screen.blit(soldierINJURYYYY_image, (consts.SCREEN_WIDTH // 2, consts.SCREEN_HEIGHT))


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)

    pygame.display.update()
    start_time = time.time()
    freeze = True
    while freeze:
        elapsed_time = time.time() - start_time
        if elapsed_time == consts.COOLDOWN:
            freeze = False

def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)
    pygame.display.update()

def draw_portal():
    for row in range(consts.MATRIX_ROWS):
        for col in range(consts.MATRIX_COLS):
            if GameField.field[row][col] == consts.TELEPORT_IMG:
                item_image = pygame.image.load(GameField.field[row][col]).convert_alpha()
                item_image = pygame.transform.scale(item_image, (consts.MINE_WIDTH, consts.MINE_HEIGHT))
                x = col * consts.CELL_SIZE
                y = row * consts.CELL_SIZE
                screen.blit(item_image, (x, y))