SOLIDER_IMG = "C:\\Users\\jbt\\PycharmProjects\\The-flag-project\\flag_images\\soldier.png"
BUSH_IMG = "C:\\Users\\jbt\\PycharmProjects\\The-flag-project\\flag_images\\grass.png"
MINE_IMG = "C:\\Users\\jbt\\PycharmProjects\\The-flag-project\\flag_images\\mine.png"
SOLIDER_NIGHT_IMG = "C:\\Users\\jbt\\PycharmProjects\\The-flag-project\\flag_images\\soldier_nigth.png"
FLAG_IMG = "C:\\Users\\jbt\\PycharmProjects\\The-flag-project\\flag_images\\flag.png"
EXPLOSION_IMG = "C:\\Users\\jbt\\PycharmProjects\\The-flag-project\\flag_images\\explotion.png"
INJURY_IMG = "C:\\Users\\jbt\\PycharmProjects\\The-flag-project\\flag_images\\injury.png"
DINO_SOLIDER_IMG = "C:\\Users\\jbt\\PycharmProjects\\The-flag-project\\flag_images\\solider (2).png"
SNAKE_IMG = "C:\\Users\\jbt\\PycharmProjects\\The-flag-project\\flag_images\\snake.png"


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
BACKGROUND_COLOR = (4, 95, 11)



COOLDOWN = 10.0
RUNNING_STATE = 1
LOSE_STATE = 2
WIN_STATE = 3