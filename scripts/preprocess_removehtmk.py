import re

def rem_html(input_file, output_file):
    output_file = open(output_file, 'wt')
    with open(input_file, 'r') as file:
        for line in file:
            line = re.sub(r"\<style>(.*?)\</style>", ' ', line)
            line = re.sub(r"\<(?:[^<>])*\>", ' ', line)
            output_file.write(line)

    print("done")


rem_html("../data/textfiles/text.txt", "../data/out.txt")
