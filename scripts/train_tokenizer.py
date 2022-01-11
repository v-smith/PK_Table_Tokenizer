from tokenizers import SentencePieceBPETokenizer

'''
#tokens without < > 
html_tokens = ['/td', '/tr', '/th', '/bold', '/italic', '/sup', '/xref', '/h4', '/head', '/table', '/body', '/html', '/tbody',
             '/thead', '/sub', '/p', '/mml:mo', '/mml:mi', '/mml:mrow', '/mml:mn', '/mml:math', '/inline-formula', '/ext-link',
             '/colgroup', '/list-item', '/tex-math', '/alternatives', '/underline', '/named-content', '/mml:msub', '/list', '/mml:mtext',
             '/mml:msup', '/monospace', '/mml:msubsup', '/sc', '/label', '/mml:mover', '/mml:mfrac', '/mml:mstyle', '/styled-content', '/mml:mfenced',
             '/mml:mtd', '/mml:mtr', '/abbrev', '/mml:munder', '/uri', '/mml:mtable', '/disp-formula', '/mml:semantics', '/mml:msqrt', '/sans-serif',
             '/mml:munderover', '/alt-text', '/inline-graphic', '/mml:annotation', '/mml:mpadded', '/tfoot', '/private-char', '/strike', '/mml:mmultiscripts',
             '/overline', '/chem-struct', '/preformat', '/email', '/roman', '/x', '/glyph-data', '/mml:menclose', '/chem-struct-wrap', '/graphic',
             '/mml:mroot', '/code', '/disp-quote', '/title', '/mml:mphantom', '/copyright-holder', '/permissions', '/disp-formula-group', '/', '/fig',
             '/funding-source', '/tb', '/= 1% vs.', 'td', 'tr', 'th', 'bold', 'italic', 'sup', 'xref', 'h4', 'head', 'table', 'body', 'html', 'tbody',
             'thead', 'sub', 'p', 'mml:mo', 'mml:mi', 'mml:mrow', 'mml:mn', 'mml:math', 'inline-formula', 'ext-link', 'colgroup', 'list-item', 'tex-math',
             'alternatives', 'underline', 'named-content', 'mml:msub', 'list', 'mml:mtext', 'mml:msup', 'monospace', 'mml:msubsup', 'sc', 'label', 'mml:mover',
             'mml:mfrac', 'mml:mstyle', 'styled-content', 'mml:mfenced', 'mml:mtd', 'mml:mtr', 'abbrev', 'mml:munder', 'uri', 'mml:mtable', 'disp-formula',
             'mml:semantics', 'mml:msqrt', 'sans-serif', 'mml:munderover', 'alt-text', 'inline-graphic', 'mml:annotation', 'mml:mpadded', 'tfoot',
             'private-char', 'strike', 'mml:mmultiscripts', 'overline', 'chem-struct_preformat', 'email', 'roman', 'x', 'glyph-data', 'mml:menclose',
             'chem-struct-wrap', 'graphic', 'mml:mroot', 'code', 'disp-quote', 'title', 'mml:mphantom', 'copyright-holder', 'permissions', 'disp-formula-group',
             'fig', 'funding-source', 'tb', '= 1% vs.', '!DOCTYPE', """ align="left" """]
'''
#html tokens in full
html_tokens= ['<h1>', '</h1>', '</td>', '</tr>', '</th>', '</bold>', '</italic>', '</sup>', '</xref>', '</h4>', '</head>', '</table>', '</body>', '</html>', '</tbody>', '</thead>', '</sub>', '</p>', '</mml:mo>', '</mml:mi>', '</mml:mrow>', '</mml:mn>', '</mml:math>', '</inline-formula>', '</ext-link>', '</colgroup>', '</list-item>', '</tex-math>', '</alternatives>', '</underline>', '</named-content>', '</mml:msub>', '</list>', '</mml:mtext>', '</mml:msup>', '</monospace>', '</mml:msubsup>', '</sc>', '</label>', '</mml:mover>', '</mml:mfrac>', '</mml:mstyle>', '</styled-content>', '</mml:mfenced>', '</mml:mtd>', '</mml:mtr>', '</abbrev>', '</mml:munder>', '</uri>', '</mml:mtable>', '</disp-formula>', '</mml:semantics>', '</mml:msqrt>', '</sans-serif>', '</mml:munderover>', '</alt-text>', '</inline-graphic>', '</mml:annotation>', '</mml:mpadded>', '</tfoot>', '</private-char>', '</strike>', '</mml:mmultiscripts>', '</overline>', '</chem-struct>', '</preformat>', '</email>', '</roman>', '</x>', '</glyph-data>', '</mml:menclose>', '</chem-struct-wrap>', '</graphic>', '</mml:mroot>', '</code>', '</disp-quote>', '</title>', '</mml:mphantom>', '</copyright-holder>', '</permissions>', '</disp-formula-group>', '</>', '</fig>', '</funding-source>', '</tb>', '</= 1% vs.>', '<td>', '<tr>', '<th>', '<bold>', '<italic>', '<sup>', '<xref>', '<h4>', '<head>', '<table>', '<body>', '<html>', '<tbody>', '<thead>', '<sub>', '<p>', '<mml:mo>', '<mml:mi>', '<mml:mrow>', '<mml:mn>', '<mml:math>', '<inline-formula>', '<ext-link>', '<colgroup>', '<list-item>', '<tex-math>', '<alternatives>', '<underline>', '<named-content>', '<mml:msub>', '<list>', '<mml:mtext>', '<mml:msup>', '<monospace>', '<mml:msubsup>', '<sc>', '<label>', '<mml:mover>', '<mml:mfrac>', '<mml:mstyle>', '<styled-content>', '<mml:mfenced>', '<mml:mtd>', '<mml:mtr>', '<abbrev>', '<mml:munder>', '<uri>', '<mml:mtable>', '<disp-formula>', '<mml:semantics>', '<mml:msqrt>', '<sans-serif>', '<mml:munderover>', '<alt-text>', '<inline-graphic>', '<mml:annotation>', '<mml:mpadded>', '<tfoot>', '<private-char>', '<strike>', '<mml:mmultiscripts>', '<overline>', '<chem-struct_preformat>', '<email>', '<roman>', '<x>', '<glyph-data>', '<mml:menclose>', '<chem-struct-wrap>', '<graphic>', '<mml:mroot>', '<code>', '<disp-quote>', '<title>', '<mml:mphantom>', '<copyright-holder>', '<permissions>', '<disp-formula-group>', '<fig>', '<funding-source>', '<tb>', '<= 1% vs.>', '<!DOCTYPE html>', '<align="left">', '<td align="left">', '<td align="left" colspan="5">']

