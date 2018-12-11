import pygame
from pygame.locals import *
from sys import exit
from AreaConfig import AreaConfig
from Pencil import Pencil
from PencilForSimCity import PencilForSimCity

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
scale = 0.8
clock = pygame.time.Clock()


def draw_object(screen, rec_obs, poly_obs):
    for ob in rec_obs:
        PencilForSimCity.draw_area(screen, ob.get_color(), ob.get_rect(), ob.get_name(),
                                   name_color=(220, 220, 220))

    for poly_ob in poly_obs:
        PencilForSimCity.draw_poly_area(screen, poly_ob.get_color(), poly_ob.get_pos_list(), poly_ob.get_name(),
                                        name_color=(220, 220, 220))


def main():
    pygame.init()
    pygame.display.set_caption("SimCity v1.0")
    screen = pygame.display.set_mode([int(SCREEN_WIDTH * scale), int(SCREEN_HEIGHT * scale)])
    config = AreaConfig(scale)

    background = pygame.image.load("img/bg.png")
    background = pygame.transform.scale(background, [int(SCREEN_WIDTH * scale), int(SCREEN_HEIGHT * scale)])

    while True:
        clock.tick(10)
        # screen.blit(background, (0, 0))
        screen.fill(color=(200, 200, 200))

        # Draw the scene
        draw_object(screen, config.get_rect_obs_list(), config.get_poly_obs_list())

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        pygame.display.update()


if __name__ == '__main__':
    main()
