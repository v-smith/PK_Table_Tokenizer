#!/usr/bin/env sh
#split on <>
python split_txt_typer.py --input-file alltablesNotest.txt --output-file alltablesNotestSplit.txt

#html removed
python remove_html_typer.py --input-file alltablesNotest.txt --output-file alltablesNotestNohtml.txt

#caption only
python split_captions_typer.py --input-file alltablesNotest.txt --output-file captionsNotest.txt
