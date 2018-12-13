from Area import RectArea
from Area import PolyArea


class AreaConfig:
    def __init__(self, scale):
        self.rect_area_list = []
        self.poly_area_list = []
        self.road_area = []
        self.cross_list = [[0 * scale, 210 * scale], [440 * scale, 210 * scale], [1500 * scale, 210 * scale],
                           [0 * scale, 790 * scale], [440 * scale, 790 * scale], [1500 * scale, 790 * scale]]

        ######################################### rect area list #######################################################

        # Create LIVING AREA BUILDING
        self.living_area = RectArea("LIVING AREA", pos=[20 * scale, 0], width_height=[400 * scale, 200 * scale],
                                    color=(231, 121, 24))
        self.living_area.add_entrance([230 * scale, 200 * scale])
        self.rect_area_list.append(self.living_area)

        # Create MARKET
        self.market = RectArea("MARKET", pos=[440 * scale, 630 * scale], width_height=[300 * scale, 150 * scale],
                               color=(220, 35, 80))
        self.market.add_entrance([460 * scale, 780 * scale])
        self.rect_area_list.append(self.market)

        # Create RESTAURANT
        self.restaurant = RectArea("RESTAURANT", pos=[740 * scale, 630 * scale], width_height=[200 * scale, 160 * scale],
                                   color=(190, 190, 0))
        self.restaurant.add_entrance([770 * scale, 780 * scale])
        self.rect_area_list.append(self.restaurant)

        # Create River
        self.river = RectArea("", pos=[0, 800 * scale], width_height=[1920 * scale, 100 * scale],
                              color=(141, 178, 238))
        self.rect_area_list.append(self.river)

        # Create road
        self.road_list = []
        road1 = RectArea("", pos=[0, 0], width_height=[20 * scale, 800 * scale],
                         color=(130, 130, 130))
        self.road_list.append(road1)
        road2 = RectArea("", pos=[0, 780 * scale], width_height=[1920 * scale, 20 * scale],
                         color=(130, 130, 130))
        self.road_list.append(road2)
        road3 = RectArea("", pos=[0, 200 * scale], width_height=[1920 * scale, 40 * scale],
                         color=(130, 130, 130))
        self.road_list.append(road3)
        road4 = RectArea("", pos=[420 * scale, 0], width_height=[20 * scale, 800 * scale],
                         color=(130, 130, 130))
        self.road_list.append(road4)
        road5 = RectArea("", pos=[1500 * scale, 0], width_height=[20 * scale, 800 * scale],
                         color=(130, 130, 130))
        self.road_list.append(road5)

        for road in self.road_list:
            self.rect_area_list.append(road)

        # Create Subway
        subway = RectArea("", pos=[0, 210 * scale], width_height=[1920 * scale, 10 * scale],
                          color=(42, 0, 255))
        self.rect_area_list.append(subway)

        ################################################################################################################

        ######################################### poly area list #######################################################

        # Create lake
        lake_pos = ((600 * scale, 550 * scale), (550 * scale, 400 * scale), (800 * scale, 350 * scale),
                    (900 * scale, 330 * scale), (1000 * scale, 500 * scale), (700 * scale, 550 * scale))
        self.lake = PolyArea("", lake_pos, color=(141, 178, 238))
        # self.poly_area_list.append(self.lake)

    ####################################################################################################################

    def get_rect_obs_list(self):
        return self.rect_area_list

    def get_poly_obs_list(self):
        return self.poly_area_list

    def get_road_area(self):
        for road in self.road_list:
            self.road_area.append([road.get_start_pos(), road.get_end_pos()])
        return self.road_area

    def get_cross_list(self):
        return self.cross_list

    def get_building_area(self):
        return self.building_area
