import os
from temp import run_all

"START-CONFIG"

rootDir = '/Users/istvan.boros/work/find_file'

"END-CONFIG "


def walk_through_folders():

    for dirPath, dirName, fileName in os.walk(rootDir):
        for s_file in fileName:
            if s_file.endswith('.feature'):
                features = run_all(dirPath, s_file)


    return dirPath, s_file, features


def main():
    walk_through_folders()


if __name__ == '__main__':
    main()
