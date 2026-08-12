import pygame
import consts
import GameField
import Soldier

pygame.init()
screen = pygame.display.set_mode(size=consts.SCREEN_SIZE)


def create_screen():
    screen.fill(consts.BACKGROUND_COLOR)
    pygame.display.set_caption('The flag game')
    GameField.create_empty_field()
    draw_mine_grass(consts.BUSH_IMG)



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

    draw_soldier()
    draw_mine_grass(item)

def draw_mine_grass(item):
    field = GameField.field.copy()
    for row in range(len(field) - 1):
        for col in range(len(field[0]) -1):
            if field[row][col] == item:
                item_image = pygame.image.load(field[row][col]).convert_alpha()
                item_image = pygame.transform.scale(item_image, (consts.MINE_WIDTH, consts.MINE_HEIGHT))

                x = col * (consts.CELL_SIZE + consts.MARGIN) + consts.MARGIN
                y = row * (consts.CELL_SIZE + consts.MARGIN) + consts.MARGIN
                screen.blit(item_image, (x, y))


def draw_soldier():
    Soldier.create()