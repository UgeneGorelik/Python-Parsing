import os
from xml.etree  import ElementTree

with open('a.XML','r') as x_file:
    dom = ElementTree.parse(x_file)
    course=dom.findall('course/title')
    for c in course:
        print(c.text)