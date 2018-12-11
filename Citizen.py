"""
@author: P_k_y
"""
import pygame
import math
import random


class Citizen(pygame.sprite.Sprite):

    def __init__(self, initial_pos, target_pos, road_area, cross_list):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([7, 7])
        self.initial_pos = initial_pos
        self.pos = initial_pos
        self.speed = 3 + 2 * random.random()
        self.target_pos = target_pos
        self.road_area = road_area
        self.cross_list = cross_list
        self.not_reached_cross = True
        self.not_reached_target = True

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

    @staticmethod
    def get_nearest_cross(pos, cross_list):
        min_d = Citizen.distance(cross_list[0], pos)
        nearest_cross = cross_list[0]
        for cross in cross_list:
            if Citizen.distance(cross, pos) < min_d:
                min_d = Citizen.distance(cross, pos)
                nearest_cross = cross
        return nearest_cross

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

    def update(self, *args):
        if self.not_reached_cross:
            nearest_cross = self.get_nearest_cross(self.target_pos, self.cross_list)
            if self.go_target(nearest_cross):
                self.not_reached_cross = False
            return

        if self.not_reached_target:
            if self.go_target(self.target_pos):
                self.not_reached_target = False
