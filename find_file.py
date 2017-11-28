import os
from feature_parser import make_feature

"START-CONFIG"

rootDir = os.getcwd()

"END-CONFIG "


def walk_through_folders():

    for dirPath, dirName, fileName in os.walk(rootDir):
        for s_file in fileName:
            if s_file.endswith('.feature'):
                feature_file = open(dirPath + '/' + s_file, 'r')
                feature_list = make_feature(feature_file.readlines())
                # ToDo: save feature to excel
                print(feature_list)


def main():
    walk_through_folders()


if __name__ == '__main__':
    main()
