import ijson
import json
infile = open("catalog_random_5perc",'rb')
catalog = {}
i = 0
for l in infile:
	if i==200000:
		break
	elif i>0:
		s = l.split('\t')
		data = json.loads(s[0])
		if data["vertical_name"] in catalog:
			for attr in data["catalog_attribute_values"]:
				if attr["attributeid"] in catalog[data["vertical_name"]]:
					for values in attr["attributevalue"]:
						if values["attributevalue"] in catalog[data["vertical_name"]][attr["attributeid"]]:
							catalog[data["vertical_name"]][attr["attributeid"]][values["attributevalue"]] = catalog[data["vertical_name"]][attr["attributeid"]][values["attributevalue"]] + 1
						else:
							catalog[data["vertical_name"]][attr["attributeid"]][values["attributevalue"]] = 1
				else:
					catalog[data["vertical_name"]][attr["attributeid"]] = {}
					for values in attr["attributevalue"]:
						catalog[data["vertical_name"]][attr["attributeid"]][values["attributevalue"]] = 1
		else:
			catalog[data["vertical_name"]] = {}
			for attr in data["catalog_attribute_values"]:
				catalog[data["vertical_name"]][attr["attributeid"]] = {}
				for values in attr["attributevalue"]:
						catalog[data["vertical_name"]][attr["attributeid"]][values["attributevalue"]] = 1
	i = i + 1

outfile = open("catalog_category_dict.json",'wb')
json.dump(catalog,outfile)