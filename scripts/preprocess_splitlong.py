import re

fin = open("../data/textfiles/alltablesNotest.txt", "rt")
fout = open("../data/textfiles/outtext.txt", "wt")

splitters = {'>': ' ', '<': ' '}

def replace_all(text, dic):
	for i, j in splitters.items():
		text = text.replace(i, j)
	return text

for line in fin:
	line = replace_all(line, splitters)
	line = re.sub(r"\{.*?\}", " ", line)
	fout.write(line)

fin.close()
fout.close()

