from os import listdir
from os.path import isfile, join
import rarfile
import re
import json
import csv
def collect_data(mypath):
	onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
	csvfile = open('combined.csv', 'wb')
	csv_writer = csv.writer(csvfile,delimiter=',')
	for filename in onlyfiles:
		rf = rarfile.RarFile(mypath+"/"+filename)
		for f in rf.infolist():
			rar_file = ""
			try:
				rar_file = rf.open(f.filename)
			except Exception, e:
				continue
			
			csv_reader = csv.reader(rar_file, delimiter=',')
			i = 0
			for row in csv_reader:
				if i!=0:
					if len(row) > 4 and str(row[4])!='':
						csv_writer.writerow(row)
				else:
					i=1

			

if __name__ == '__main__':
	collect_data("SYW")