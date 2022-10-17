import pandas as pd
from bs4 import BeautifulSoup
import re

def read_jsonl(file_path):
    """Read a .jsonl file and yield its contents line by line.
    file_path (unicode / Path): The file path.
    YIELDS: The loaded JSON contents of each line.
    """
    with Path(file_path).open('r', encoding='utf8') as f:
        for line in f:
            try:  # hack to handle broken jsonl
                yield ujson.loads(line.strip())
            except ValueError:
                continue

def write_to_text(input_json, out_file):
    """Writes html tables to TXT file.
    input_json (unicode / Path): The input json file. """
    all_tables = [x['html'].replace("\n", "#n#") for x in read_jsonl(file_path=input_json)]

    with open(out_file, 'w') as f:
        for item in all_tables:
            f.write("%s\n" % item)
            
    
def get_tags(input_file, output_file):
    """Retrieves all unique html tags from a xml document.
    input_path (unicode / Path): The xml file path.
    output_file (unicode / Path): output csv file path"""
    all_tags = []
    with open(input_file, 'r') as file:
        for line in tqdm(file):
            soup = BeautifulSoup(line, 'lxml')  # Parse the HTML as a string
            tags = [tag.name for tag in soup.find_all()]
            all_tags += tags

    frequencies = Counter(all_tags).most_common()
    pd.DataFrame(frequencies).to_csv(output_file)
    unique_tags = list(set(all_tags))
    print(unique_tags)
    print(len(unique_tags))
    return unique_tags

def find_line_tokens(input_file):
    """Retrives all unique html tags from TXT file.
    input_path (unicode / Path): The txt file path.
    YIELDS: list of tokens. """
    file = open(input_file)
    tokens = []
    for line in file:
        line_tokens = re.findall(r"\</(?:[^<>])*\>", line, flags=re.VERBOSE)
        tokens.extend(line_tokens)

    frequencies = Counter(tokens).most_common()
    unique_tokens = list(set(tokens))
    print(unique_tokens)
    print(f"unique tokens: {len(unique_tokens)}")
    return unique_tokens

def check_len_txt(input_file):
    """Check the length of a text file"""
    line_count = 0
    for line in open(input_file, "r"):
        if line != "\n":
            line_count += 1
    file.close()

    print(line_count)
    
def rem_html(input_file, output_file):
    """Removes html tags from txt file"""
    output_file = open(output_file, 'wt')
    with open(input_file, 'r') as file:
        for line in file:
            line = re.sub(r"\<style>(.*?)\</style>", ' ', line)
            line = re.sub(r"\<(?:[^<>])*\>", ' ', line)
            output_file.write(line)
    print("done")

def replace_all(text, dic):
    splitters = {'>': ' ', '<': ' '}
    for i, j in splitters.items():
        text = text.replace(i, j)
    return text


def multiple_replace(dictionary, text):
    """Creates a regular expression  from dictionaryary keys"""
    regex = re.compile("(%s)" % "|".join(map(re.escape, dictionary.keys())))
    # For each match, look-up corresponding value in dictionaryary
    String = lambda mo: dictionary[mo.string[mo.start():mo.end()]]
    return regex.sub(String, text)

def split_captions(input_file, output_file):
    '''Split out captions from txt file of tables and save to a new file'''
    fout = open(output_file, "wt")

    with open(input_file) as file:
        line_count = 0
        for line in tqdm(file):
            caption = re.search(r"(?<=\<h4>)(.*?)(?=\</h4>)", line).group()
            fout.write(caption + "\n")
            line_count += 1
        print(line_count)
