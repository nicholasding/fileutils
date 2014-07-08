try:
    import ujson as json
except ImportError:
    import json


def iterparse(fp, func):
    with open(fp, 'r') as fp:
        for line in fp:
            func(json.loads(line))
