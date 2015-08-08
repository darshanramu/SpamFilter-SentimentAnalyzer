To Generate the Training file:
------------------------------
Place all the training files under one directory. Ensure all files have proper labels as their filenames and run:
./create_spam_training.py <Directory_Name> <output_filename>
./create_sentiment_training.py <Directory_Name> <output_filename>

To learn and generate the model file:
-------------------------------------
./nblearn.py TRAININGFILE MODELFILE

To classify the documents:
--------------------------
./nbclassify MODELFILE TESTFILE > output_file
MODELFILE is the file generated during learning phase
