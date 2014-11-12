__author__ = 'tian'

from Feature import Feature

from collections import defaultdict

from math import log

SMOOTH = 0.1


class NaiveBayesian:
    def __init__(self):
        self.features = None

    def learn(self, feature: Feature, data_set):
        self.features = feature.features
        self.labels = feature.labels

        self.count_label = defaultdict(int)
        self.count_label_feature = {}

        for X, label in data_set:
            self.count_label[label] += 1
            for feature_name, feature_value in X.items():
                if (label, feature_name) not in self.count_label_feature:
                    self.count_label_feature[(label, feature_name)] = defaultdict(int)
                self.count_label_feature[(label, feature_name)][feature_value] += 1

    def get_p_label(self, label):
        return 1.0 * self.count_label[label] / sum(self.count_label.values())

    def smooth_ratio(self, d, key):
        single = 1.0 * d[key] if key in d else 0.0
        all = 1.0 * sum(d.values())
        num = len(d)
        return (single + SMOOTH) / (all + num * SMOOTH)

    def get_p_label_feature_value(self, label, feature_name, feature_value):
        if (label, feature_name) not in self.count_label_feature:
            assert False
        return self.smooth_ratio(self.count_label_feature[(label, feature_name)], feature_value)

    def test(self, X: dict):
        rv_label = {}
        for label in self.labels:
            v = log(self.get_p_label(label))
            for feature_name, feature_value in X.items():
                p = self.get_p_label_feature_value(label, feature_name, feature_value)
                v += log(p)
            rv_label[label] = v

        max_rv = max(rv_label.values())
        for label, rv in rv_label.items():
            if rv == max_rv:
                return label
        assert False