import re
from pk_tokenizer.utils import multiple_replace

replacements = {'<(.*?)>': 'test', "\{.*?\}": 'test2'}

with open("../data/textfiles/text.txt") as Bib_read:
    with open ('../data/textfiles/outext.txt', 'w') as Bib_write:
        read_lines = Bib_read.readlines()
        for rows in read_lines:
            #print(rows)
            text = rows
            new_text = multiple_replace(replacements, text)
            #print(new_text)
            Bib_write.write(new_text)

