import json
infile = open("headphone_dict.json",'rb')
inv_diction = {}
diction = json.load(infile)
for attribute_name in diction:
	for values in diction[attribute_name]:
		if values in inv_diction:
			inv_diction[values][attribute_name] = 1
		else:
			inv_diction[values] = {}
			inv_diction[values][attribute_name] = 1

outfile = open("headphone_inv_dict.json",'wb')

json.dump(inv_diction,outfile)
