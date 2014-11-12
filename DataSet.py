__author__ = 'tian'


class DataSet:
    def __init__(self):
        self.data_list = []

    def clear(self):
        self.data_list = []

    def add_data(self, data):
        self.data_list.append(data)

