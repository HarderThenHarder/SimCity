from Pencil import Pencil


class Pencil_for_SimCity:

    @staticmethod
    def create_building(screen, building_color, building_pos, building_name, name_size=30):
        Pencil.draw_rect(screen, building_pos, (0, 0, 0), width=3)
        Pencil.draw_rect(screen, (building_pos[0]+1, building_pos[1]+2, building_pos[2]-2, building_pos[3]-2),
                         building_color)
        Pencil.write_text(screen, building_name, font_pos=[building_pos[0] + 5, building_pos[1] + 5],
                          font_size=name_size)
