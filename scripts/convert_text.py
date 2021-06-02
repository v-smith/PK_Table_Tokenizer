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


def write_to_text(input_json, out_file):
    all_tables = [x['html'].replace("\n", "#n#") for x in read_jsonl(file_path=input_json)]

    with open(out_file, 'w') as f:
        for item in all_tables:
            f.write("%s\n" % item)

    print("done")

write_to_text("../data/json/test_removed/A-BpmctablesNotest.jsonl", "../data/textfiles/A-BpmctablesNotest.txt")
write_to_text("../data/json/test_removed/C-HpmctablesNotest.jsonl", "../data/textfiles/C-HpmctablesNotest.txt")
write_to_text("../data/json/test_removed/I-NpmctablesNotest.jsonl", "../data/textfiles/I-NpmctablesNotest.txt")
write_to_text("../data/json/test_removed/O-ZpmctablesNotest.jsonl", "../data/textfiles/O-ZpmctablesNotest.txt")

