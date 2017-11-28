import re
from enum import Enum

BLOCK_MAX_SPACES = 3


class FeatureType(Enum):
    feature = 'Feature:'
    background = 'Background:'
    scenario = 'Scenario:'


def make_feature(feature_file):
    feature_list = list()

    def lead_spaces(line):
        match = re.match(r'^\s*', line)
        return match.group().count(' ')

    def parse_feature():
        feature_ended = True
        feature = list()
        # strip right to count left white spaces
        for item in (x.rstrip() for x in feature_file if x.strip()):
            if feature_ended and lead_spaces(item) < BLOCK_MAX_SPACES:
                # start of feature
                feature_ended = False
                if feature:
                    process_feature(feature)
                    feature = list()
            elif lead_spaces(item) >= BLOCK_MAX_SPACES:
                # consider feature as ended
                feature_ended = True
            feature.append(item.lstrip())
        else:  # process last feature
            process_feature(feature)

    def process_feature(feature):
        tags = list()
        f_type, body = str(), str()
        for item in feature:
            if item.startswith('@'):
                tags.append(item)
                continue
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
