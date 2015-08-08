#!/usr/bin/python3
import sys
import math
import collections

if(len(sys.argv) == 3):
	training_file = str(sys.argv[1])
	model_file = str(sys.argv[2])
else:
	print("Invalid Arguments.\nUsage: nblearn.py TRAINING_FILE MODEL_FILE")
	sys.exit()

opf = open(model_file,"w")
ipf = open(training_file,"r")

no_of_docs=0
classes = dict()
bag_of_words = collections.defaultdict(dict)

nofwinc = dict()

listline =list()
feature = ""

for line in ipf:
	listline=line.split()
	
	class_word=listline[0]
	if class_word not in classes:
		classes[class_word]=1
		for feature in listline:
			
			if(feature!=class_word):
				if feature not in bag_of_words:
					
					if class_word in bag_of_words[feature]:
						bag_of_words[feature][class_word]+=1
					else:
						bag_of_words[feature][class_word]=1
				else:
					if class_word in bag_of_words[feature]:
						bag_of_words[feature][class_word]+=1
					else:
						bag_of_words[feature][class_word]=1
					
	else:
		classes[class_word]+=1
		for feature in listline:
			
			if(feature!=class_word):
				if feature not in bag_of_words:
					
					if class_word in bag_of_words[feature]:
						bag_of_words[feature][class_word]+=1
					else:
						
						bag_of_words[feature][class_word]=1
				else:
					if class_word in bag_of_words[feature]:
						bag_of_words[feature][class_word]+=1
					else:
						
						bag_of_words[feature][class_word]=1
		
	no_of_docs+=1
	

	
vocab_size= len(bag_of_words)

for x in classes.keys():
	nofwinc[x]=0
	
	for word in bag_of_words.keys():
		
		if x in bag_of_words[word]:		
			nofwinc[x]+=bag_of_words[word][x]
		
	

for x in classes.keys():
	logPofclass=str(math.log10(classes[x]/no_of_docs))
	opf.write(x+" "+logPofclass+"\n")
	for word in bag_of_words.keys():
		if x in bag_of_words[word]:	
			logPofword=str(math.log10((bag_of_words[word][x]+1)/(nofwinc[x]+vocab_size+1)))
			opf.write(x+" "+word+" "+logPofword+"\n")
	opf.write(x+" drshnvr "+str(math.log10(1/(nofwinc[x]+vocab_size+1)))+"\n")


