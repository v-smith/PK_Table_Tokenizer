# Tokenizer

Scripts to: 
1. Convert Jsonl files to txt
2. Preprocess files 
```
python preprocess_txt_typer.py --input-file alltablesNotest.txt --output-file unique_html_tokens.csv
```
3. Train SentencePiece Tokenizer with all pubmed data 
4. a) Run typer file to train SentencePiece from command line (or on myriad) and allow change of vocab size etc: 
```
python tokenizer_tables.py --input-file alltables.txt --output-dir . --vocab-size 10000 --min-fz 3 --tokenizer-name alltables
python tokenizer_tables.py --input-file alltables.txt --output-dir . --vocab-size 5000 --min-fz 3 --tokenizer-name alltables
python tokenizer_tables.py --input-file nohtmlalltables.txt --output-dir . --vocab-size 5000 --min-fz 3 --tokenizer-name nohtmltables

```
b) Or Run typer file in terminal natively in Pycharm: 
```
python tokenizer_typer.py --input-file ../data/textfiles/text.txt --output-dir ../data/textfiles/ --vocab-size 200 --min-fz 3 --tokenizer-name test
```


