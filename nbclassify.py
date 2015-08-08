#!/usr/bin/python3

import sys
import re
import math
import collections



if(len(sys.argv) == 3):
	model_file = str(sys.argv[1])
	training_file = str(sys.argv[2])
	
else:
	print("Invalid arguments.\nUsage: nbclassify.py MODEL_FILE TEST_FILE")
	sys.exit()

tf = open(training_file,"r")
mf = open(model_file,"r")
model = collections.defaultdict(dict)
class_prob  = dict()


for line in mf:
	words=line.split()
	cl = words[0]
	if(len(words)==2):
		class_prob[cl]=words[1]
	else:
	
		model[cl][words[1]]=words[2]

class_found='NA'
classes = class_prob.keys()
classify = dict()
for fts in tf:
	max=float('-inf')
	features=fts.split()
	
	for c in classes:
	
		classify[c]=(float(class_prob[c]))
		for f in features:
			if model[c].get(f) :
				classify[c]+=(float(model[c].get(f)))
			else:
				classify[c]+=(float(model[c].get('drshnvr')))
		if(classify[c]>max):
			max=classify[c]
			class_found=c
	print(class_found)
	


