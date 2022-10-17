"""This script removes html tokens and style information from a txt file for tokenizer training"""
import typer
import re
from tqdm import tqdm
from pk_tokenizer.utils import rem_html

def main(
        input_file: str = typer.Option(default="/Scratch/alltablesNotest.txt",
                                       help="Input text file"),
        output_file: str = typer.Option(default="/Scratch/alltablesNotestNohtml.txt",
                                    help="Output text file")

):
    rem_html(input_file, output_file)

if __name__ == '__main__':
    typer.run(main)
