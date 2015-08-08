#!/usr/bin/python3

import os
import sys
import re
if(len(sys.argv) == 3):
	input_file = str(sys.argv[1])
	output_file = str(sys.argv[2])
else:
	input_file="./SENTIMENT_training"
	output_file="sentiment_training.txt"


tf = open(output_file,"w")

neg=0
pos=0

for line in sorted(os.listdir(input_file)):
			classtype=re.search("NEG", line)
			if(classtype):
				neg=1
				pos=0
			classtype=re.search("POS",line)
			if(classtype):
				pos=1
				neg=0					
			line = input_file+'/'+line
			fh = open(line.replace('\n',''),"rb")
			contents = fh.read().decode('utf-8','replace').replace('\r\n',' ')
			if(neg):
				tf.write("NEG "+contents+'\n')
			if(pos):
				tf.write("POS "+contents+'\n')


		

			


