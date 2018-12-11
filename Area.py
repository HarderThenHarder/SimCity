class RectArea:
    def __init__(self, name, pos, width_height, color):
        self._name = name
        self._pos = pos
        self._width_height = width_height
        self._color = color

    def get_start_pos(self):
        return self._pos

    def get_end_pos(self):
        return [self._pos[0] + self._width_height[0], self._pos[1] + self._width_height[1]]

    def get_color(self):
        return self._color

    def get_rect(self):
        return self._pos[0], self._pos[1], self._width_height[0], self._width_height[1]

    def get_name(self):
        return self._name


class PolyArea:
    def __init__(self, name, pos_list, color):
        self._name = name
        self._pos_list = pos_list
        self._color = color

    def get_name(self):
        return self._name

    def get_color(self):
        return self._color

    def get_pos_list(self):
        return self._pos_list

