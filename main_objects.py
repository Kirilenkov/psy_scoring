import os
from datetime import datetime as dt


class Participant:

    def __init__(self, full_name, dob, filling_date):
        self.name = full_name
        self.dob = dob
        self.date = filling_date


class Scale:

    def __init__(self, name, items, band, keys):
        self.title = name
        self.quests = items
        self.band = band
        self.keys = keys

    def fill_answers(self):
        pass


if __name__ == '__main__':
    pass

