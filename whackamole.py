import pygame
import random
import math

def main():
    try:
        pygame.init()
        
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        moleCoords = ((round(random.random() * 19)) * 32, (round(random.random() * 15)) * 32)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    clickCoords = event.pos
                    if math.floor(event.pos[0] / 32) == math.floor(moleCoords[0] / 32) and math.floor(event.pos[1] / 32) == math.floor(moleCoords[1] / 32):
                        moleCoords = ((round(random.random() * 19)) * 32, (round(random.random() * 15)) * 32)
            screen.fill("light green")
            for i in range(0,21):
                pygame.draw.line(screen, (255,0,0) , (i * 32,0), (i * 32,512))
            for i in range(0,17):
                pygame.draw.line(screen, (0,0,255) , (0,i * 32), (640,i * 32))
            screen.blit(mole_image, mole_image.get_rect(topleft = moleCoords))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
