import pygame
import random

def main():
    def draw_grid():
        #draw horizontal lines
        for i in range(1, 16):
            pygame.draw.line(
                screen, 
                line_color, 
                (0, i), 
                (width, i), 
                line_width
            )

        #draw vertical lines
        for i in range(1, 20):
            pygame.draw_line(
                screen, 
                line_color, 
                (i, 0),
                (i, height), 
                line_width
            )
    
    def draw_mole():
        rand_x = random.randint(1, 640)
        rand_y = random.randint(1, 512)
        screen.blit(mole_image, mole_image.get_rect(topleft = (0,0)))
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            screen.blit(mole_image, mole_image.get_rect(center = (rand_x, rand_y)))
                    
    try:
        pygame.init()
        width = 640
        height = 512
        line_width = 5
        line_color = "black"
        
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((width, height))
        clock = pygame.time.Clock()
        running = True
            
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
            screen.fill("light pink")
            pygame.display.flip()
            clock.tick(60)
         
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
