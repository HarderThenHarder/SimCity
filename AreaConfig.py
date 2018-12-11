from Area import RectArea
from Area import PolyArea


class AreaConfig:
    def __init__(self, scale):
        self.rect_area_list = []
        self.poly_area_list = []

    ######################################### rect area list ###########################################################

        # Create LIVING AREA BUILDING
        living_area = RectArea("LIVING AREA", pos=[20 * scale, 0], width_height=[400 * scale, 200 * scale],
                               color=(231, 121, 24))
        self.rect_area_list.append(living_area)

        # Create MARKET
        market = RectArea("MARKET", pos=[500 * scale, 550 * scale], width_height=[200 * scale, 200 * scale],
                          color=(220, 35, 80))
        self.rect_area_list.append(market)

        # Create River
        river = RectArea("", pos=[0, 800 * scale], width_height=[1920 * scale, 100 * scale],
                         color=(141, 178, 238))
        self.rect_area_list.append(river)

        # Create road
        self.road_list = []
        road1 = RectArea("", pos=[0, 0], width_height=[20 * scale, 800 * scale],
                         color=(130, 130, 130))
        self.road_list.append(road1)
        road2 = RectArea("", pos=[0, 750 * scale], width_height=[1920 * scale, 50 * scale],
                         color=(130, 130, 130))
        self.road_list.append(road2)
        road3 = RectArea("", pos=[0, 200 * scale], width_height=[1920 * scale, 50 * scale],
                         color=(130, 130, 130))
        self.road_list.append(road3)
        road4 = RectArea("", pos=[420 * scale, 0], width_height=[50 * scale, 800 * scale],
                         color=(130, 130, 130))
        self.road_list.append(road4)

        for road in self.road_list:
            self.rect_area_list.append(road)

        # Create Subway
        subway = RectArea("", pos=[0, 220 * scale], width_height=[1920 * scale, 10 * scale],
                          color=(42, 0, 255))
        self.rect_area_list.append(subway)

    ####################################################################################################################

    ######################################### poly area list ###########################################################

        # Create lake
        lake_pos = ((700 * scale, 550 * scale), (750 * scale, 450 * scale), (850 * scale, 450 * scale),
                    (850 * scale, 550 * scale), (700 * scale, 550 * scale))
        lake = PolyArea("LAKE", lake_pos, color=(141, 178, 238))
        self.poly_area_list.append(lake)






    def get_rect_obs_list(self):
        return self.rect_area_list

    def get_poly_obs_list(self):
        return self.poly_area_list
