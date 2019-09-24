from basic_structures.subroutines.vector_sum import vector_sum

class Schedule:
    'Actual representation of a schedule. formatted as a dictionary'
    default_schedule = {
        'Mon': [0,0,0,0,0,0,0],
        'Tue': [0,0,0,0,0,0,0],
        'Wen': [0,0,0,0,0,0,0],
        'Thu': [0,0,0,0,0,0,0],
        'Fri': [0,0,0,0,0,0,0],
        'Sat': [0,0,0,0,0,0,0]}

    def __init__(self, data = default_schedule):
        self.overlaps = 0
        self.data = data
        self.compute_overlaps()

    def compute_overlaps(self):
        self.overlaps = 0 # overlaps is reset to calculate new value
        for day in self.data:
            for block in range(7):
                if self.data[day][block] > 1:
                    self.overlaps += (self.data[day][block] - 1)
    
    def add_schedule(self, added_schedule):
        if self.data.keys() == added_schedule.data.keys():
            for day in self.data:
                if len(self.data[day]) == len(added_schedule.data[day]):
                    self.data[day] = vector_sum(self.data[day], added_schedule.data[day])

    def load_from_dict(self, schedule_dict):
        if self.data.keys() == schedule_dict.keys():
            self.data = schedule_dict
            self.compute_overlaps()

    def clear(self):
        self.data = {
        'Mon': [0,0,0,0,0,0,0],
        'Tue': [0,0,0,0,0,0,0],
        'Wen': [0,0,0,0,0,0,0],
        'Thu': [0,0,0,0,0,0,0],
        'Fri': [0,0,0,0,0,0,0],
        'Sat': [0,0,0,0,0,0,0]}

class Subject:
    'Actual representation of a subject.'
    def __init__(self, code, schedule_options):
        self.code = code # Ex: DEF101
        self.schedule_options = schedule_options # dictionary of Schedule objects with sections as keys

    def change_schedule_option(self, option, new_state):
        if (len(option.keys()) == 1):
            option_section = list(option.keys())[0]
            for section in self.schedule_options:
                if section == option_section:
                    if new_state == 1:
                        self.schedule_options[section] = option[section] # option[section] is a Schedule object
                    elif new_state == 0:
                        self.schedule_options.pop(section)
                    return
            if new_state == 1:
                self.schedule_options[option_section] = option[option_section]