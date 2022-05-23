#! usr/bin/env python
# script to visualize the impact of beam size on the bleu score
 
import pandas as pd
import argparse
import matplotlib.pyplot as plt
 
def cli():
    parser = argparse.ArgumentParser("script to visualize the impact of beam size on the bleu score")
    parser.add_argument("-i", help="input .csv with the beam size in the first and BLEU score in the second column")
    parser.add_argument("-o", help="path to the .png the graph should be saved to")
    args = parser.parse_args()
    return args

def main(args):
    df = pd.read_csv(args.i, names=["Beam size", "BLEU", "time in s"])
    line = df.plot.line(x="Beam size", subplots=True)
    #plt.show()
    plt.savefig(args.o)

main(cli())
        
