import ijson
import json
infile = open("catalog_random_5perc",'rb')
catalog = {}
i = 0
for l in infile:
	if i>0:
		s = l.split('\t')
		data = json.loads(s[0])
		if data["vertical_name"] == "book":
			continue
		for attr in data["catalog_attribute_values"]:
			if attr["attributeid"] in catalog:
				for values in attr["attributevalue"]:
					if values["attributevalue"] in catalog[attr["attributeid"]]:
						catalog[attr["attributeid"]][values["attributevalue"]] = catalog[attr["attributeid"]][values["attributevalue"]] + 1
					else:
						catalog[attr["attributeid"]][values["attributevalue"]] = 1
			else:
				catalog[attr["attributeid"]] = {}
				for values in attr["attributevalue"]:
					catalog[attr["attributeid"]][values["attributevalue"]] = 1
	i = i + 1

outfile = open("catalog_dict.json",'wb')
json.dump(catalog,outfile)