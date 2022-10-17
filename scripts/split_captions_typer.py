from pk_tokenizer.utils import split_captions

def main(
        input_file: str = typer.Option(default="/Scratch/alltablesNotest.txt",
                                       help="Input text file"),
        output_file: str = typer.Option(default="/Scratch/captionsNotest.txt",
                                    help="Output text file")
):
    split_captions(input_file, output_file)

if __name__ == '__main__':
    typer.run(main)
