__author__ = 'tian'

from EmailData import EmailData
from Feature import Feature
from NaiveBayesian import NaiveBayesian

from collections import defaultdict


def get_precision_and_recall(tp, fp, fn, tn):
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    return precision, recall


def test(naive_bayesian, test_data_set):
    test_counter = defaultdict(int)

    for xs, label in test_data_set.data_list:
        predict_label, rv_label = naive_bayesian.test(xs)
        test_counter[(label, predict_label)] += 1
        #if predict_label != label:
        #    print(xs)
        #    print(label,predict_label)
        #    print(rv_label)


    print('Detail:')
    for key, value in test_counter.items():
        label, predict_label = key
        print('%-4s -> %-4s : %d' % (label, predict_label, value))

    # for total
    print('Total: precision = %.3f' % (
        (test_counter[('spam', 'spam')] + test_counter[('ham', 'ham')]) / sum(test_counter.values())
    ))

    # for junk
    precision, recall = get_precision_and_recall(
        test_counter[('spam', 'spam')],
        test_counter[('ham', 'spam')],
        test_counter[('spam', 'ham')],
        test_counter[('ham', 'ham')]
    )
    print('Junk: precision = %.3f, recall = %.3f' % (precision, recall))

    # for legitimate
    precision, recall = get_precision_and_recall(
        test_counter[('ham', 'ham')],
        test_counter[('spam', 'ham')],
        test_counter[('ham', 'spam')],
        test_counter[('spam', 'spam')]
    )
    print('Legitimate: precision = %.3f, recall = %.2f' % (precision, recall))



def main():
    train_email_data = EmailData()
    train_email_data.load_from_file('data/train')

    feature = Feature()
    feature.learn(train_email_data)
    train_data_set = feature.translate_email_data(train_email_data)

    #print(feature.features)

    naive_bayesian = NaiveBayesian()
    naive_bayesian.learn(feature, train_data_set)

    test_email_data = EmailData()
    test_email_data.load_from_file('data/test')
    test_data_set = feature.translate_email_data(test_email_data)

    print('# Training set')
    test(naive_bayesian, train_data_set)
    print('# Testing set')
    test(naive_bayesian, test_data_set)


if __name__ == '__main__':
    main()