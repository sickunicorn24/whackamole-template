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

        screen.fill("black")
        draw_grid(screen, line_color, square_size, width, height)
        screen.blit(mole_image, mole_image.get_rect(topleft = (current_x, current_y)))
        pygame.display.flip()
        clock.tick(60)

        rand_x = random.randint(0, columns)
        rand_y = random.randint(0, rows)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos

                    start_x = current_x * square_size
                    end_x = (current_x+1) * square_size

                    start_y = current_y * square_size
                    end_y = (current_y+1) * square_size

                    if (start_x <= x <= end_x) and (start_y <= y <= end_y):
                        current_x = rand_x * square_size
                        current_y = rand_y * square_size

                    screen.fill("black")
                    draw_grid(screen, line_color, square_size, width, height)

                    screen.blit(mole_image, mole_image.get_rect(topleft = (current_x, current_y)))
                    pygame.display.flip()

                    print(current_x)
                    print(current_y)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
