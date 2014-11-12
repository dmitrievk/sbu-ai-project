__author__ = 'tian'

from EmailData import EmailData

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

    def translate_email(self, email):
        id, label, words = email
        rv = dict()
        for word, count in words.items():
            if count > 0 and word in self.features:
                rv[word] = 0
        return rv, label

    def translate_email_data(self, email_data: EmailData):
        rv = []
        for email in email_data.emails:
            rv.append(self.translate_email(email))
        return rv

