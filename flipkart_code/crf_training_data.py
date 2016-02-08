import json
def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)


list_of = ['brand','color','model_id','headphone_jack','cord_length','wired_wireless','headset_design','headset_type']
infile = open("annotated_data.json",'rb')
data = json.load(infile)
infile.close()
infile = open("headphone_inv_dict.json",'rb')
inv_diction = json.load(infile)
k = 0
f = open('crf_training_data.txt', 'w')
for key in data:
	itokens,labels = data[key]
	k = 0
	for iitem in itokens:
		item = iitem.encode('ascii', 'ignore').decode('ascii')
		s = ""
		s = s+item
		if k == 0:
			s = s+"\t"+"1"
		else:
			s = s+"\t"+"0"

		if k == len(itokens)-1:
			s = s+"\t"+"1"
		else:
			s = s+"\t"+"0"

		if hasNumbers(item) is True:
			s = s+"\t"+"1"
		else:
			s = s+"\t"+"0"

		if item.isdigit():
			s = s+"\t"+"1"
		else:
			s = s+"\t"+"0"

		c = 0
		for i in range(len(item)-3):
			p = item[i:i+4]
			s = s+"\t"+p
			c = c + 1
			if c == 5:
				break
		while c<=5:
			s = s + "\t"+"X"
			c = c+1

		if k!=0 and iitem[k-1] == "from":
			s = s+"\t"+"1"
		else:
			s = s+"\t"+"0"

		if k!=0 and iitem[k-1] == "by":
			s = s+"\t"+"1"
		else:
			s = s+"\t"+"0"

		if k!=0 and iitem[k-1] == "and":
			s = s+"\t"+"1"
		else:
			s = s+"\t"+"0"


		for attr in list_of:
			if item in inv_diction:
				if attr in inv_diction[item]:
					s = s+"\t"+"1"
				else:
					s = s+"\t"+"0"
			else:
				s = s+"\t"+"0"

		f.write(s+"\n")
	f.write("\n")

