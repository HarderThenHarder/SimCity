"""
@author: P_k_y
"""


class DailySchedule:
    def __init__(self, timer, area_config, citizen_config):
        self.timer = timer
        self.area_config = area_config
        self.citizen_config = citizen_config

    def trigger(self):
        second = self.timer.get_second()
        minute = self.timer.get_minute()
        hour = self.timer.get_hour()

        if hour == 8 and minute == 0:
            for citizen in self.citizen_config.citizen_list:
                if citizen.occupation_area:
                    citizen.change_target(citizen.occupation_area)

        if hour == 19 and minute == 30:
            programmers = self.citizen_config.find_citizen_by_occupation("programmer")
            for programmer in programmers:
                programmer.change_target(programmer.occupation_area)

        # if hour == 19 and minute == 30:
        #     # for citizen in citizen_group_list[0]:
        #     #     citizen.change_target(config.coffee)
        #     #     citizen.update()
        #     for i in range(len(citizen_list) - 1):
        #         rand_target = randint(0, 12)
        #         citizen_list[i].change_target(area_config.rect_area_list[rand_target])
        #         citizen_list[i].update()

        # if hour == 19 and minute == 48:
        #     # for citizen in citizen_group_list[1]:
        #     #     citizen.change_target(config.library)
        #     #     citizen.update()
        #     for i in range(len(citizen_list) - 1):
        #         rand_target = randint(0, 12)
        #         citizen_list[i].change_target(config.rect_area_list[rand_target])
        #         citizen_list[i].update()
        #
        # if hour == 21 and minute == 0:
        #     for i in range(int(len(citizen_list[0]) / 3)):
        #         rand_target = randint(0, 12)
        #         citizen_list[0][i].change_target(config.rect_area_list[rand_target])
        #         citizen_list[0][i].update()
        #     for i in range(int(len(citizen_list[1]) / 3)):
        #         rand_target = randint(0, 12)
        #         citizen_list[1][i].change_target(config.rect_area_list[rand_target])
        #         citizen_list[1][i].update()
        #
        # if hour == 22 and minute == 0:
        #     for i in range(len(citizen_list[0])):
        #         citizen_list[0][i].change_target(config.living_area)
        #         citizen_list[0][i].update()
        #     for i in range(len(citizen_list[1])):
        #         citizen_list[1][i].change_target(config.living_area2)
        #         citizen_list[1][i].update()

