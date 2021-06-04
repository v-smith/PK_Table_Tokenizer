from tokenizers import Tokenizer
import typer

def main(
        input_file: str = typer.Option(default="../data/tokenizers/tokenizeralltablesNotesNohtml10000.json",
                                    help="Input tokenizer file"),
        input_string: str = typer.Option(default="pharmacokinetics table head",
                                       help="Input text string"),

):

    tokenizer = Tokenizer.from_file(input_file)

    encoded = tokenizer.encode(input_string)

    print(encoded.tokens)
    print(encoded.ids)

if __name__ == '__main__':
    typer.run(main)
