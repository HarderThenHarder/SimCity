"""
@author: P_k_y
"""
import pygame
from random import random, randint
from SearchRoad import CityMap
from MathUtility import MathUtility


class CitizenByFloyd(pygame.sprite.Sprite):
    def __init__(self, initial_pos, city_map, state, residence=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([5, 5])
        self.initial_pos = initial_pos
        self.pos = initial_pos
        self.speed = 3 + 2 * random()
        self.target_area = residence
        self.path_list = []
        self.city_map = city_map
        self.node_has_arrived = 0
        self.state = state
        self.occupation = None
        self.residence = residence
        self.in_which_target = residence

    def set_occupation(self, occupation):
        self.occupation = occupation

    def go_target(self, target_pos):
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

        # judge reached
        if MathUtility.distance(self.pos, target_pos) < self.speed:
            return True
        return False

    def set_path_list(self):
        path_node_list = []
        self.city_map.find_path(CityMap.find_node_by_name(self.in_which_target.get_name(), self.city_map.node_list),
                                CityMap.find_node_by_name(self.target_area.get_name(), self.city_map.node_list), path_node_list)
        self.path_list = [node.pos for node in path_node_list]
        self.path_list.append(self.target_area.get_entrance())

    def go_target_in_path(self):
        if self.node_has_arrived == len(self.path_list):
            self.in_which_target = self.target_area
            self.state = "walk_in_area"
            return
        tmp_target = self.path_list[self.node_has_arrived]
        if self.go_target(tmp_target):
            self.node_has_arrived += 1

    def change_target(self, target):
        if self.state == "walk_in_area":
            self.state = "walk_out_area"
        elif self.state != "walk_out_area":
            self.state = "to_target"
        self.target_area = target
        self.set_path_list()
        self.node_has_arrived = 0

    def walk_in_area(self):
        start_pos = self.in_which_target.get_start_pos()
        end_pos = self.in_which_target.get_end_pos()
        rand_pos = [randint(start_pos[0], end_pos[0] + 1), randint(start_pos[1], end_pos[1] + 1)]
        self.go_target(rand_pos)

    def walk_out_area(self):
        if self.go_target(self.in_which_target.get_entrance()):
            self.state = "to_target"

    def update(self, *args):
        if self.state == "to_target":
            self.go_target_in_path()
        if self.state == "walk_in_area":
            self.walk_in_area()
        if self.state == "walk_out_area":
            self.walk_out_area()
