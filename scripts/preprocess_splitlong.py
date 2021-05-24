import re

fin = open("../data/text_files/alltables.txt", "rt")
fout = open("../data/text_files/outalltables.txt", "wt")

splitters = {'>': ' > ', '<': ' < '}

def replace_all(text, dic):
	for i, j in splitters.items():
		text = text.replace(i, j)
	return text

for line in fin:
	fout.write(replace_all(line, splitters))

fin.close()
fout.close()

