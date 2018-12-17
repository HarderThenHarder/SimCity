"""
@author: P_k_y
"""
from CitizenByFloyd import CitizenByFloyd


class CitizenConfig:
    def __init__(self, scale, area_config, city_map):
        self.citizen_list = []

        # ----- Create Person by residence -----
        for i in range(50):
            citizen = CitizenByFloyd([220 * scale, 100 * scale], city_map, "walk_in_area", area_config.living_area)
            self.citizen_list.append(citizen)
        for i in range(50):
            citizen = CitizenByFloyd([1750 * scale, 100 * scale], city_map, "walk_in_area", area_config.living_area2)
            self.citizen_list.append(citizen)

        #  ----- Give occupation to them -----
        # 20 Programmers which index [ 0 ~ 9 + 50 ~ 59]
        self.set_occupation("programmer", area_config.it_building, [0, 10], [49, 59])
        # 30 Accountants which index [ 10 ~ 24 + 60 ~ 74]
        self.set_occupation("accountant", area_config.financial_tower, [10, 25], [59, 74])
        # 20 Embedded Engineers which index [25 ~ 34 + 75 ~ 84]
        self.set_occupation("embedded engineer", area_config.high_technology, [25, 35], [75, 85])
        # 5 Natural park staff which index [35 ~ 37 + 85 ~ 86]
        self.set_occupation("natural park staff", area_config.natural_park, [35, 38], [85, 87])
        # 10 Market staff which index [38 ~ 42 + 87 ~ 91]
        self.set_occupation("market staff", area_config.market, [38, 43], [87, 92])
        # 3 Coffee staff which index [43 ~ 43, 92 ~ 93]
        self.set_occupation("coffee staff", area_config.coffee, [43, 44], [92, 94])
        # 3 Bar staff which index [44 ~ 44 + 94 ~ 95]
        self.set_occupation("bar staff", area_config.bar, [44, 45], [94, 96])
        # 3 Library staff which index [45 ~ 45 + 96 ~ 97]
        self.set_occupation("library staff", area_config.library, [45, 46], [96, 98])
        # 4 Restaurant staff which index [46 ~ 47 + 98 ~ 99]
        self.set_occupation("restaurant staff", area_config.restaurant, [46, 48], [98, 100])
        # 2 Cinema staff which index [48 ~ 49 + None]
        self.set_occupation("cinema staff", area_config.cinema, [48, 50], [])

    def find_citizen_by_occupation(self, occupation_name):
        result_list = []
        for citizen in self.citizen_list:
            if citizen.occupation_name == occupation_name:
                result_list.append(citizen)
        return result_list

    def find_citizen_by_residence(self, residence_name):
        result_list = []
        for citizen in self.citizen_list:
            if citizen.residence.get_name() == residence_name:
                result_list.append(citizen)
        return result_list

    def set_occupation(self, occupation_name, occupation_area, index_list_1, index_list_2):
        if index_list_1:
            citizen_live_in_1 = [i for i in range(index_list_1[0], index_list_1[1])]
        else:
            citizen_live_in_1 = []
        if index_list_2:
            citizen_live_in_2 = [i for i in range(index_list_2[0], index_list_2[1])]
        else:
            citizen_live_in_2 = []
        citizen_index = citizen_live_in_1 + citizen_live_in_2
        for i in range(len(citizen_index)):
            self.citizen_list[citizen_index[i]].set_occupation(occupation_name, occupation_area)



