from Pencil import Pencil
import math
import pygame


class PencilForSimCity:

    @staticmethod
    def draw_area(screen, building_color, building_pos, building_name, width=0, name_size=20, name_color=(0, 0, 0)):
        Pencil.draw_rect(screen, building_pos, building_color, width=width)
        name_length = len(building_name)
        Pencil.write_text(screen, building_name, font_pos=[building_pos[0] + building_pos[2] / 2 - (name_length / 2 * 0.6 * name_size),
                                                           building_pos[1] + building_pos[3] / 2 - name_size * 0.5],
                          font_size=name_size, color=name_color)

    @staticmethod
    def draw_poly_area(screen, building_color, building_pos, building_name, width=0, name_size=20, name_color=(0, 0, 0)):
        Pencil.draw_poly_rect(screen, pointlist=building_pos, color=building_color, width=width)
        Pencil.write_text(screen, building_name, font_pos=[building_pos[0][0] + 5, building_pos[0][1] + 5],
                          font_size=name_size, color=name_color)

    @staticmethod
    def draw_sun(screen, pos, scale):
        radians = int(15 * scale)
        color = (230, 230, 230)
        Pencil.draw_circle(screen, [int(pos[0]), int(pos[1])], radians, color)

        Pencil.draw_rect(screen, [pos[0] - 2, pos[1] - radians * 2 - 2, 4, radians], color)
        Pencil.draw_rect(screen, [pos[0] - 2, pos[1] + radians + 2, 4, radians], color)
        Pencil.draw_rect(screen, [pos[0] - radians * 2 - 2, pos[1] - 2, radians, 4], color)
        Pencil.draw_rect(screen, [pos[0] + radians + 2, pos[1] - 2, radians, 4], color)
        Pencil.draw_poly_rect(screen, color,
                              [[pos[0] - (2 * radians) // 4 * 3, pos[1] - (2 * radians) // 4 * 3],
                               [pos[0] - (2 * radians) // 4 * 1, pos[1] - (2 * radians) // 4 * 1],
                               [pos[0] - (2 * radians) // 4 * 1 - 2, pos[1] - (2 * radians) // 4 * 1 + 2],
                               [pos[0] - (2 * radians) // 4 * 3 - 2, pos[1] - (2 * radians) // 4 * 3 + 2]])
        Pencil.draw_poly_rect(screen, color,
                              [[pos[0] + (2 * radians) // 4 * 3, pos[1] - (2 * radians) // 4 * 3],
                               [pos[0] + (2 * radians) // 4 * 1, pos[1] - (2 * radians) // 4 * 1],
                               [pos[0] + (2 * radians) // 4 * 1 + 2, pos[1] - (2 * radians) // 4 * 1 + 2],
                               [pos[0] + (2 * radians) // 4 * 3 + 2, pos[1] - (2 * radians) // 4 * 3 + 2]])
        Pencil.draw_poly_rect(screen, color,
                              [[pos[0] - (2 * radians) // 4 * 3, pos[1] + (2 * radians) // 4 * 3],
                               [pos[0] - (2 * radians) // 4 * 1, pos[1] + (2 * radians) // 4 * 1],
                               [pos[0] - (2 * radians) // 4 * 1 - 2, pos[1] + (2 * radians) // 4 * 1 - 2],
                               [pos[0] - (2 * radians) // 4 * 3 - 2, pos[1] + (2 * radians) // 4 * 3 - 2]])
        Pencil.draw_poly_rect(screen, color,
                              [[pos[0] + (2 * radians) // 4 * 3, pos[1] + (2 * radians) // 4 * 3],
                               [pos[0] + (2 * radians) // 4 * 1, pos[1] + (2 * radians) // 4 * 1],
                               [pos[0] + (2 * radians) // 4 * 1 + 2, pos[1] + (2 * radians) // 4 * 1 - 2],
                               [pos[0] + (2 * radians) // 4 * 3 + 2, pos[1] + (2 * radians) // 4 * 3 - 2]])

