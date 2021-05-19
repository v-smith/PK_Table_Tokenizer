import fileinput

with open('../PycharmProjects/Tokenizer/data/alltables.txt', 'w') as fout, fileinput.input(['text_files/mergedtablesA-B.txt', 'text_files/mergedtablesC-H.txt', 'text_files/mergedtablesI-N.txt', 'text_files/mergedtablesO-Z.txt']) as fin:
    for line in fin:
        fout.write(line)
