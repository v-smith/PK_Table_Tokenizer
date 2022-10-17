import fileinput

with open(file='../data/alltablesNotest.txt', encoding='w') as fout, fileinput.input(['../data/textfiles/A-BpmctablesNotest.txt', '../data/textfiles/C-HpmctablesNotest.txt', '../data/textfiles/I-NpmctablesNotest.txt', '../data/textfiles/O-ZpmctablesNotest.txt']) as fin:
    for line in fin:
        fout.write(line)
