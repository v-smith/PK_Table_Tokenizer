import re

splitters = {'>': ' ', '<': ' '}

def replace_all(text, dic):
	for i, j in splitters.items():
		text = text.replace(i, j)
	return text

fout = open("../data/textfiles/outtext.txt", "wt")

with open(input_file) as file:
	for line in file:
		line = re.sub(r"\<style>(.*?)\</style>", ' ', line)
		line = replace_all(line, splitters)
		fout.write(line)

