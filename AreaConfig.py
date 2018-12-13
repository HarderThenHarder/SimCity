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
        self.living_area = RectArea("LIVING AREA", pos=[0, 0], width_height=[400 * scale, 200 * scale],
                                    color=(192, 80, 70))
        self.living_area.add_entrance([200 * scale, 200 * scale])
        self.rect_area_list.append(self.living_area)

        # Create NATURAL PARK
        self.natural_park = RectArea("NATURAL PARK", pos=[420 * scale, 0], width_height=[980 * scale, 200 * scale],
                                     color=(171, 154, 192))
        self.natural_park.add_entrance([460 * scale, 200 * scale])
        self.rect_area_list.append(self.natural_park)

        # Create LIVING AREA2 BUILDING
        self.living_area2 = RectArea("LIVING AREA", pos=[1420 * scale, 0], width_height=[500 * scale, 200 * scale],
                                     color=(192, 80, 70))
        self.living_area2.add_entrance([1670 * scale, 200 * scale])
        self.rect_area_list.append(self.living_area2)

        # Create AMUSEMENT PARK
        self.amusement_park = RectArea("AMUSEMENT PARK", pos=[0, 220 * scale], width_height=[400 * scale, 250 * scale],
                                       color=(0, 176, 106))
        self.amusement_park.add_entrance([200 * scale, 220 * scale])
        self.rect_area_list.append(self.amusement_park)

        # Create MARKET
        self.market = RectArea("MARKET", pos=[420 * scale, 220 * scale], width_height=[980 * scale, 250 * scale],
                               color=(245, 157, 86))
        self.market.add_entrance([460 * scale, 220 * scale])
        self.rect_area_list.append(self.market)

        # Create FINANCIAL TOWER
        self.financial_tower = RectArea("FINANCIAL TOWER", pos=[1420 * scale, 220 * scale],
                                        width_height=[250 * scale, 400 * scale],
                                        color=(215, 227, 191))
        self.financial_tower.add_entrance([1520 * scale, 220 * scale])
        self.rect_area_list.append(self.financial_tower)

        # Create HIGH-TECHNOLOGY
        self.high_technology = RectArea("HIGH-TECHNOLOGY", pos=[1670 * scale, 220 * scale],
                                        width_height=[250 * scale, 200 * scale],
                                        color=(171, 154, 192))
        self.high_technology.add_entrance([1770 * scale, 220 * scale])
        self.rect_area_list.append(self.high_technology)

        # Create BAR
        self.bar = RectArea("BAR", pos=[0, 470 * scale], width_height=[200 * scale, 150 * scale],
                            color=(127, 127, 127))
        self.bar.add_entrance([100 * scale, 620 * scale])
        self.rect_area_list.append(self.bar)

        # Create COFFEE
        self.coffee = RectArea("COFFEE", pos=[200 * scale, 470 * scale], width_height=[200 * scale, 150 * scale],
                               color=(127, 96, 0))
        self.coffee.add_entrance([300 * scale, 620 * scale])
        self.rect_area_list.append(self.coffee)

        # Create LIBRARY
        self.library = RectArea("LIBRARY", pos=[420 * scale, 470 * scale], width_height=[380 * scale, 150 * scale],
                                color=(255, 192, 0))
        self.library.add_entrance([610 * scale, 620 * scale])
        self.rect_area_list.append(self.library)

        # Create RESTAURANT
        self.restaurant = RectArea("RESTAURANT", pos=[800 * scale, 470 * scale],
                                   width_height=[380 * scale, 150 * scale],
                                   color=(204, 194, 217))
        self.restaurant.add_entrance([850 * scale, 620 * scale])
        self.rect_area_list.append(self.restaurant)

        # Create CINEMA
        self.cinema = RectArea("CINEMA", pos=[1100 * scale, 470 * scale], width_height=[300 * scale, 150 * scale],
                               color=(157, 187, 97))
        self.cinema.add_entrance([1250 * scale, 620 * scale])
        self.rect_area_list.append(self.cinema)

        # Create IT-BUILDING
        self.it_building = RectArea("IT-BUILDING", pos=[1670 * scale, 420 * scale],
                                    width_height=[250 * scale, 200 * scale],
                                    color=(255, 192, 97))
        self.it_building.add_entrance([1770 * scale, 620 * scale])
        self.rect_area_list.append(self.it_building)

        # Create UNDEVELOPED-AREA
        self.undeveloped_area1 = RectArea("UNDEVELOPED AREA...", pos=[0 * scale, 760 * scale],
                                          width_height=[400 * scale, 200 * scale],
                                          color=(0, 73, 48))
        self.rect_area_list.append(self.undeveloped_area1)

        # Create UNDEVELOPED-AREA
        self.undeveloped_area2 = RectArea("UNDEVELOPED AREA...", pos=[420 * scale, 760 * scale],
                                          width_height=[980 * scale, 200 * scale],
                                          color=(0, 73, 48))
        self.rect_area_list.append(self.undeveloped_area2)

        # Create UNDEVELOPED-AREA
        self.undeveloped_area3 = RectArea("UNDEVELOPED AREA...", pos=[1420 * scale, 760 * scale],
                                          width_height=[500 * scale, 200 * scale],
                                          color=(0, 73, 48))
        self.rect_area_list.append(self.undeveloped_area3)

        # Create RIVER
        self.river = RectArea("RIVER", pos=[0 * scale, 640 * scale], width_height=[1920 * scale, 100 * scale],
                              color=(75, 172, 198))
        self.rect_area_list.append(self.river)

        # Create road
        # horizon road
        self.road_list = []
        road1 = RectArea("", pos=[0, 200 * scale], width_height=[1920 * scale, 20 * scale],
                         color=(180, 180, 180))
        self.road_list.append(road1)
        road2 = RectArea("", pos=[0, 620 * scale], width_height=[1920 * scale, 20 * scale],
                         color=(180, 180, 180))
        self.road_list.append(road2)
        road3 = RectArea("", pos=[0, 740 * scale], width_height=[1920 * scale, 20 * scale],
                         color=(180, 180, 180))
        self.road_list.append(road3)
        # vertical Road
        road4 = RectArea("", pos=[400 * scale, 0], width_height=[20 * scale, 640 * scale],
                         color=(180, 180, 180))
        self.road_list.append(road4)
        road5 = RectArea("", pos=[1400 * scale, 0], width_height=[20 * scale, 640 * scale],
                         color=(180, 180, 180))
        self.road_list.append(road5)
        road6 = RectArea("", pos=[400 * scale, 740 * scale], width_height=[20 * scale, 220 * scale],
                         color=(180, 180, 180))
        self.road_list.append(road6)
        road7 = RectArea("", pos=[1400 * scale, 740 * scale], width_height=[20 * scale, 220 * scale],
                         color=(180, 180, 180))
        self.road_list.append(road7)

        for road in self.road_list:
            self.rect_area_list.append(road)

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
