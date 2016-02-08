import random
import csv
import matching
import json
def create_sample(category,size):
	print "size is "+ size
	print "category is "+ category
	csvfile = open('combined.csv')
	csv_reader = csv.reader(csvfile, delimiter=',')
	i = 1
	array = []
	for row in csv_reader:
		text = row[3]
		split = text.split(',')
		tmp = "All Categories"
		if(tmp==category):
		    category=split[0]
		if(split[0] == category):
			print split[0]
			array.append(i)
		i = i+1
	#print i
	print len(array)
	#print "ssss"+ size
	sample = random.sample(array,int(size))
	return sample

def output_rows(category,size):
	json_data = open('catalog_dict.json')
	catalog = json.load(json_data)
	json_data.close()
	json_data1 = open('inv_catalog_dict.json')
	inv_catalog = json.load(json_data1)
	sample = create_sample(category,size)
	csvfile = open('combined.csv')
	csv_reader = csv.reader(csvfile, delimiter=',')
	rows = []
	x = []
	x.append("S NO.")
	x.append("ASIN")
	x.append("Title")
	x.append("Brand")
	x.append("Category")
	x.append("Description")
	x.append("Output")
	rows.append(x)
	j = 1
	i = 1
	for row in csv_reader:
		#print row +"\n"
		if i in sample:
			x = []
			x.append(str(j))
			j = j + 1
			x.append(row[0])
			x.append(row[1])
			x.append(row[2])
			x.append(row[3])
			x.append(row[4])
			output = matching.match(row[4],catalog,inv_catalog)
			x.append(output)
			rows.append(x)
		i = i + 1
	return rows