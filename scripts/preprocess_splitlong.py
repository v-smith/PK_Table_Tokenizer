import re
from pk_tokenizer.utils import replace_all

fout = open("../data/textfiles/outtext.txt", "wt")

with open(input_file) as file:
	for line in file:
		line = re.sub(r"\<style>(.*?)\</style>", ' ', line)
		line = replace_all(line, splitters)
		fout.write(line)

