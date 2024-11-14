import pygame
import random
#Added comment
def draw_grid(screen, line_color, square_size, width, height):
    #draw horizontal lines
    for i in range(1, 16):
        pygame.draw.line(
            screen,
            line_color,
            (0, i*square_size),
            (width, i*square_size),

        )

    #draw vertical lines
    for i in range(1, 20):
        pygame.draw.line(
            screen,
            line_color,
            (i*square_size, 0),
            (i*square_size, height),

        )

def main():

    try:
        pygame.init()
        width = 640
        rows = 16
        columns = 20
        height = 512
        line_color = "light green"
        square_size = 32

        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((width, height))
        clock = pygame.time.Clock()
        running = True

        current_x = 0
        current_y = 0

        #draws the background and grid with the mole in the top left square
        screen.fill("black")
        draw_grid(screen, line_color, square_size, width, height)
        screen.blit(mole_image, mole_image.get_rect(topleft = (current_x, current_y)))
        pygame.display.flip()
        clock.tick(60)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                #checks if the mouse clicks within the mole's square, and if so moves it to a random location
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos

                    start_x = current_x * square_size
                    end_x = (current_x+1) * square_size
                    start_y = current_y * square_size
                    end_y = (current_y+1) * square_size

                    if (start_x <= x <= end_x) and (start_y <= y <= end_y):
                        current_x = random.randint(0, columns-1)
                        current_y = random.randint(0, rows-1)

                        screen.fill("black")
                        draw_grid(screen, line_color, square_size, width, height)

                        screen.blit(mole_image, mole_image.get_rect(topleft = (current_x * square_size, current_y * square_size)))
                        pygame.display.flip()

            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
