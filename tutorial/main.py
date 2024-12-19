# processing text files
# write a out put of a file to show many times each world was used.
# will be saved in new text file

import glob

# input is the text files
# using glob library

filepaths = glob.glob("files/*.txt") # also known as a pattern
# * is a filter if more then just txt files where in folder would not see them