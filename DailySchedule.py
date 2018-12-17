"""
@author: P_k_y
"""
import random


class DailySchedule:
    def __init__(self, timer, area_config, citizen_config):
        self.timer = timer
        self.area_config = area_config
        self.citizen_config = citizen_config

    def trigger(self):
        second = self.timer.get_second()
        minute = self.timer.get_minute()
        hour = self.timer.get_hour()
        global lunch_time_for_programmer, lunch_time_for_embedded_engineer, lunch_time_for_accountant, random_time_in_7_8_one, shuffle_citizen_list, random_time_in_7_8_two, random_time_in_8_9_one, random_time_in_8_9_two
        building_area = self.area_config.get_building_area()

        if hour == 8 and minute == 0:
            for citizen in self.citizen_config.citizen_list:
                if citizen.occupation_area:
                    citizen.change_target(citizen.occupation_area)

        # -------------------- lunch time ---------------------------- #
        if hour == 11 and minute == 0:
            lunch_time_for_programmer = random.randint(0, 59)
            lunch_time_for_embedded_engineer = random.randint(0, 59)
            lunch_time_for_accountant = random.randint(0, 59)

        if hour == 11 and minute == lunch_time_for_programmer:
            lunch_list = self.citizen_config.find_citizen_by_occupation("programmer")
            for citizen in lunch_list:
                citizen.change_target(self.area_config.restaurant)

        if hour == 11 and minute == lunch_time_for_embedded_engineer:
            lunch_list = self.citizen_config.find_citizen_by_occupation("embedded engineer")
            for citizen in lunch_list:
                citizen.change_target(self.area_config.restaurant)

        if hour == 11 and minute == lunch_time_for_accountant:
            lunch_list = self.citizen_config.find_citizen_by_occupation("accountant")
            for citizen in lunch_list:
                citizen.change_target(self.area_config.restaurant)

        # lunch time is 1 hour
        if hour == 12 and minute == lunch_time_for_programmer:
            lunch_list = self.citizen_config.find_citizen_by_occupation("programmer")
            for citizen in lunch_list:
                citizen.change_target(self.area_config.it_building)

        if hour == 12 and minute == lunch_time_for_embedded_engineer:
            lunch_list = self.citizen_config.find_citizen_by_occupation("embedded engineer")
            for citizen in lunch_list:
                citizen.change_target(self.area_config.high_technology)

        if hour == 12 and minute == lunch_time_for_accountant:
            lunch_list = self.citizen_config.find_citizen_by_occupation("accountant")
            for citizen in lunch_list:
                citizen.change_target(self.area_config.financial_tower)
        # ---------------------------------------------------------- #

        # -------------------------- off duty ---------------------- #
        if hour == 18 and minute == 30:
            random_time_in_7_8_one = random.randint(0, 59)
            random_time_in_7_8_two = random.randint(0, 59)
            random_time_in_8_9_one = random.randint(0, 59)
            random_time_in_8_9_two = random.randint(0, 59)
            shuffle_citizen_list = self.citizen_config.citizen_list.copy()
            random.shuffle(shuffle_citizen_list)

        if hour == 19 and minute == random_time_in_7_8_one:
            for i in range(30):
                shuffle_citizen_list[i].change_target(self.area_config.market)

        if hour == 19 and minute == random_time_in_7_8_two:
            for i in range(30, 51):
                shuffle_citizen_list[i].change_target(self.area_config.market)

        if hour == 20 and minute == random_time_in_8_9_one:
            for i in range(51, 61):
                shuffle_citizen_list[i].change_target(self.area_config.cinema)

        if hour == 20 and minute == random_time_in_8_9_two:
            for i in range(61, 66):
                shuffle_citizen_list[i].change_target(self.area_config.cinema)
        # -------------------------------------------------------------- #

        # ------------------------ go home ---------------------------- #

        if hour == 22 and minute == 30:
            for citizen in self.citizen_config.citizen_list:
                citizen.change_target(citizen.residence)

