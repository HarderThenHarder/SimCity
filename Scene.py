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
        self.period = ""

    def update(self):
        minute = self.timer.get_minute()
        hour = self.timer.get_hour()

        # update brightness and Period
        if 7 <= hour <= 8:
            brightness = 120
            brightness -= ((hour - 7) * 60 + minute)
            self.brightness_canvas.set_alpha(brightness)
            self.period = "sunrise"

        elif 18 <= hour <= 19:
            brightness = 0
            brightness += (hour - 18) * 60 + minute
            self.brightness_canvas.set_alpha(brightness)
            self.period = "sunset"

        # update rest Period
        elif 0 <= hour < 7 or 20 <= hour < 24:
            self.period = "night"

        elif 9 <= hour < 12:
            self.period = "morning"

        elif 12 <= hour < 13:
            self.period = "noon"

        elif 13 <= hour < 18:
            self.period = "afternoon"

        elif 20 <= hour < 12:
            self.period = "morning"
