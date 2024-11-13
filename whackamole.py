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
        height = 512
        line_color = "black"
        square_size = 32


        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((width, height))
        clock = pygame.time.Clock()
        running = True

        while running:
            rand_x = random.randint(1, 21)
            rand_y = random.randint(1, 17)
            mole_rect = mole_image.get_rect(topleft = (rand_x, rand_y))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos

                    if event.pos == mole_rect:
                        screen.blit(mole_image, mole_rect)

            screen.fill("light pink")
            draw_grid(screen, line_color, square_size, width, height)
            screen.blit(mole_image, mole_image.get_rect(topleft = (0,0)))
            pygame.display.flip()
            clock.tick(60)
         
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
