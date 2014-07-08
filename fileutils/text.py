import codecs


def iterparse(fp, func, utf8=False):
    if utf8:
        fp = codecs.open(fp, 'r', encoding='UTF-8')
    else:
        fp = open(fp, 'r')

    for line in fp: func(line)

    fp.close()
