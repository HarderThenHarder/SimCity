"""
@author: P_k_y
"""
from CitizenByFloyd import CitizenByFloyd


class CitizenConfig:
    def __init__(self, scale, config, city_map):
        self.citizen_list = []

        # Create Person by residence
        for i in range(50):
            citizen = CitizenByFloyd([220 * scale, 100 * scale], city_map, "walk_in_area", residence=config.living_area)
            self.citizen_list.append(citizen)
        for i in range(50):
            citizen = CitizenByFloyd([1750 * scale, 100 * scale], city_map, "walk_in_area", residence=config.living_area2)
            self.citizen_list.append(citizen)

        # Give occupation to them
        # 20 Programmers which index [ 0 ~ 9 + 49 ~ 58]
        programmer_live_in_1 = [i for i in range(10)]
        programmer_live_in_2 = [i for i in range(49, 59)]
        programmer_index = programmer_live_in_1 + programmer_live_in_2
        for i in range(len(programmer_index)):
            self.citizen_list[programmer_index[i]].set_occupation("programmer")


    def find_citizen_by_occupation(self, occupation_name):
        result_list = []
        for citizen in self.citizen_list:
            if citizen.occupation == occupation_name:
                result_list.append(citizen)
        return result_list

    def find_citizen_by_residence(self, residence_name):
        result_list = []
        for citizen in self.citizen_list:
            if citizen.residence.get_name() == residence_name:
                result_list.append(citizen)
        return result_list



