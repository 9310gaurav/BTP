import ijson
import json
import re
_digits = re.compile('\d')
def contains_digits(d):
    return bool(_digits.search(d))
infile = open("catalog_random_5perc",'rb')
invcatalog = {}
i = 0
for l in infile:
	if i>0:
		s = l.split('\t')
		data = json.loads(s[0])
		if data["vertical_name"] == "book":
			continue
		for attr in data["catalog_attribute_values"]:
			for values in attr["attributevalue"]:
				if contains_digits(values["attributevalue"]) == False:
					invcatalog[values["attributevalue"]] = 1
	
	i = i + 1
if "is" in invcatalog:
	print "yolo"
if "for" in invcatalog:
	print "hush" 
#outfile = open("inv_catalog_dict.json",'wb')
#json.dump(invcatalog,outfile)