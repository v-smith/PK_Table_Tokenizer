"""This script parses html tables in txt files to find out unique tokens"""
import typer
from bs4 import BeautifulSoup
from collections import Counter
import pandas as pd
from tqdm import tqdm

def main(
        input_file: str = typer.Option(default="/Scratch/text.txt",
                                       help="Input text file"),
        output_file: str = typer.Option(default="/Scratch/bs_html_tokens.csv",
                                    help="Output text file")

):

    def get_tags(input_file, output_file):
        '''Function to retrieve all unique html tags from a lxml document'''
        all_tags = []
        with open(input_file, 'r') as file:
            for line in tqdm(file):
                soup = BeautifulSoup(line, 'lxml')  # Parse the HTML as a string
                tags = [tag.name for tag in soup.find_all()]
                all_tags += tags


        frequencies = Counter(all_tags).most_common()
        pd.DataFrame(frequencies).to_csv(output_file)
        unique_tags = list(set(all_tags))
        print(unique_tags)
        print(len(unique_tags))

    get_tags(input_file, output_file)

if __name__ == '__main__':
    typer.run(main)
