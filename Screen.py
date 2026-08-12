import pygame
import consts
import GameField


pygame.init()
screen = pygame.display.set_mode(size=consts.SCREEN_SIZE)

def create_screen():
    screen.fill(consts.BACKGROUND_COLOR)
    pygame.display.set_caption('The flag game')
    GameField.create_field()



def update_text(disappear=False):
    # set text on the top left
    font = pygame.font.SysFont(None, 20)

    if not disappear:
        text = font.render('Welcome to the flag game! have fun', True, (255, 122, 149))
        text_rect = text.get_rect()
        text_rect.topleft = (0, 0)
        screen.blit(text, text_rect)
    else:
        screen.fill(color=pygame.color.Color(4, 95, 11))


def update_screen_net():
    screen.fill(color=pygame.color.Color(0,0,0))

    # vertical lines
    for x in range(0, consts.SCREEN_WIDTH, consts.CELL_SIZE):
        pygame.draw.line(screen, (4,95,11), (x,0),(x, consts.SCREEN_HEIGHT))

    # horozinal lines
    for y in range(0, consts.SCREEN_HEIGHT, consts.CELL_SIZE):
        pygame.draw.line(screen, (4,95,11), (0,y),(consts.SCREEN_WIDTH, y))


def draw_soldier():
    soldier_img = pygame.image.load(consts.SOLIDER_IMG).convert_alpha()
    screen.blit(soldier_img,(0,0))