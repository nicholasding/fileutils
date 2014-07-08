from lxml import etree


def fast_iter(context, func):
    for event, el in context:
        func(el)
        el.clear()
        while el.getprevious() is not None:
            del el.getparent()[0]
    del context

def iterparse(fp, tag, func):
    context = etree.iterparse(fp, events=('end',), tag=tag)
    fast_iter(context, func)
