import os

rootDir = '/Users/istvan.boros/work/find_file'


def walk_through_folders():
    for dirName, subdirList, fileList in os.walk(rootDir):
       # print('Found directory: %s' % dirName)
        for fname in fileList:
        #    print('\t%s' % fname)
            if fname.endswith('.feature'):
                my_file = open_file(dirName, fname)
                get_my_data(my_file, fname)
    return dirName, fname


def open_file(dirName, fname):
    all_file = open(dirName + '/' + fname, 'r')
    my_file = all_file.readlines()
    return my_file


def get_my_data(my_file, fname):
    tags = {fname: " "}
    for item in my_file:
        while not item.lstrip().startswith("@"):
            tags[fname].update(item)
            break
    print(tags)


def main():
    dirName, fname = walk_through_folders()
    open_file(dirName, fname)


if __name__ == '__main__':
    main()
