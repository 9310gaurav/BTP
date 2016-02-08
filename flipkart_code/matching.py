from os import listdir
from os.path import isfile, join

import re
import json
import nltk
import os
_digits = re.compile('\d')
def contains_digits(d):
    return bool(_digits.search(d))



def match(s,catalog,inv_catalog):
	#s="The PHBT98BK Bluetooth Home Theater Tower brings a beautiful, powerful sound system, 30-pin iPod, iPhone, iPad player and charger to any room of your home. The 600 watt system booms with power, thanks to built-in dual tweeters, dual 3.5 mid-range drivers, and an 8 subwoofer that packs a massive punch. Bluetooth compatibility allows you to stream your favorite music or internet radio stations easily and wire-free. Plug in your iPad, iPhone, or iPod, to the docking station location at the top of the unit, and youre ready to go - plus, this unit charges your iDevice, so the party will never end. More features include 2.1 channel digital amplifier, built-in FM radio, alarm clock and time control so you can wake up to your favorite music, and AUX input so you can connect and stream audio from other digital music players and external media sources. Use the front panel touch controls or the included remote to adjust the volume, bass, treble, and even remotely control your iDevice when docked. The blue LCD display is bright and crisp, and the matte black finish will add an elegant and clean design to your full ranged audio. Includes 110V AC power adapter."
	tokens = nltk.word_tokenize(s.decode('utf-8'))
	lastattr = ""
	tags = {}
	matches = {}
	for item in tokens:
		itemx = item.lower()
		if itemx in catalog:
			tags[item] = "attribute_name"
	for item in tokens:
		itemx = item.lower()
		if itemx in catalog["finish"] or contains_digits(itemx):
			tags[item] = "attribute_value"
	for item in tokens:
		itemx = item.lower()
		if item in tags and tags[item] == "attribute_name":
			lastattr = itemx
		elif item in tags and lastattr != "":
				if itemx in catalog[lastattr] or contains_digits(item):
					matches[item] = lastattr
			

	lastattr = ""
	for item in reversed(tokens):
		itemx = item.lower()
		if item in tags and tags[item] == "attribute_name":
			lastattr = itemx
		elif item in tags and lastattr != "":
				if itemx in catalog[lastattr]:
					matches[item] = lastattr
	for i in range(len(tokens)):
		if tokens[i] == ":" and i!=0 and i!=len(tokens)-1:
			matches[tokens[i+1]] = tokens[i-1]
	workfile = open("stanford-parser-full-2014-10-31/input.txt",'w+')
	workfile.write(s)
	workfile.close()
	os.system('stanford-parser-full-2014-10-31/lexparser.sh stanford-parser-full-2014-10-31/input.txt > output.txt')
	infile = open('output.txt')
	for line in infile:
		if line[0:4] == "prep" or line[0:4] == "amod" or line[0:3] == "num":
			x = line.split("(")
			y = x[1].split(",")
			p1 = y[0].split("-")[0]
			p2 = y[1].split("-")[0][1:]
			if p1 in tokens and p2 in tokens:
				if p1 in tags and tags[p1] == "attribute_name":
					matches[p2] = p1
				elif p2 in tags and tags[p2] == "attribute_name":	
					matches[p1] = p2
				elif p1 in inv_catalog or contains_digits(p1):
					matches[p1] = p2
				elif p2 in inv_catalog or contains_digits(p2):
					matches[p2] = p1

	return (tags,matches)



