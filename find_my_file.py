#!/usr/local/bin/python3
import os


def sub_folders(path):
    for item in os.listdir(path):
        item = os.path.abspath(item)
        if os.path.isdir(item):
            sub_folders(os.path.join(path, item))
        elif item.endswith('.feature'):
            print('>>>>>>', item)


def main():
    sub_folders('/Users/istvan.boros/work/find_file')

if __name__ == '__main__':
    main()
