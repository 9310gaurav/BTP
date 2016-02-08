import csv
import json
import nltk
import re
desc="Pc108M 8 In. Vmt Tuneable Cb Antenna With Magnet Mount"
tokens = nltk.word_tokenize(desc.decode('utf-8'))
print tokens
for item in tokens:
	if(re.match('^(?=.*[a-zA-Z])(?=.*\d)',item) or re.match('^(?=.*\d)(?=.*[a-zA-Z])',item)):
		print item
	
diction = {}
list_of = ['brand','color','model_id','headphone_jack','cord_length','wired_wireless','headset_design','headset_type']
for item in list_of:
	diction[item] = {}
modelids = []
count = 0
modelids.append("model_id")
with open("headphone_1454324853776_catalog.csv") as csvfile:
	spamreader = csv.DictReader(csvfile)
	i = 0
	for row in spamreader:
		count = count+1
		s = row['model_id'] + " "+ row['brief_description']
		flag = 0
		tokens = nltk.word_tokenize(s.decode('utf-8'))
		for item in tokens:
			if(re.match('^(?=.*[a-zA-Z])(?=.*\d)',item) or re.match('^(?=.*\d)(?=.*[a-zA-Z])',item)):
				modelids.append(item.encode('utf-8').replace(" ", ""))
				flag = 1
				break
		if flag == 0:
			modelids.append("NA")

with open('model_id.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerows(modelids)		