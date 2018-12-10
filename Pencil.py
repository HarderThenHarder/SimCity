import pygame


class Pencil:

    @staticmethod
    def draw_line(screen, start_pos, end_pos, color=(0, 0, 0), width=1):
        pygame.draw.line(screen, color, start_pos, end_pos, width)

    @staticmethod
    def draw_rect(screen, rect, color=(0, 0, 0), width=0):
        """
        If width != 0, then the rect won't be filled, it will be stroked!

        """
        pygame.draw.rect(screen, color, rect, width)

    @staticmethod
    def draw_circle(screen, pos,  radius, color=(0, 0, 0), width=1):
        pygame.draw.circle(screen, color, pos, radius, width)

    @staticmethod
    def write_text(screen, content, font_pos, font_size=10, color=(0, 0, 0), font_family=None):
        my_font = pygame.font.Font(font_family, font_size)
        text_image = my_font.render(content, True, color)
        screen.blit(text_image, font_pos)
