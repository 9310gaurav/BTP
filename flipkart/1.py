import csv
with open("headphone_1454324853776_catalog.csv") as csvfile:
	spamreader = csv.DictReader(csvfile)
	i = 0
	for row in spamreader:
		print row['model_id']
		break

