__author__ = 'tian'

from EmailData import EmailData
from DataSet import DataSet

from collections import defaultdict


class Feature:
    def __init__(self):
        self.labels = set()
        self.features = defaultdict(set)  # feature -> list of values
        pass

    def learn(self, email_data: EmailData):
        for id, label, words in email_data.emails:
            self.labels.add(label)
            for word in words:
                self.features[word].add(0)
                self.features[word].add(1)
                self.features[word].add(2)

    def translate_email(self, email):
        _, label, words = email
        xs = dict()
        for word in self.features:
            xs[word] = 0
        for word, count in words.items():
            if word in self.features:
                if count > 0:
                    if count <= 3:
                        xs[word] = 1
                    else:
                        xs[word] = 2
        return xs, label

    def translate_email_data(self, email_data: EmailData):
        rv = DataSet()
        for email in email_data.emails:
            rv.add_data(self.translate_email(email))
        return rv

