"""This script splits txt file on html tokens for tokenizer training"""
import typer
import re
from tqdm import tqdm

def main(
        input_file: str = typer.Option(default="/Scratch/alltablesNotest.txt",
                                       help="Input text file"),
        output_file: str = typer.Option(default="/Scratch/alltablesNotestSplit.txt",
                                    help="Output text file")

):
    splitters = {'>': ' ', '<': ' '}

    def replace_all(text, dic):
        for i, j in splitters.items():
            text = text.replace(i, j)
        return text

    fout = open(output_file, "wt")

    with open(input_file) as file:
        line_count = 0
        for line in tqdm(file):
            line = re.sub(r"\<style>(.*?)\</style>", ' ', line)
            line = replace_all(line, splitters)
            fout.write(line)
            line_count += 1

    print(line_count)

if __name__ == '__main__':
    typer.run(main)
