"""
@author: P_k_y
"""
import pygame
from random import random, randint
import math
from SearchRoad import CityMap


class CitizenByFloyd(pygame.sprite.Sprite):
    def __init__(self, initial_pos, target_area, state, road_area, cross_list, city_map, in_which_area=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([7, 7])
        self.initial_pos = initial_pos
        self.pos = initial_pos
        self.speed = 5 + 2 * random()
        self.target_area = target_area
        self.in_which_area = in_which_area
        self.road_area = road_area
        self.cross_list = cross_list
        self.state = state
        self.city_map = city_map
        self.path_node_list = []
        self.node_has_arrived = 0

    @staticmethod
    def distance(pos1, pos2):
        return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

    @staticmethod
    def is_in_road(pos1, road_list):
        flag = False
        for road_point in road_list:
            if road_point[0][0] <= pos1[0] <= road_point[1][0] and road_point[0][1] <= pos1[1] <= road_point[1][1]:
                flag = True
        return flag

    def change_target(self, target_area):
        if self.state == "walk_in_area":
            self.state = "walk_out_area"
        elif self.state != "walk_out_area":
            self.state = "to_target"
        self.target_area = target_area

    def go_target_in_building(self, target_pos):
        # x_offset calculate
        if target_pos[0] != self.pos[0]:
            x_direction = (target_pos[0] - self.pos[0]) / abs(target_pos[0] - self.pos[0])
        else:
            x_direction = 0
        self.pos[0] += x_direction * self.speed

        # y_offset calculate
        if target_pos[1] != self.pos[1]:
            y_direction = (target_pos[1] - self.pos[1]) / abs(target_pos[1] - self.pos[1])
        else:
            y_direction = 0
        self.pos[1] += y_direction * self.speed

    def walk_in_target(self):
        start_pos = self.in_which_area.get_start_pos()
        end_pos = self.in_which_area.get_end_pos()
        rand_pos = [randint(start_pos[0], end_pos[0] + 1), randint(start_pos[1], end_pos[1] + 1)]
        self.go_target_in_building(rand_pos)

    def walk_out_target(self):
        self.go_target_in_building(self.in_which_area.get_entrance())
        if self.is_in_road(self.pos, self.road_area):
            self.state = "to_target"

    def go_target(self, target_pos):
        # x_offset calculate
        if target_pos[0] != self.pos[0]:
            x_direction = (target_pos[0] - self.pos[0]) / abs(target_pos[0] - self.pos[0])
        else:
            x_direction = 0
        if self.is_in_road([self.pos[0] + x_direction * self.speed, self.pos[1]], self.road_area):
            self.pos[0] += x_direction * self.speed

        # y_offset calculate
        if target_pos[1] != self.pos[1]:
            y_direction = (target_pos[1] - self.pos[1]) / abs(target_pos[1] - self.pos[1])
        else:
            y_direction = 0
        if self.is_in_road([self.pos[0], self.pos[1] + y_direction * self.speed], self.road_area):
            self.pos[1] += y_direction * self.speed

        # judge reached
        if self.distance(self.pos, target_pos) < self.speed:
            return True
        return False

    def on_way_in_path_list(self):
        self.city_map.find_path(CityMap.find_node_by_name("BAR", self.city_map.node_list),
                                CityMap.find_node_by_name("HIGH-TECHNOLOGY", self.city_map.node_list), self.path_node_list)
        path_list = [node.pos for node in self.path_node_list]

        if self.node_has_arrived == len(path_list) - 1:
            self.state = "walk_in_area"
        else:
            tmp_target = path_list[self.node_has_arrived]
            if self.go_target(tmp_target):
                self.node_has_arrived += 1

    def update(self, *args):
        if self.state == "walk_out_area":
            self.walk_out_target()
            return

        if self.state == "to_target":
            self.on_way_in_path_list()
            return

        if self.state == "walk_in_area":
            self.walk_in_target()
