from Pencil import Pencil


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
