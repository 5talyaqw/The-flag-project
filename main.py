import screen
import consts
import game_field
import pygame

pygame.init()



def main():
    screen.create_screen()
    running = True
    show_text = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                show_text +=1
                if show_text == 1:
                    screen.update_text(show_text)
                if event.key == pygame.K_DOWN:
                    pass
                if event.key == pygame.K_UP:
                    pass
                if event.key == pygame.K_LEFT:
                    pass
                if event.key == pygame.K_RIGHT:
                    pass
                if event.key == pygame.K_KP_ENTER:
                    pass

        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    main()
