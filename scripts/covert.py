from pathlib import Path
import ujson

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


all_tables = [x['html'].replace("\n", "#n#") for x in read_jsonl(file_path="all_pmcs/O-Zpmctables.jsonl")]

with open('text_files/mergedtablesO-Z.txt', 'w') as f:
    for item in all_tables:
        f.write("%s\n" % item)

a = 1
