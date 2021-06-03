import typer
import re
from tqdm import tqdm

def main(
        input_file: str = typer.Option(default="/Scratch/alltablesNotest.txt",
                                       help="Input text file"),
        output_file: str = typer.Option(default="/Scratch/captionsNotest.txt",
                                    help="Output text file")

):
    def split_captions(input_file, output_file):
        '''Function to split out captions from txt file of tables and save to a new file'''
        fout = open(output_file, "wt")

        with open(input_file) as file:
            line_count = 0
            for line in tqdm(file):
                caption = re.search(r"(?<=\<h4>)(.*?)(?=\</h4>)", line).group()
                fout.write(caption + "\n")
                line_count += 1
            print(line_count)

    split_captions(input_file, output_file)

if __name__ == '__main__':
    typer.run(main)
