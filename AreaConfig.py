from Area import RectArea, PolyArea, Cross


class Node:
    def __init__(self, pos, name):
        self.pos = pos
        self.name = name


class Edge:
    def __init__(self, nodeA, nodeB):
        self.nodeA = nodeA
        self.nodeB = nodeB


class AreaConfig:
    def __init__(self, scale):
        self.rect_area_list = []
        self.poly_area_list = []
        self.road_area = []
        self.cross_node_list = []

        crossA = Cross([420 * scale, 220 * scale], "A")
        self.cross_node_list.append(crossA)
        crossB = Cross([1420 * scale, 220 * scale], "B")
        self.cross_node_list.append(crossB)
        crossC = Cross([420 * scale, 620 * scale], "C")
        self.cross_node_list.append(crossC)
        crossD = Cross([1420 * scale, 620 * scale], "D")
        self.cross_node_list.append(crossD)

        self.cross_list = [crossA.get_pos(), crossB.get_pos(), crossC.get_pos(), crossD.get_pos()]

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
        self.living_area2 = RectArea("LIVING AREA 2", pos=[1420 * scale, 0], width_height=[500 * scale, 200 * scale],
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
                                   color=(152, 121, 100))
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

    def find_node_by_name(self, name, node_list):
        for node in node_list:
            if node.name == name:
                return node

    def get_city_map(self):
        node_list = []
        for rect_area in self.rect_area_list:
            # 只加入有entrance的建筑物，river和road排除掉
            if rect_area.get_entrance():
                tmp_node = Node(rect_area.get_entrance(), rect_area.get_name())
                node_list.append(tmp_node)
        for cross in self.cross_node_list:
            tmp_node = Node(cross.get_pos(), cross.get_name())
            node_list.append(tmp_node)

        edge_list = []
        edge1 = Edge(self.find_node_by_name("LIVING AREA", node_list), self.find_node_by_name("A", node_list))
        edge_list.append(edge1)
        edge2 = Edge(self.find_node_by_name("A", node_list), self.find_node_by_name("NATURAL PARK", node_list))
        edge_list.append(edge2)
        edge3 = Edge(self.find_node_by_name("NATURAL PARK", node_list), self.find_node_by_name("B", node_list))
        edge_list.append(edge3)
        edge4 = Edge(self.find_node_by_name("B", node_list), self.find_node_by_name("LIVING AREA 2", node_list))
        edge_list.append(edge4)
        edge5 = Edge(self.find_node_by_name("AMUSEMENT PARK", node_list), self.find_node_by_name("A", node_list))
        edge_list.append(edge5)
        edge6 = Edge(self.find_node_by_name("NATURAL PARK", node_list), self.find_node_by_name("MARKET", node_list))
        edge_list.append(edge6)
        edge7 = Edge(self.find_node_by_name("B", node_list), self.find_node_by_name("FINANCIAL TOWER", node_list))
        edge_list.append(edge7)
        edge8 = Edge(self.find_node_by_name("FINANCIAL TOWER", node_list), self.find_node_by_name("HIGH-TECHNOLOGY", node_list))
        edge_list.append(edge8)
        edge9 = Edge(self.find_node_by_name("A", node_list), self.find_node_by_name("C", node_list))
        edge_list.append(edge9)
        edge10 = Edge(self.find_node_by_name("C", node_list), self.find_node_by_name("COFFEE", node_list))
        edge_list.append(edge10)
        edge11 = Edge(self.find_node_by_name("COFFEE", node_list), self.find_node_by_name("BAR", node_list))
        edge_list.append(edge11)
        edge12 = Edge(self.find_node_by_name("C", node_list), self.find_node_by_name("LIBRARY", node_list))
        edge_list.append(edge12)
        edge13 = Edge(self.find_node_by_name("LIBRARY", node_list), self.find_node_by_name("RESTAURANT", node_list))
        edge_list.append(edge13)
        edge14 = Edge(self.find_node_by_name("RESTAURANT", node_list), self.find_node_by_name("CINEMA", node_list))
        edge_list.append(edge14)
        edge15 = Edge(self.find_node_by_name("CINEMA", node_list), self.find_node_by_name("D", node_list))
        edge_list.append(edge15)
        edge16 = Edge(self.find_node_by_name("D", node_list), self.find_node_by_name("B", node_list))
        edge_list.append(edge16)
        edge17 = Edge(self.find_node_by_name("D", node_list), self.find_node_by_name("IT-BUILDING", node_list))
        edge_list.append(edge17)

        # node_list = []
        #
        # for cross in self.cross_node_list:
        #     tmp_node = Node(cross.get_pos(), cross.get_name())
        #     node_list.append(tmp_node)
        # node_list.append(Node(self.financial_tower.get_entrance(), self.financial_tower.get_name()))
        # node_list.append(Node(self.coffee.get_entrance(), self.coffee.get_name()))
        #
        # edge_list = []
        #
        # edge1 = Edge(self.find_node_by_name("A", node_list), self.find_node_by_name("B", node_list))
        # edge_list.append(edge1)
        # edge2 = Edge(self.find_node_by_name("B", node_list), self.find_node_by_name("D", node_list))
        # edge_list.append(edge2)
        # edge3 = Edge(self.find_node_by_name("D", node_list), self.find_node_by_name("C", node_list))
        # edge_list.append(edge3)
        # edge4 = Edge(self.find_node_by_name("A", node_list), self.find_node_by_name("C", node_list))
        # edge_list.append(edge4)
        # edge5 = Edge(self.find_node_by_name("B", node_list), self.find_node_by_name("FINANCIAL TOWER", node_list))
        # edge_list.append(edge5)
        # edge6 = Edge(self.find_node_by_name("C", node_list), self.find_node_by_name("COFFEE", node_list))
        # edge_list.append(edge6)

        return node_list, edge_list
