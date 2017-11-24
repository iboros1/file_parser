feature_dict = dict(
    # file=s_file,
    date=None,
    feature_name=None,
    name=None,
    steps=None,
    tags=None,
    comments=None,
    background=None,
    all=[]
)



def open_file(dirPath, s_file):
    all_file = open(dirPath + '/' + s_file, 'r')
    my_file = all_file.readlines()
    return my_file, s_file


def parse_feature(my_file):
    feature_ended = True
    feature = list()
    for item in filter(lambda x: bool(x.strip()), my_file):
        # check if start of feature
        item = item.strip()
        if feature_ended and item.count(' ') < 3:
            feature_ended = False
        if feature:
                process_feature(feature)
                feature = []
        elif item.count(' ') >= 3:
            # consider feature as ended
            feature_ended = True
        feature.append(item.lstrip())
    else:
        # process last feature
        process_feature(feature)


def process_feature(feature):

    if feature is not None:
        for item in feature:
            if'Feature:' in str(item):
                feature_dict['feature_name'] = feature
            elif feature[0].startswith('#'):
                feature_dict['comments'] = feature
            elif feature[0].startswith('Background'):
                feature_dict['background'] = feature
            else:
                feature_dict['all'].append(feature)
    return feature_dict


def run_all(dirPath, s_file):
    my_file, s_file = open_file(dirPath, s_file)
    feature = parse_feature(my_file)
    dict =  process_feature(feature)
    # print('>>>>>>>', my_file)
    # print('......' , feature)
    # print('----------', dict)
    print(feature_dict)
    return dict