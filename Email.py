__author__ = 'tian'


class Email:
    def __init__(self):
        self.emails = []  # list of tuple(a,b,c) where a is id, b is label and c is dict

    def clear(self):
        self.emails = []

    def load_from_file(self, filename:str):
        for line in open(filename):
            tokens = line.strip('\r\n').split()
            if len(tokens) < 2:
                continue
            i = tokens[0]
            label = tokens[1]
            d = dict()
            for i in range(2, len(tokens), 2):
                d[tokens[i]] = int(tokens[i + 1])
            self.emails.append((i, label, d))




