SOLIDER_IMG = "C:\\Users\\97254\\PycharmProjects\\The-flag-project\\flag_images\\soldier.png"
BUSH_IMG = "C:\\Users\\97254\\PycharmProjects\\The-flag-project\\flag_images\\grass.png"
MINE_IMG = "C:\\Users\\97254\\PycharmProjects\\The-flag-project\\flag_images\\mine.png"
SOLIDER_NIGHT_IMG = "C:\\Users\\97254\\PycharmProjects\\The-flag-project\\flag_images\\solider_night.png"
FLAG_IMG = "C:\\Users\\97254\\PycharmProjects\\The-flag-project\\flag_images\\flag.png"
EXPLOSION_IMG = "C:\\Users\\97254\\PycharmProjects\\The-flag-project\\flag_images\\explotion.png"
INJURY_IMG = "C:\\Users\\97254\\PycharmProjects\\The-flag-project\\flag_images\\injury.png"
DINO_SOLIDER_IMG = "C:\\Users\\97254\\PycharmProjects\\The-flag-project\\flag_images\\solider (2).png"
SNAKE_IMG = "C:\\Users\\97254\\PycharmProjects\\The-flag-project\\flag_images\\snake.png"
TELEPORT_IMG = "C:\\Users\\97254\\PycharmProjects\\lag-project\\flag_images\\teleport.png"
GUARD_IMG = "C:\\Users\\97254\\PycharmProjects\\The-flag-project\\flag_images\\guard.png"
LOSE_BY_GUARD = "C:\\Users\\97254\\PycharmProjects\\The-flag-project\\flag_images\\guardarrestingplayer.png"

MARGIN = 2
MATRIX_ROWS = 25
MATRIX_COLS = 50
CELL_SIZE = 20

SCREEN_WIDTH = MATRIX_COLS * CELL_SIZE
SCREEN_HEIGHT = MATRIX_ROWS * CELL_SIZE
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

SOLDIER_WIDTH = 40
SOLDIER_HEIGHT = 80
SOLDIER_SIZE = (SOLDIER_WIDTH, SOLDIER_HEIGHT)
SOLDIER_SPEED = 20
SOLDIER_BOTTOM = 100

TOTAL_GRASS = 20
TOTAL_MINES = 10
MINE_POSITIONS = set()
GRASS_POSITIONS = set()

FLAG_HEIGHT = 60
FLAG_WIDTH = 50
FLAG_MARGIN_X = 30
FLAG_MARGIN_Y = 45

MINE_HEIGHT = 20
MINE_WIDTH = 40

TELEPORTATION_AMOUNT = 5



BACKGROUND_COLOR = (4, 95, 11)
BLACK = (0, 0, 0)
FONT_NAME = "Calibri"
LOSE_MESSAGE = "You Lost!"
LOSE_FONT_SIZE = int(0.15 * SCREEN_WIDTH)
LOSE_COLOR = BLACK
LOSE_LOCATION = \
    (0.2 * SCREEN_WIDTH, SCREEN_HEIGHT / 2 - (LOSE_FONT_SIZE / 2))
WIN_MESSAGE = "You Won!"
WIN_FONT_SIZE = LOSE_FONT_SIZE
WIN_COLOR = (255, 149, 169)
WIN_LOCATION = \
    (0.2 * SCREEN_WIDTH, SCREEN_HEIGHT / 2 - (WIN_FONT_SIZE / 2))
EXPLOSION_LOCATION = (LOSE_LOCATION[0], LOSE_LOCATION[1] -100)



WAIT_NIGHT = 1
COOLDOWN = 3.00
TELEPORT_COOLDOWN = 2

RUNNING_STATE = 1
LOSE_STATE = 2
WIN_STATE = 3