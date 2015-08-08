#!/usr/bin/python3

import os
import sys
import re
if(len(sys.argv) == 3):
	input_file = str(sys.argv[1])
	output_file = str(sys.argv[2])
else:
	input_file="./SPAM_training"
	output_file="spam_training.txt"


tf = open(output_file,"w")

spam=0
ham=0

for line in sorted(os.listdir(input_file)):
			classtype=re.search("SPAM", line)
			if(classtype):
				spam=1
				ham=0
			classtype=re.search("HAM",line)
			if(classtype):
				ham=1
				spam=0					
			line = input_file+'/'+line
			fh = open(line.replace('\n',''),"rb")
			contents = fh.read().decode('utf-8','replace').replace('\r\n',' ')
			if(spam):
				tf.write("SPAM "+contents+'\n')
			if(ham):
				tf.write("HAM "+contents+'\n')


		

			


