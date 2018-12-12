import pygame
from pygame.locals import *
from sys import exit
from AreaConfig import AreaConfig
from Citizen import Citizen
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
    ticks = 0

    background = pygame.image.load("img/bg.png")
    background = pygame.transform.scale(background, [int(SCREEN_WIDTH * scale), int(SCREEN_HEIGHT * scale)])

    citizen_group = []
    for i in range(20):
        citizen = Citizen([220 * scale, 200 * scale], config.market, config.get_road_area(), config.get_cross_list())
        citizen_group.append(citizen)

    while True:
        clock.tick(10)
        # screen.blit(background, (0, 0))
        screen.fill(color=(255, 255, 255))

        # Draw the scene
        draw_object(screen, config.get_rect_obs_list(), config.get_poly_obs_list())

        # Draw citizen
        for citizen in citizen_group:
            screen.blit(citizen.image, citizen.pos)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                for citizen in citizen_group:
                    citizen.change_target(config.living_area)
                    citizen.update()

        if ticks % 2 == 0:
            for citizen in citizen_group:
                citizen.update()

        ticks += 1
        pygame.display.update()


if __name__ == '__main__':
    main()
