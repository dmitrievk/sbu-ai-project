__author__ = 'tian'

from Email import Email

def main():
    emails = Email()
    emails.load_from_file('data/train')
    #print(emails.emails)
    pass

if __name__ == '__main__':
    main()