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
        global lunch_time_for_programmer, lunch_time_for_embedded_engineer, lunch_time_for_accountant
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
        # ----------------------------------------------------------#

        if hour == 17 and minute == 30:
            accounts = self.citizen_config.find_citizen_by_occupation("accountant")
            for account in accounts:
                account.change_target(account.residence)
