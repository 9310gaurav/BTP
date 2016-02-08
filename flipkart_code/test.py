import csv
import json
with open("model_id.csv",'rb') as csvfile:
	spamreader = csv.DictReader(csvfile)
	i = 0
	for row in spamreader:
		print row['model_id']