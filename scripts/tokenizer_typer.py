"""This script trains SentencePiece Tokenizer with desired input file and saves trained tokenizer"""
import typer
import os
from tokenizers import SentencePieceBPETokenizer


def main(
        input_file: str = typer.Option(default="../data/textfiles/text.txt",
                                       help="Input file with all tables"),
        output_dir: str = typer.Option(default="../data/text_files",
                                    help="name of tokenizer"),
        vocab_size: int = typer.Option(default=10000,
                                        help="Vocab Size"),
        min_fz: int = typer.Option(default=3,
                                        help="minimum frequency"),
        tokenizer_name: str =typer.Option(default='tokenizer', help="tokenizer name")
):

        output_tokenizer_path = os.path.join(output_dir, 'tokenizer'+tokenizer_name+str(vocab_size)+'.json')

        tokenizer = SentencePieceBPETokenizer()
        tokenizer.train(input_file, vocab_size=vocab_size, min_frequency=min_fz)
        tokenizer.save(output_tokenizer_path)


if __name__ == '__main__':
    typer.run(main)
