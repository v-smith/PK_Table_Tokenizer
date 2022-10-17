"""This script finds unique html tokens in desired input file and saves these to a txt file"""
import typer
import re
from collections import Counter
import pandas as pd
from pk_tokenizer.utils import find_line_tokens


def main(
        input_file: str = typer.Option(default="/Scratch/text.txt",
                                       help="Input text file"),
        output_file: str = typer.Option(default="/Scratch/html_tokens.csv",
                                    help="Output text file")

):
        unique_tokens = find_line_tokens(input_file=input_file)

        with open(file=output_file, encoding="w") as output:
            output.write(str(unique_tokens))

if __name__ == '__main__':
    typer.run(main)
