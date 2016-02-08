import nltk
import csv
import json
import pprint
import pickle
infile = open("headphone_inv_dict.json",'rb')
inv_diction = json.load(infile)
map_data = {}
k = 0
with open("test_headphones.csv") as csvfile:
	spamreader = csv.DictReader(csvfile)
	i = 0
	j=0
	for row in spamreader:
		desc1 = row['model_id'].lower()+" "+row['description'].lower()
		if desc1!="":
			j= j+1
		desc =desc1.replace("||", " ")
		tokens = nltk.word_tokenize(desc.decode('utf-8'))
		print tokens
		itokens = []
		labels = []
		list_of = ['brand','color','model_id','headphone_jack','cord_length','wired_wireless','headset_design','headset_type']
		for index in range(len(tokens)):
			if tokens[index] in inv_diction:
				lab = "NA"
				for x in inv_diction[tokens[index]]:
					if x in list_of:
						lab = x
						list_of.remove(x)
						break
				labels.append(lab)
				itokens.append(tokens[index])
				i = i+1
			else:
				if index == len(tokens)-1:
					break
				two_gram = tokens[index]+" "+tokens[index+1]
				two_gram_2 = tokens[index]+"$$"+tokens[index+1]
				if two_gram in inv_diction:
					lab ="NA"
					for x in inv_diction[two_gram]:
						if x in list_of:
							lab = x
							list_of.remove(x)
							break
					labels.append(lab)
					labels.append(lab)
					itokens.append(tokens[index])
					itokens.append(tokens[index+1])
					index = index+1
					i = i+1
					continue
				if two_gram_2 in inv_diction:
					lab ="NA"
					for x in inv_diction[two_gram_2]:
						if x in list_of:
							lab = x
							list_of.remove(x)
							break
					labels.append(lab)
					labels.append(lab)
					itokens.append(tokens[index])
					itokens.append(tokens[index+1])
					index = index+1
					i=i+1
				else:
					if index > len(tokens)-3:
						break
					three_gram = tokens[index]+" "+tokens[index+1]+" "+tokens[index+2]
					if three_gram in inv_diction:
						lab = "NA"
						for x in inv_diction[three_gram]:
							if x in list_of:
								lab = x
								list_of.remove(x)
								break
						labels.append(lab)
						labels.append(lab)
						labels.append(lab)
						itokens.append(tokens[index])
						itokens.append(tokens[index+1])
						itokens.append(tokens[index+2])
						index = index+2
						i = i+1
					else:
						itokens.append(tokens[index])
						labels.append("NA")
		map_data[str(k)] = (itokens,labels)
		k = k + 1
outfile = open("test_annotated_data.json",'wb')

json.dump(map_data,outfile)
print i,j