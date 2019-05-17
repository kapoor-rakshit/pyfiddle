
# REFERENCE : https://docs.python.org/3.7/library/xml.etree.elementtree.html

# The xml.etree.ElementTree (ET) module implements a simple and efficient API for parsing and creating XML data.
# ET has two classes for this purpose - ElementTree represents the whole XML document as a tree, 
#                                   and Element represents a single node in this tree.



# importing data by reading from a file
import xml.etree.ElementTree as ET
tree = ET.parse('testXML.xml')
root = tree.getroot()



# an Element has a tagNAME, dictionary of attributes, text content within tag
print(root.tag)
print(root.attrib)
print(root.text)



# children nodes over which we can iterate
for i in root:
	print(i.tag, i.attrib, i.text)
	for j in i:
		print("<" + j.tag + ">", j.attrib, j.text)
	print("---------------------------------------")



# Children are nested, and we can access specific child nodes by index also
print(root[2][2].text)



# Element.iter() : iterate recursively over all sub-tree of an element below it (its children, their children, and so on).
# Element.findall() : finds only elements with a tag which are DIRECT children of the current element. 
# Element.find() : finds the first child with a particular tag.
# Element.get() : accesses the element’s attribute specified.
# 1
tags_list = root.iter("year")
for t in tags_list:
	print(t.text)

# 2
country_list = root.findall("country")
for c in country_list:
	print(c.find("rank").text)
	print(c.get("capital"))
	print("-----------------")



# Element.text : changing its text content 
# Element.set() : adding and modifying attributes
# Element.remove() : remove it's child element, STRING not allowed, only Element object
# Element.append() : adding new children
# ElementTree.write() : build XML documents and write them to files
# 1
# add one to each country’s rank, and add an updated attribute to the rank element
for rank in root.iter('rank'):
	new_rank = int(rank.text) + 1
	rank.text = str(new_rank)
	rank.set('updated', 'yes')

tree.write('testXML.xml')

# 2   
# remove all countries with a rank higher than 50
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)
        
tree.write('testXML.xml')

# 3
# remove attribute of an element, using pop('key', defaultValue_to_return) as attrib is a dict()
root[2][0].attrib.pop("updated", None)
tree.write("testXML.xml")
