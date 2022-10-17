"""This script parses html tables in txt files to find out unique tokens"""
import typer
from bs4 import BeautifulSoup
from collections import Counter
import pandas as pd
from tqdm import tqdm
from pk_tokenizer.utils import get_tags

def main(
        input_file: str = typer.Option(default="/Scratch/text.txt",
                                       help="Input text file"),
        output_file: str = typer.Option(default="/Scratch/bs_html_tokens.csv",
                                    help="Output text file")

):

    get_tags(input_file=input_file, output_file=output_file)

if __name__ == '__main__':
    typer.run(main)
