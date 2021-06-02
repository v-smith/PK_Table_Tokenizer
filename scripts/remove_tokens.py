import re

replacements = {'<(.*?)>': 'test', "\{.*?\}": 'test2'}

def multiple_replace(dictionary, text):
    # Create a regular expression  from the dictionaryary keys

    regex = re.compile("(%s)" % "|".join(map(re.escape, dictionary.keys())))

    # For each match, look-up corresponding value in dictionaryary
    String = lambda mo: dictionary[mo.string[mo.start():mo.end()]]
    return regex.sub(String , text)

if __name__ == "__main__":

    with open("../data/textfiles/text.txt") as Bib_read:
        with open ('../data/textfiles/outext.txt', 'w') as Bib_write:
            read_lines = Bib_read.readlines()
            for rows in read_lines:
                #print(rows)
                text = rows
                new_text = multiple_replace(replacements, text)
                #print(new_text)
                Bib_write.write(new_text)

