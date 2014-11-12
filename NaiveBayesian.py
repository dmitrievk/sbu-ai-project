__author__ = 'tian'

from Feature import Feature

from collections import defaultdict

from math import log

SMOOTH = 0.1


class NaiveBayesian:
    def __init__(self):
        pass

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

    def smooth_ratio(self, d, key):
        single = 1.0 * d[key] if key in d else 0.0
        all = 1.0 * sum(d.values())
        num = len(d)
        return (single + SMOOTH) / (all + num * SMOOTH)

    def get_p_label(self, label):
        return self.smooth_ratio(self.count_label, label)

    def get_p_feature_value(self, feature_name, feature_value):
        d = defaultdict(int)
        for label in self.labels:
            if (label, feature_name) in self.count_label_feature:
                for feature_value, count in self.count_label_feature[(label, feature_name)].items():
                    d[feature_value] += count
        return self.smooth_ratio(d, feature_value)


    def get_p_label_feature_value(self, label, feature_name, feature_value):
        if (label, feature_name) not in self.count_label_feature:
            assert False
        # print(self.count_label_feature[(label, feature_name)], feature_value)
        return self.smooth_ratio(self.count_label_feature[(label, feature_name)], feature_value)

    def feature_selection(self):
        l = []
        for feature_name in self.features:
            v = 0.0

            for feature_value in self.features[feature_name]:
                for label in self.labels:
                    p_cross = self.get_p_label_feature_value(label, feature_name, feature_value)
                    p_feature = self.get_p_feature_value(feature_name, feature_value)
                    p_label = self.get_p_label(label)
                    # print(p_cross, p_feature, p_label)
                    v += p_cross * log(p_cross / (p_feature * p_label))
            l.append((v, feature_name))

        l.sort(key=lambda _: -_[0])

        self.good_features = set()
        for v, feature_name in l[:]:
            self.good_features.add(feature_name)

        max_weight = max([_[0] for _ in l])
        self.feature_weight = {}
        for v, feature_name in l[:]:
            self.feature_weight[feature_name] = v / max_weight

    def smooth_binomial(self, p, smooth):
        return (p + smooth) / ((p + smooth) + (1 - p + smooth))

    def test(self, X: dict):
        rv_label = {}
        for label in self.labels:
            v = log(self.get_p_label(label))
            for feature_name, feature_value in X.items():
                #if feature_value == 0:
                #    continue
                if feature_name not in self.good_features:
                    continue
                p = self.get_p_label_feature_value(label, feature_name, feature_value)
                #p = self.smooth_binomial(p, 0.01 * self.feature_weight[feature_name])
                v += log(p)
            rv_label[label] = v

        max_rv = max(rv_label.values())
        for label, rv in rv_label.items():
            if rv == max_rv:
                return label
        assert False