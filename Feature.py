__author__ = 'tian'

from EmailData import EmailData
from DataSet import DataSet

from collections import defaultdict
from math import ceil, log, log10


LOG_BASE = 2

class Feature:
    def __init__(self):
        self.labels = set()
        self.features = defaultdict(set)  # feature -> list of values
        pass

    def learn(self, email_data: EmailData):
        word_max_occur = defaultdict(int)
        for id, label, words in email_data.emails:
            self.labels.add(label)
            for word, count in words.items():
                word_max_occur[word] = max(word_max_occur[word], count)
        for word, count in word_max_occur.items():
            most = ceil(log(count, LOG_BASE)) + 1
            for _ in range(most + 1):
                self.features[word].add(_)

    def translate_email(self, email):
        _, label, words = email
        xs = dict()
        for word in self.features:
            xs[word] = 0
        for word, count in words.items():
            if word in self.features:
                if count > 0:
                    xs[word] = ceil(log(count, LOG_BASE)) + 1
        return xs, label

    def translate_email_data(self, email_data: EmailData):
        rv = DataSet()
        for email in email_data.emails:
            rv.add_data(self.translate_email(email))
        return rv

