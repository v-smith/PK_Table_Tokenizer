# PK Table Tokenizer

This project trains Google's SentencePiece Tokenizer on text extracted from tables from the whole PubMed Open Access Subset of papers and Pharmacokinetic tables from that subset with different vocabulary sizes. 

Scripts to: 
1. Convert JSONL files to TXT file 
```          
python convert_text.py
```

2. Concatenate text files (for large files) 
```
python concat_txt_files.py
```
3. Preprocess files before Tokenization - N.B. typer files to use from command line

#find unique tokens using regex
python preprocess_txt_typer.py --input-file alltablesNotest.txt --output-file unique_html_tokens.csv

#check unique tokens using beautiful soup
python BSParserTyper.py --input-file alltablesNotest.txt --output-file bs_uniquie_tokens.csv

#remove html from files
python remove_html_typer.py --input-file alltablesNotest.txt --output-file alltablesNotestNohtml.txt
python remove_html_typer.py --input-file ../data/textfiles/test_table.txt --output-file ../data/test_table_nohtml.txt
python remove_html_typer.py --input-file ../data/textfiles/PKpmctablesNotest.txt --output-file ../data/textfiles/PKtablesNotest_nohtml.txt

#split file on html tags 
python split_txt_typer.py --input-file alltablesNotest.txt --output-file alltablesNotestNohtml.txt
python split_txt_typer.py --input-file ../data/textfiles/test_table.txt --output-file ../data/test_table_split.txt
python split_txt_typer.py --input-file ../data/textfiles/PKpmctablesNotest.txt --output-file ../data/PKtablesNotest_split.txt

#split out only captions 
python split_captions_typer.py --input-file alltablesNotest.txt --output-file captionsNotest.txt
python split_captions_typer.py --input-file ../data/textfiles/test_table.txt --output-file ../data/test_table_captions.txt

```

4. Train SentencePiece Tokenizer with all pubmed data 
a) Run typer file to train SentencePiece from command line (or on cluster) and allow change of vocab size etc: 
```
python tokenizer_tables.py --input-file alltables.txt --output-dir . --vocab-size 10000 --min-fz 3 --tokenizer-name alltables
python tokenizer_tables.py --input-file alltables.txt --output-dir . --vocab-size 5000 --min-fz 3 --tokenizer-name alltables
python tokenizer_tables.py --input-file nohtmlalltables.txt --output-dir . --vocab-size 5000 --min-fz 3 --tokenizer-name nohtmltables

```

b) Or Run typer file in terminal natively in Pycharm:
python tokenizer_typer.py --input-file ../data/textfiles/text.txt --output-dir ../data/textfiles/ --vocab-size 200 --min-fz 3 --tokenizer-name test

5. Try out tokenizer
```
try_tokenizer.py
```

