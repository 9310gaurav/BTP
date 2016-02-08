import csv
import json
import nltk
import re
diction = {}
list_of = ['brand','color','model_id','headphone_jack','cord_length','wired_wireless','headset_design','headset_type']
for item in list_of:
	diction[item] = {}
with open("headphone_1454324853776_catalog.csv") as csvfile:
	spamreader = csv.DictReader(csvfile)
	i = 0
	for row in spamreader:
		for item in list_of:
			if item=='model_id':
				modelids = "NA"
				s = row['model_id'] + " "+ row['brief_description']
				flag = 0
				tokens = nltk.word_tokenize(s.decode('utf-8'))
				for it in tokens:
					if(re.match('^(?=.*[a-zA-Z])(?=.*\d)',it) or re.match('^(?=.*\d)(?=.*[a-zA-Z])',it)):
						modelids = it.encode('utf-8').replace(" ", "")
						flag = 1
						break
				diction[item][modelids.lower()] = 1
			else:
				diction[item][row[item].lower()]=1
outfile = open("headphone_dict.json",'wb')

json.dump(diction,outfile)			