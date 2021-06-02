#!/usr/bin/env sh
python tokenizer_tables.py --input-file alltablesNotest.txt --output-dir . --vocab-size 10000 --min-fz 3 --tokenizer-name alltablesNotest
python tokenizer_tables.py --input-file alltablesNotest.txt --output-dir . --vocab-size 5000 --min-fz 3 --tokenizer-name alltablesNotest
python tokenizer_tables.py --input-file alltablesNotestSplit.txt --output-dir . --vocab-size 5000 --min-fz 3 --tokenizer-name alltablesNotestSplit
#python tokenizer_tables.py --input-file alltablesNotestSplit.txt --output-dir . --vocab-size 5000 --min-fz 3 --tokenizer-name alltablesNotestSplit
#python tokenizer_tables.py --input-file alltablesNotestSplit.txt --output-dir . --vocab-size 5000 --min-fz 3 --tokenizer-name alltablesNotestSplit
