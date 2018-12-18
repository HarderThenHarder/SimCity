import pygame
from pygame.locals import *
from sys import exit
from AreaConfig import AreaConfig
from DailySchedule import DailySchedule
from Pencil import Pencil
from PencilForSimCity import PencilForSimCity
import time
from SearchRoad import CityMap
from CitizenConfig import CitizenConfig
from Timer import Timer
from Scene import Scene

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 960
scale = 0.8
clock = pygame.time.Clock()


def draw_object(screen, rec_obs, poly_obs):
    for ob in rec_obs:
        PencilForSimCity.draw_area(screen, ob.get_color(), ob.get_rect(), ob.get_name(), name_size=int(25 * scale))


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
    timer.set_time(6, 59, 23)
    ticks = 0
    tick_elapsed = 0
    time_elapsed_speed = 1

    # Create Scene
    scene = Scene(timer, [SCREEN_WIDTH, SCREEN_HEIGHT])

    # Create City Map
    graph = area_config.get_city_map()
    node_list = graph[0]
    edge_list = graph[1]
    city_map = CityMap(node_list, edge_list)

    # Create citizen
    citizen_config = CitizenConfig(scale, area_config, city_map)

    # Create DailySchedule
    daily_schedule = DailySchedule(timer, area_config, citizen_config)

    while True:
        since = time.time()
        clock.tick(10)

        screen.fill(color=(0, 73, 48))

        # Draw the scene
        draw_object(screen, area_config.get_rect_obs_list(), area_config.get_poly_obs_list())
        time_size = int(38 * scale)
        # brightness canvas
        screen.blit(scene.brightness_canvas, (0, 0))
        # time
        Pencil.write_text(screen, "%02d:%02d" % (timer.get_hour(), timer.get_minute()),
                          [(SCREEN_WIDTH - time_size * 4) * scale, 20 * scale], font_size=time_size,
                          color=(230, 230, 230))
        # time_signal
        # PencilForSimCity.draw_sun(screen, [(SCREEN_WIDTH - time_size * 2) * scale, 90 * scale], scale)

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

        # Draw brightness canvas
        screen.blit(scene.brightness_canvas, (0, 0))

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

        daily_schedule.trigger()
        scene.update_brightness()
        pygame.display.update()


if __name__ == '__main__':
    main()
