from Pencil import Pencil


class PencilForSimCity:

    @staticmethod
    def draw_area(screen, building_color, building_pos, building_name, width=0, name_size=30, name_color=(0, 0, 0)):
        Pencil.draw_rect(screen, building_pos, building_color, width=width)
        Pencil.write_text(screen, building_name, font_pos=[building_pos[0] + 5, building_pos[1] + 5],
                          font_size=name_size, color=name_color)

    @staticmethod
    def draw_poly_area(screen, building_color, building_pos, building_name, width=0, name_size=30, name_color=(0, 0, 0)):
        Pencil.draw_poly_rect(screen, pointlist=building_pos, color=building_color, width=width)
        Pencil.write_text(screen, building_name, font_pos=[building_pos[0][0] + 5, building_pos[0][1] + 5],
                          font_size=name_size, color=name_color)
