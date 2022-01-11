from tokenizers import Tokenizer

my_tokens = ['/td', '/tr', '/th', '/bold', '/italic', '/sup', '/xref', '/h4', '/head', '/table', '/body', '/html', '/tbody',
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

tokenizer = Tokenizer.from_file("../data/tokenizers/tokenizerPKtablesSpecialTokens5000.json")

tokenizer.add_tokens(my_tokens)

#tokenizer.save("../data/tokenizers/tokenizeralltablesNotestHtml10000.json")

#encoded = tokenizer.encode("!DOCTYPE html  html  body  h4 Population pharmacokinetic parameter estimates for the typical individual after administration of "
                           #"cladribine as; an infusion, orally or subcutaneously. The relative standards")

encoded = tokenizer.encode("""td align="left" (RSE%) /td  /tr  /thead  tbody  tr  td align="left" Clearance (L/h) /td  " \
                             "td align="left" 39.3 /td  td align="left" (4.9) /td  td align="left" 54""")


#encoded = tokenizer.encode("""<td align="left">(RSE%)<sup>1</sup></td><td align="left">Estimate %</td><td align="left">
#(RSE%)</td></tr></thead><tbody><tr><td align="left">Clearance (L/h)</td><td align="left">39.3</td><td align="left">""")

#encoded = tokenizer.encode("""<!DOCTYPE html><html><body><h4>Population pharmacokinetic parameter estimates for the typical individual after administration
                                #of cladribine as; an infusion, orally or subcutaneously. The relative standards""")
print(encoded.tokens)
print(encoded.ids)



