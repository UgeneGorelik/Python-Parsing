#simple XML parse and search usinh xml.etree lib

import os
import xml.etree.ElementTree as et

#find the corrent path
base_path=os.path.dirname(os.path.realpath(__file__))

#path of xml file
xml_file=os.path.join(base_path,"data\\listing.xml")

#parse tree to object from file
tree=et.parse(xml_file)

#get root obkect
root=tree.getroot()

#print tag and attribute starting from root tree
for child in root:
    print(child.tag,child.attrib)

#print elemnts that belongs to root
for child in root:
    for element in child:
        print(element.tag,":",element.text)

#instert new elemnt (first path,then name ,then attribute as dicy
new_var=et.SubElement(root[0][0],"note",attrib={"id":"4"})
#sub elements element
new_var_to=et.SubElement(new_var,"to")
#sub elemnets second element
new_var_from=et.SubElement(new_var,"from")

#text to sub elemets elements
new_var_to.text="d"
new_var_from.text="d"

#write back to xmls file
tree.write(xml_file)

#you can acsses also using indexes such as directory
print(root[0][0].tag,root[0][0].text)

#iterative go trough tree using DFS
for elem in tree.iter():
   print (elem.tag, elem.attrib)


#fins all elements
all_name_elements = tree.findall('*/to')

print(all_name_elements)

for x in all_name_elements:
    print(x.tag,x.text)
