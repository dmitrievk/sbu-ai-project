__author__ = 'tian'

from Feature import Feature
from DataSet import DataSet

from collections import defaultdict

from math import log

SMOOTH = 1e-5


class SmoothUtils:
    @staticmethod
    def smooth_binomial(p, smooth):
        return (p + smooth) / ((p + smooth) + (1 - p + smooth))

    @staticmethod
    def smooth(value_list, value, smooth=SMOOTH):
        return (value + smooth) / (sum(value_list) + smooth * len(value_list))


class NaiveBayesian:
    def __init__(self):
        pass

    def learn(self, feature: Feature, data_set: DataSet):
        self.features = feature.features
        self.labels = feature.labels

        self.count_label = defaultdict(int)
        self.count_label_feature = {}

        for X, label in data_set.data_list:
            self.count_label[label] += 1
            for feature_name, feature_value in X.items():
                if (label, feature_name) not in self.count_label_feature:
                    self.count_label_feature[(label, feature_name)] = defaultdict(int)
                self.count_label_feature[(label, feature_name)][feature_value] += 1

    def get_p_label(self, label):
        return SmoothUtils.smooth(self.count_label.values(), self.count_label[label])

    def get_p_feature_value(self, feature_name, feature_value):
        d = defaultdict(int)
        for label in self.labels:
            if (label, feature_name) in self.count_label_feature:
                for feature_value, count in self.count_label_feature[(label, feature_name)].items():
                    d[feature_value] += count
        return SmoothUtils.smooth(d.values(), d[feature_value])

    def get_p_label_feature_value(self, label, feature_name, feature_value):
        if (label, feature_name) not in self.count_label_feature:
            assert False
        values = self.count_label_feature[(label, feature_name)].values()
        value = self.count_label_feature[(label, feature_name)][feature_value]
        return SmoothUtils.smooth(values, value)

    def test(self, xs: dict):
        rv_label = {}
        for label in self.labels:
            v = log(self.get_p_label(label))
            for feature_name, feature_value in xs.items():
                p = self.get_p_label_feature_value(label, feature_name, feature_value)
                v += log(p)
            rv_label[label] = v

        max_rv = max(rv_label.values())
        for label, rv in rv_label.items():
            if rv == max_rv:
                return label, rv_label
        assert False