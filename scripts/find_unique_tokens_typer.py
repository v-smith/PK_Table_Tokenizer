"""This script finds unique html tokens in desired input file and saves these to a txt file"""
import typer
import re
from collections import Counter
import pandas as pd


def main(
        input_file: str = typer.Option(default="/Scratch/text.txt",
                                       help="Input text file"),
        output_file: str = typer.Option(default="/Scratch/html_tokens.csv",
                                    help="Output text file")

):
        file = open(input_file, "r")

        tokens = []
        for line in file:
            line_tokens = re.findall(r"\</(?:[^<>])*\>", line,
                                     flags=re.VERBOSE)  # r"\<(?:[^<>])*\>"  #r"(?<=\<)(.*?)(?=\>)" #r"\<.*?\>"
            tokens.extend(line_tokens)

        frequencies = Counter(tokens).most_common()
        pd.DataFrame(frequencies).to_csv(output_file)
        unique_tokens = sorted(list(set(tokens)))
        print(f"unique tokens: {len(unique_tokens)}")

        #with open(output_file, "w") as output:
            #output.write(str(unique_tokens))

if __name__ == '__main__':
    typer.run(main)
