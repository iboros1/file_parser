from enum import Enum

BLOCK_MAX_SPACES = 3


class FeatureType(Enum):
    feature = 'Feature:'
    background = 'Background:'
    scenario = 'Scenario:'


def make_feature(feature_file):

    feature_list = list()

    def parse_feature():
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
        else:  # process last feature
            process_feature(feature)

    def process_feature(feature):
        tags = list()
        f_type = str()
        body = str()
        for item in feature:
            if item.startswith('@'):
                tags.append(item)
                continue
            # elif item.startswith(FeatureType.feature.value):
            #     f_type = FeatureType.feature
            # elif item.startswith(FeatureType.background.value):
            #     f_type = FeatureType.background
            # elif item.startswith(FeatureType.scenario.value):
            #     f_type = FeatureType.scenario
            for ty in FeatureType:
                if item.startswith(ty.value):
                    f_type = ty
            body += '{} '.format(item)
        else:
            if f_type == FeatureType.feature:
                f_type = '{0}{1}'.format(','.join(tags), f_type.name)
                tags = list()
            else:
                f_type = f_type.name
            feature_list.append(dict(
                type=f_type,
                body=body,
                tags=','.join(tags)
            ))

    parse_feature()
    return feature_list
