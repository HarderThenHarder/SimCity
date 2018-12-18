"""
@author: P_k_y
"""
import pygame


class Scene:
    def __init__(self, timer, screen_width_height_list):
        self.timer = timer
        self.brightness_canvas = pygame.Surface(screen_width_height_list)
        self.brightness_canvas.fill(color=(0, 0, 0))
        self.brightness_canvas.set_alpha(0)

    def update_brightness(self):
        minute = self.timer.get_minute()
        hour = self.timer.get_hour()

        if 7 <= hour <= 8:
            brightness = 120
            brightness -= ((hour - 7) * 60 + minute)
            self.brightness_canvas.set_alpha(brightness)

        if 18 <= hour <= 19:
            brightness = 0
            brightness += (hour - 18) * 60 + minute
            self.brightness_canvas.set_alpha(brightness)
