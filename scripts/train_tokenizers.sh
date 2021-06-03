#!/usr/bin/env sh
#alltables
python tokenizer_typer.py --input-file alltablesNotest.txt --output-dir . --vocab-size 10000 --min-fz 3 --tokenizer-name alltablesNotest
python tokenizer_typer.py --input-file alltablesNotest.txt --output-dir . --vocab-size 5000 --min-fz 3 --tokenizer-name alltablesNotest

#split on <>
python tokenizer_typer.py --input-file alltablesNotestSplit.txt --output-dir . --vocab-size 10000 --min-fz 3 --tokenizer-name alltablesNotestSplit
python tokenizer_typer.py --input-file alltablesNotestSplit.txt --output-dir . --vocab-size 5000 --min-fz 3 --tokenizer-name alltablesNotestSplit

#html removed
python tokenizer_typer.py --input-file alltablesNotestNohtml.txt --output-dir . --vocab-size 10000 --min-fz 3 --tokenizer-name alltablesNotesNohtml
python tokenizer_typer.py --input-file alltablesNotestNohtml.txt --output-dir . --vocab-size 5000 --min-fz 3 --tokenizer-name alltablesNotestNohtml
python tokenizer_typer.py --input-file alltablesNotestNohtml.txt --output-dir . --vocab-size 3000 --min-fz 3 --tokenizer-name alltablesNotestNohtml

#caption only
python tokenizer_typer.py --input-file captionsNotest.txt --output-dir . --vocab-size 5000 --min-fz 3 --tokenizer-name captionsNotest
python tokenizer_typer.py --input-file captionsNotest.txt --output-dir . --vocab-size 3000 --min-fz 3 --tokenizer-name captionsNotest
