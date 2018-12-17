import pygame
from pygame.locals import *
from sys import exit
from AreaConfig import AreaConfig
from Pencil import Pencil
from PencilForSimCity import PencilForSimCity
import time
from SearchRoad import CityMap
from CitizenConfig import CitizenConfig
from Timer import Timer

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 960
scale = 0.8
clock = pygame.time.Clock()


def draw_object(screen, rec_obs, poly_obs):
    for ob in rec_obs:
        PencilForSimCity.draw_area(screen, ob.get_color(), ob.get_rect(), ob.get_name(), name_size=int(25 * scale))


def trigger(timer, area_config, citizen_config):
    second = timer.get_second()
    minute = timer.get_minute()
    hour = timer.get_hour()

    if hour == 19 and minute == 30:
        programmers = citizen_config.find_citizen_by_residence("LIVING AREA 2")
        for programmer in programmers:
            programmer.change_target(area_config.it_building)

    # if hour == 19 and minute == 30:
    #     # for citizen in citizen_group_list[0]:
    #     #     citizen.change_target(config.coffee)
    #     #     citizen.update()
    #     for i in range(len(citizen_list) - 1):
    #         rand_target = randint(0, 12)
    #         citizen_list[i].change_target(area_config.rect_area_list[rand_target])
    #         citizen_list[i].update()

    # if hour == 19 and minute == 48:
    #     # for citizen in citizen_group_list[1]:
    #     #     citizen.change_target(config.library)
    #     #     citizen.update()
    #     for i in range(len(citizen_list) - 1):
    #         rand_target = randint(0, 12)
    #         citizen_list[i].change_target(config.rect_area_list[rand_target])
    #         citizen_list[i].update()
    #
    # if hour == 21 and minute == 0:
    #     for i in range(int(len(citizen_list[0]) / 3)):
    #         rand_target = randint(0, 12)
    #         citizen_list[0][i].change_target(config.rect_area_list[rand_target])
    #         citizen_list[0][i].update()
    #     for i in range(int(len(citizen_list[1]) / 3)):
    #         rand_target = randint(0, 12)
    #         citizen_list[1][i].change_target(config.rect_area_list[rand_target])
    #         citizen_list[1][i].update()
    #
    # if hour == 22 and minute == 0:
    #     for i in range(len(citizen_list[0])):
    #         citizen_list[0][i].change_target(config.living_area)
    #         citizen_list[0][i].update()
    #     for i in range(len(citizen_list[1])):
    #         citizen_list[1][i].change_target(config.living_area2)
    #         citizen_list[1][i].update()


def main():
    pygame.init()

    # Set title bar
    pygame.display.set_caption("SimCity v1.0")
    screen = pygame.display.set_mode([int(SCREEN_WIDTH * scale), int(SCREEN_HEIGHT * scale)])
    icon = pygame.image.load("img/icon.png")
    pygame.display.set_icon(icon)

    # Set constance value
    area_config = AreaConfig(scale)
    timer = Timer()
    timer.set_time(19, 28, 23)
    ticks = 0
    tick_elapsed = 0
    time_elapsed_speed = 1

    # Create City Map
    graph = area_config.get_city_map()
    node_list = graph[0]
    edge_list = graph[1]
    city_map = CityMap(node_list, edge_list)

    # Create citizen
    citizen_config = CitizenConfig(scale, area_config, city_map)

    while True:
        since = time.time()
        clock.tick(10)

        # screen.blit(background, (0, 0))
        screen.fill(color=(0, 73, 48))

        # Draw the scene
        draw_object(screen, area_config.get_rect_obs_list(), area_config.get_poly_obs_list())
        time_size = int(38 * scale)
        Pencil.write_text(screen, "%02d:%02d" % (timer.get_hour(), timer.get_minute()),
                          [(SCREEN_WIDTH - time_size * 4) * scale, 20 * scale], font_size=time_size,
                          color=(230, 230, 230))

        # Draw citizen
        for citizen in citizen_config.citizen_list:
            screen.blit(citizen.image, citizen.pos)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    time_elapsed_speed = 2
                elif event.key == K_DOWN:
                    time_elapsed_speed = 1

        if ticks % int(2 / time_elapsed_speed) == 0:
            for citizen in citizen_config.citizen_list:
                citizen.update()

        ticks += 1
        tick_elapsed += time.time() - since
        if tick_elapsed >= (1 / time_elapsed_speed):
            timer.elapse_one_minute()
            print("%02d:%02d" % (timer.get_hour(), timer.get_minute()), end=': ')
            print(citizen_config.citizen_list[0].state)
            tick_elapsed = 0

        trigger(timer, area_config, citizen_config)
        pygame.display.update()


if __name__ == '__main__':
    main()
