


def parse_feature_file(dirPath, s_file):
    feature_dict = dict(
        file=s_file,
        date=None,
        feature_name=None,
        name=None,
        steps=None,
        tags=None,
        comments=None,
        background=None
    )

    def open_file(dirPath, s_file):
        all_file = open(dirPath + '/' + s_file, 'r')
        my_file = all_file.readlines()
        return my_file


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
                #consider feature as ended
                feature_ended = True
            feature.append(item.lstrip())
        else:
            #process last feature
            process_feature(feature)

    def process_feature(my_file):
        tags = []
        feature = parse_feature(my_file)
        for item in feature:
            if item.startswit('@'):
                tags.append(item)
            elif item.startswit('Feature:'):
                feature_dict['feature_name'] = '{0} {1}'.format(','.join(tags), item)
            elif item.startswit('Background:'):
                feature_dict['background'] += item
            elif item.startswit('Scenario'):
                feature_dict['background'] += item





    def run_all(dirPath, s_file):
        my_file = open_file(dirPath, s_file)
        feature = parse_feature(my_file)
        return process_feature(feature)