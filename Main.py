__author__ = 'tian'

from EmailData import EmailData
from Feature import Feature
from NaiveBayesian import NaiveBayesian


def test(naive_bayesian, test_data_set):
    count_all = 0
    count_correct = 0

    for X, label in test_data_set:
        predict_label = naive_bayesian.test(X)
        if predict_label == label:
            count_correct += 1
        count_all += 1

    return 1 * count_correct / count_all


def main():
    train_email_data = EmailData()
    train_email_data.load_from_file('data/train')

    feature = Feature()
    feature.learn(train_email_data)
    train_data_set = feature.translate_email_data(train_email_data)

    #print(train_data_set)
    naive_bayesian = NaiveBayesian()
    naive_bayesian.learn(feature, train_data_set)

    test_email_data = EmailData()
    test_email_data.load_from_file('data/test')
    test_data_set = feature.translate_email_data(test_email_data)

    precession = test(naive_bayesian, test_data_set)
    print(precession)

    print(naive_bayesian.count_label_feature)


if __name__ == '__main__':
    main()