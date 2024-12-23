# processing text files
# write a out put of a file to show many times each world was used.
# will be saved in new text file

import glob

# input is the text files
# using glob library

filepaths = sorted(glob.glob("files/*.txt")) # also known as a pattern
# * is a filter if more then just txt files where in folder would not see them
# use sort to place files in abc order

# open each text file
# list of something what to iteriate

word_frequencies = {} # gets define outside of for loop
"use a dictionary {} each word is a key and frequencie is value"
for filepath in filepaths:
    with open(filepath, 'r') as file:
        content = file.read()

        words = content.split() # treats each word as a seperate item


        for word in words:
            if not word in word_frequencies:
                word_frequencies[word] = 1 # int method
            else: # if word is in list then it adds 1
                word_frequencies[word] += 1

# creating doc with word freqencies
with open('word_frequencies.txt', 'w') as file:
    for word, count in word_frequencies.items(): # this makes the word_frequencie into a str
        'access each key and value'
        content = file.write(f'{word}: {count}\n') # only accepts str method
        """
        take the dictionary 
         word = key
         int = value         
        """
