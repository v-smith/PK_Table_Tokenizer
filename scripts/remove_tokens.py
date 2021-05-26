import re

fin = open("../data/text_files/alltables.txt", "rt")
fout = open("../data/text_files/nohtmlalltables.txt", "wt")

for line in fin:
    fout.write(re.sub(r'<(.*?)>', '', line))

fin.close()
fout.close()

fin = open("../data/text_files/alltables.txt", "rt")
fout = open("../data/text_files/nohtmlalltables.txt", "wt")
