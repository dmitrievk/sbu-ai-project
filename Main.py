__author__ = 'tian'

from EmailData import EmailData
from Feature import Feature


def main():
    email_data = EmailData()
    email_data.load_from_file('data/train')
    feature = Feature()
    feature.learn(email_data)


    pass


if __name__ == '__main__':
    main()