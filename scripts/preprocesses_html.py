import re

#find unique tags

fin = open("../data/text_files/alltables.txt", "rt")
#fout = open("../data/text_files/uniquetokens.txt", "wt")

for line in fin:
    tokens= []
    line_tokens = re.findall(r'<(.*?)>', line)
    tokens+= line_tokens

unique_tokens = set(tokens)
unique_tokens = str(list(unique_tokens))
print(unique_tokens)

#fout.write(unique_tokens)

fin.close()
#fout.close()

