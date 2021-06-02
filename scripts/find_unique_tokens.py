import re
from collections import Counter
import pandas as pd

file = open("../data/textfiles/text.txt", "r")

tokens = []
for line in file:
    line_tokens = re.findall(r"\</(?:[^<>])*\>", line, flags=re.VERBOSE) #r"\<(?:[^<>])*\>"  #r"(?<=\<)(.*?)(?=\>)" #r"\<.*?\>"
    tokens.extend(line_tokens)

frequencies = Counter(tokens).most_common()
#pd.DataFrame(frequencies).to_csv("../data/allNotestresults.csv")
unique_tokens = list(set(tokens))

#with open("../data/textfiles/html_tokens.txt", "w") as output:
    #output.write(str(unique_tokens))

print(unique_tokens)
print(f"unique tokens: {len(unique_tokens)}")

# line_tokens2 = re.findall(r"\{(?:[^{}])*\}", line) #r"\{(.*?)\}"
# tokens2.extend(line_tokens2)
#tokens= ["<" + token + ">" for token in tokens]
#tokens2= ["{" + token + "}" for token in tokens2]
#tokens.extend(tokens2)