tokenizer = SentencePieceBPETokenizer()
tokenizer.add_special_tokens(html_tokens)
tokenizer.train("../data/textfiles/PKtablesNotest_nohtml.txt", vocab_size=3000, min_frequency=2)

tokenizer.save("../data/tokenizers/tokenizerPKtablesSpecialTokens3000.json")

example = "<!DOCTYPE html><html><body><h4>Demographics and disease characteristics of the subject who received at " \
          "least one dose of obinutuzumab</h4><head><style> table, th, td {border: 1px solid " \
          "black;}</style></head><body><table xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" " \
          "xmlns:xlink=\"http://www.w3.org/1999/xlink\" frame=\"hsides\" rules=\"groups\"><thead><tr><th " \
          "align=\"left\">Variable</th><th align=\"left\">CLL (<italic>n</italic> = 12)</th><th align=\"left\">DLBCL " \
          "(<italic>n</italic> = 23)</th><th align=\"left\">FL (<italic>n</italic> = 13)</th><th " \
          "align=\"left\">Overall (<italic>n</italic> = 48)</th></tr></thead><tbody><tr><td align=\"left\" " \
          "colspan=\"5\">Age at baseline (years)</td></tr><tr><td align=\"left\"> Mean (sd)</td><td " \
          "align=\"left\">60.7 (12.0)</td><td align=\"left\">53.3 (15.8)</td><td align=\"left\">55.1 (8.8)</td><td " \
          "align=\"left\">55.6 (13.4)</td></tr><tr><td align=\"left\" colspan=\"5\">Gender [<italic>n</italic> (" \
          "%)]</td></tr><tr><td align=\"left\"> Male</td><td align=\"left\">7 (58.3)</td><td align=\"left\">11 (" \
          "47.8)</td><td align=\"left\">8 (61.5)</td><td align=\"left\">26 (54.2)</td></tr><tr><td align=\"left\"> " \
          "Female</td><td align=\"left\">5 (41.7)</td><td align=\"left\">12 (52.2)</td><td align=\"left\">5 (" \
          "38.5)</td><td align=\"left\">22 (45.8)</td></tr><tr><td align=\"left\" colspan=\"5\">Weight (" \
          "kg)</td></tr><tr><td align=\"left\"> Mean (sd)</td><td align=\"left\">60.83 (11.44)</td><td " \
          "align=\"left\">62.33 (9.86)</td><td align=\"left\">64.27 (12.49)</td><td align=\"left\">62.48 (" \
          "10.85)</td></tr><tr><td align=\"left\" colspan=\"5\">Height (cm)</td></tr><tr><td align=\"left\"> Mean (" \
          "sd)</td><td align=\"left\">161.0 (5.0)</td><td align=\"left\">164.1 (7.1)</td><td align=\"left\">166.3 (" \
          "10.7)</td><td align=\"left\">163.9 (7.9)</td></tr><tr><td align=\"left\" colspan=\"5\">ECOG at baseline [" \
          "<italic>n</italic> (%)]</td></tr><tr><td align=\"left\"> 0</td><td align=\"left\">2 (16.7)</td><td " \
          "align=\"left\">8 (34.8)</td><td align=\"left\">8 (61.5)</td><td align=\"left\">18 (37.5)</td></tr><tr><td " \
          "align=\"left\"> 1</td><td align=\"left\">10 (83.3)</td><td align=\"left\">15 (65.2)</td><td " \
          "align=\"left\">5 (38.5)</td><td align=\"left\">30 (62.5)</td></tr><tr><td align=\"left\" colspan=\"5\">Ann " \
          "Arbor stage at diagnosis<sup>a</sup> [<italic>n</italic> (%)]</td></tr><tr><td align=\"left\"> I</td><td " \
          "align=\"left\">N/A</td><td align=\"left\">0</td><td align=\"left\">2 (15.4)</td><td align=\"left\">2 (" \
          "5.6)</td></tr><tr><td align=\"left\"> II</td><td align=\"left\">N/A</td><td align=\"left\">4 (" \
          "17.4)</td><td align=\"left\">0</td><td align=\"left\">4 (11.1)</td></tr><tr><td align=\"left\"> " \
          "III</td><td align=\"left\">N/A</td><td align=\"left\">8 (34.8)</td><td align=\"left\">5 (38.5)</td><td " \
          "align=\"left\">13 (36.1)</td></tr><tr><td align=\"left\"> IV</td><td align=\"left\">N/A</td><td " \
          "align=\"left\">7 (30.4)</td><td align=\"left\">3 (23.1)</td><td align=\"left\">10 (27.8)</td></tr><tr><td " \
          "align=\"left\"> Missing</td><td align=\"left\">N/A</td><td align=\"left\">4 (17.4)</td><td " \
          "align=\"left\">3 (23.1)</td><td align=\"left\">7 (19.4)</td></tr><tr><td align=\"left\" " \
          "colspan=\"5\">Binet stage<sup>a</sup> [<italic>n</italic> (%)]</td></tr><tr><td align=\"left\"> Stage " \
          "A</td><td align=\"left\">1 (8.3)</td><td align=\"left\">N/A</td><td align=\"left\">N/A</td><td " \
          "align=\"left\">1 (8.3)</td></tr><tr><td align=\"left\"> Stage B</td><td align=\"left\">6 (50.0)</td><td " \
          "align=\"left\">N/A</td><td align=\"left\">N/A</td><td align=\"left\">6 (50.0)</td></tr><tr><td " \
          "align=\"left\"> Stage C</td><td align=\"left\">2 (16.7)</td><td align=\"left\">N/A</td><td " \
          "align=\"left\">N/A</td><td align=\"left\">2 (16.7)</td></tr><tr><td align=\"left\"> Unknown</td><td " \
          "align=\"left\">3 (25.0)</td><td align=\"left\">N/A</td><td align=\"left\">N/A</td><td align=\"left\">3 (" \
          "25.0)</td></tr><tr><td align=\"left\" colspan=\"5\">Number of previous lines of treatment</td></tr><tr><td " \
          "align=\"left\"> Median</td><td align=\"left\">2.0</td><td align=\"left\">2.0</td><td " \
          "align=\"left\">3.0</td><td align=\"left\">2.0</td></tr><tr><td align=\"left\"> Minimum–maximum</td><td " \
          "align=\"left\">1–7</td><td align=\"left\">1–11</td><td align=\"left\">1–6</td><td " \
          "align=\"left\">1–11</td></tr><tr><td align=\"left\" colspan=\"5\">Best response of prior treatment [" \
          "<italic>n</italic> (%)]</td></tr><tr><td align=\"left\"> CR</td><td align=\"left\">1 (8.3)</td><td " \
          "align=\"left\">9 (39.1)</td><td align=\"left\">2 (15.4)</td><td align=\"left\">12 (25.0)</td></tr><tr><td " \
          "align=\"left\"> PR</td><td align=\"left\">8 (66.7)</td><td align=\"left\">9 (39.1)</td><td " \
          "align=\"left\">7 (53.8)</td><td align=\"left\">24 (50.0)</td></tr><tr><td align=\"left\"> SD</td><td " \
          "align=\"left\">1 (8.3)</td><td align=\"left\">2 (8.7)</td><td align=\"left\">0</td><td align=\"left\">3 (" \
          "6.3)</td></tr><tr><td align=\"left\"> PD</td><td align=\"left\">0</td><td align=\"left\">2 (8.7)</td><td " \
          "align=\"left\">0</td><td align=\"left\">2 (4.2)</td></tr><tr><td align=\"left\"> Missing</td><td " \
          "align=\"left\">2 (16.7)</td><td align=\"left\">1 (4.3)</td><td align=\"left\">4 (30.8)</td><td " \
          "align=\"left\">7 (14.6)</td></tr><tr><td align=\"left\" colspan=\"5\">Duration of best " \
          "response</td></tr><tr><td align=\"left\"> <italic>n</italic></td><td align=\"left\">6</td><td " \
          "align=\"left\">18</td><td align=\"left\">7</td><td align=\"left\">31</td></tr><tr><td align=\"left\"> Mean " \
          "(sd) (days)</td><td align=\"left\">355.2 (604.2)</td><td align=\"left\">152.5 (119.2)</td><td " \
          "align=\"left\">159.4 (136.4)</td><td align=\"left\">193.3 (281.3)</td></tr></tbody></table></body></html> "
example = example.replace("\n", "#n#")
output = tokenizer.encode(example)

for x in output.tokens:
    print(x)



