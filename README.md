# Tokenizer

Preprocess PubMed files and train SentencePience tokenizer on PubMed OA corpus and Pharmacokinetic Corpus from PubMed OA.

1. Convert Jsonl files to txt
```
#convert jsonl file to txt file 
python convert_text.py

#concatenate text files (for large files) 
python concat_txt_files.py
```
2. Preprocess files - N.B. typer files to use from command line with different inputs (useful for remote machines) 
```
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
3. Train SentencePiece Tokenizer with all pubmed data 
a) Run typer file to train SentencePiece from command line (or on myriad) and allow change of vocab size etc: 
```
python tokenizer_tables.py --input-file alltables.txt --output-dir . --vocab-size 10000 --min-fz 3 --tokenizer-name alltables
python tokenizer_tables.py --input-file alltables.txt --output-dir . --vocab-size 5000 --min-fz 3 --tokenizer-name alltables
python tokenizer_tables.py --input-file nohtmlalltables.txt --output-dir . --vocab-size 5000 --min-fz 3 --tokenizer-name nohtmltables

```
b) Or Run typer file in terminal natively in Pycharm: 
```
python tokenizer_typer.py --input-file ../data/textfiles/text.txt --output-dir ../data/textfiles/ --vocab-size 200 --min-fz 3 --tokenizer-name test
```
4. Try out tokenizer

```
python try_tokenizer_typer.py --input-file "../data/tokenizers/tokenizeralltablesNotesNohtml10000.json" --input-string DOCTYPE html  html  body  h4  
```

