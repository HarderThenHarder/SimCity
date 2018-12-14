import pygame
from pygame.locals import *
from sys import exit
from AreaConfig import AreaConfig
from Citizen import Citizen
from Pencil import Pencil
from PencilForSimCity import PencilForSimCity
import time
from SearchRoad import CityMap
from CitizenByFloyd import CitizenByFloyd

from Timer import Timer

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 960
scale = 0.8
clock = pygame.time.Clock()


def draw_object(screen, rec_obs, poly_obs):
    for ob in rec_obs:
        PencilForSimCity.draw_area(screen, ob.get_color(), ob.get_rect(), ob.get_name())
    for poly_ob in poly_obs:
        PencilForSimCity.draw_poly_area(screen, poly_ob.get_color(), poly_ob.get_pos_list(), poly_ob.get_name())


def trigger(timer, citizen_group, config):
    second = timer.get_second()
    minute = timer.get_minute()
    hour = timer.get_hour()

    if hour == 19 and minute == 48 and second == 26:
        for citizen in citizen_group:
            citizen.change_target(config.market)
            citizen.update()

    if hour == 19 and minute == 49 and second == 5:
        for citizen in citizen_group:
            citizen.change_target(config.restaurant)
            citizen.update()

    if hour == 19 and minute == 49 and second == 20:
        for citizen in citizen_group:
            citizen.change_target(config.living_area)
            citizen.update()


def main():
    pygame.init()
    pygame.display.set_caption("SimCity v1.0")
    screen = pygame.display.set_mode([int(SCREEN_WIDTH * scale), int(SCREEN_HEIGHT * scale)])
    config = AreaConfig(scale)
    timer = Timer()
    timer.set_time(19, 48, 23)
    ticks = 0
    tick_elapsed = 0

    # Create City Map
    graph = config.get_city_map()
    node_list = graph[0]
    edge_list = graph[1]
    city_map = CityMap(node_list, edge_list)

    background = pygame.image.load("img/city_bg2.png")
    background = pygame.transform.scale(background, [int(SCREEN_WIDTH * scale), int(SCREEN_HEIGHT * scale)])

    citizen_group = []
    # for i in range(20):
    #     citizen = Citizen([220 * scale, 100 * scale], config.living_area, "walk_in_area", config.get_road_area(), config.get_cross_list(),
    #                       in_which_area=config.living_area)
    #     citizen_group.append(citizen)

    for i in range(20):
        citizen = CitizenByFloyd([220 * scale, 100 * scale], config.living_area, "walk_in_area", config.get_road_area(),
                                 config.get_cross_list(), city_map,
                                 in_which_area=config.living_area)
        citizen_group.append(citizen)

    while True:
        since = time.time()
        clock.tick(10)

        # screen.blit(background, (0, 0))
        screen.fill(color=(0, 73, 48))

        # Draw the scene
        draw_object(screen, config.get_rect_obs_list(), config.get_poly_obs_list())
        time_size = 30
        Pencil.write_text(screen, "%02d:%02d:%02d" % (timer.get_hour(), timer.get_minute(), timer.get_second()),
                          [(SCREEN_WIDTH - time_size * 6) * scale, 20 * scale], font_size=time_size,
                          color=(230, 230, 230))

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
        tick_elapsed += time.time() - since
        if tick_elapsed >= 1:
            timer.elapse_one_second()
            print("%02d:%02d:%02d" % (timer.get_hour(), timer.get_minute(), timer.get_second()), end=': ')
            print(citizen_group[0].state)
            tick_elapsed = 0

        trigger(timer, citizen_group, config)
        pygame.display.update()


if __name__ == '__main__':
    main()
