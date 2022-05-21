#!usr/bin/env python
# simple commandline script to remove the counts from vocab.src and vocab.trg file to use them for the joint vocab

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", help="provide path to vocab file")
parser.add_argument("-o", help="provide path to ouput file")
args = parser.parse_args()

with open(args.i, "r") as infile, open(args.o, "w") as outfile:
    for line in infile:
        word = line.split()[0]
        outfile.write(word + "\n")
print("done!")
