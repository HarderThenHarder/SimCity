import pygame
from pygame.locals import *
from sys import exit

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
scale = 0.8


def main():
    pygame.init()
    pygame.display.set_caption("SimCity v1.0")
    screen = pygame.display.set_mode([int(SCREEN_WIDTH * scale), int(SCREEN_HEIGHT * scale)])

    background = pygame.image.load("img/bg.png")
    background = pygame.transform.scale(background, [int(SCREEN_WIDTH * scale), int(SCREEN_HEIGHT * scale)])

    myfont = pygame.font.Font(None, 30)
    textImage = myfont.render("Living Area", True, (0, 0, 0))

    while True:
        screen.blit(background, (0, 0))
        # draw river
        pygame.draw.rect(screen, (141, 178, 238), (0, 800 * scale, 1920 * scale, 50 * scale))
        # draw uptown
        pygame.draw.rect(screen, (0, 0, 0, 0.8), (20 * scale, 0, 400 * scale, 200 * scale), 3)
        pygame.draw.rect(screen, (231, 121, 24), (22 * scale, 2, 398 * scale, 197 * scale))
        screen.blit(textImage, (25, 5))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.QUIT
                exit()

        pygame.display.update()


if __name__ == '__main__':
    main()
