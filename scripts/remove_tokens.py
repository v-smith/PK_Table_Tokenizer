import re

unique_tokens= ['<thead>',
 '<td align="left" valign="top" rowspan="1" colspan="1"/>',
 '<style>',
 '</head>',
 '</html>',
 '<h4>',
 '<!DOCTYPE html>',
 '</body>',
 '</h4>',
 '</style>',
 '</tr>',
 '<head>',
 '<td align="char" char="." valign="top" rowspan="1" colspan="1">',
 '<body>',
 '<td align="left" valign="bottom" rowspan="1" colspan="1">',
 '<tr>',
 '</table>',
 '<td align="left" valign="top" rowspan="1" colspan="1">',
 '</thead>',
 '<table xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:mml="http://www.w3.org/1998/Math/MathML" frame="hsides" rules="groups">',
 '<td align="left" valign="bottom" rowspan="1" colspan="1"/>',
 '</td>',
 '</tbody>',
 '<html>',
 '<tbody>']


fin = open("../data/text_files/alltables.txt", "rt")
fout = open("../data/text_files/nohtmlalltables.txt", "wt")

for line in fin:
    fout.write(re.sub(r'<(.*?)>', '', line))

fin.close()
fout.close()
