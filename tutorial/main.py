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
for filepath in filepaths:
    with open(filepath, 'r') as file:
        content = file.read()

