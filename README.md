fileutils
=========

Utilities for file parsing in Python.

XML iterparse
-------------

<pre>
from fileutils import xml

def print_attributes(element):
    print element

xml.iterparse('example.xml', tag='Item', func=print_attribute)
</pre>

