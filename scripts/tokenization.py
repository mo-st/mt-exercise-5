#! /bin/env/python

import sys
import argparse
from sacremoses import MosesTokenizer

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lang", type=str, help="language code for tokenizing", required=True)
    parser.add_argument("--input", help="input file to tokenize", required=True)
    args = parser.parse_args()

    return args

def main():
    
    args = parse_args()
    tokenizer = MosesTokenizer(lang=args.lang)
    
    with open(args.input, "r") as lines:
        all_tokens = []

        for line in lines:
            t = tokenizer.tokenize(line)
            all_tokens.append(t)

        for tokens in all_tokens:
            output_string = " ".join(tokens)
            sys.stdout.write(output_string + "\n")

if __name__ == "__main__":
    main()

