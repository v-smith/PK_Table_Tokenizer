"""This script removes html tokens and style information from a txt file for tokenizer training"""
import typer
import re
from tqdm import tqdm

def main(
        input_file: str = typer.Option(default="/Scratch/alltablesNotest.txt",
                                       help="Input text file"),
        output_file: str = typer.Option(default="/Scratch/alltablesNotestNohtml.txt",
                                    help="Output text file")

):
    def rem_html(input_file, output_file):
        output_file = open(output_file, 'wt')
        with open(input_file, 'r') as file:
            line_count = 0
            for line in tqdm(file):
                line = re.sub(r"\<style>(.*?)\</style>", ' ', line)
                line = re.sub(r"\<(?:[^<>])*\>", ' ', line)
                line_count += 1
                #output_file.write(' '.join(line.split()))
                output_file.write(re.sub('\s+',' ',line) + "\n")
            print(line_count)

    rem_html(input_file, output_file)

if __name__ == '__main__':
    typer.run(main)
