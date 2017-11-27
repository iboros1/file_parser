feature_list = list()
BLOCK_MAX_SPACES = 3


def open_file(dirPath, s_file):
    all_file = open(dirPath + '/' + s_file, 'r')
    my_file = all_file.readlines()
    return my_file


def parse_feature(feature_file):
    feature_ended = True
    feature = list()
    # strip right to count left white spaces
    for item in (x.rstrip() for x in feature_file if x.strip()):
        if feature_ended and item.count(' ') < BLOCK_MAX_SPACES:
            # start of feature
            feature_ended = False
            if feature:
                process_feature(feature)
                feature = list()
        elif item.count(' ') >= BLOCK_MAX_SPACES:
            # consider feature as ended
            feature_ended = True
        feature.append(item.lstrip())
    else: # process last feature
        process_feature(feature)


def process_feature(feature):
    tags = list()
    f_type = str()
    body = str()
    for item in feature:
        if item.startswith('@'):
            tags.append(item)
            continue
        elif item.startswith('Feature:'):
            f_type = 'feature'
        elif item.startswith('Background:'):
            f_type = 'background'
        elif item.startswith('Scenario:'):
            f_type = 'scenario'
        body += item
    else:
        if f_type == 'feature':
            f_type = '{0}{1}'.format(','.join(tags), f_type)
            tags = list()
        feature_list.append(dict(
            type=f_type,
            body=body,
            tags=','.join(tags)
        ))
    return feature_list

