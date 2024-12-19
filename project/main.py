# merge files together
# using the glob
import glob

with open('combined_files.txt', 'w') as outfile: # creating new file
    for filename in sorted(glob.glob('files/*.txt')): # interating over each file
        with open(filename) as infile: # opens each file to read
            for line in infile:
                outfile.write(line)
            outfile.write('\n\n##################\n\n')


