import pandas as pd
from bs4 import BeautifulSoup
from pk_tokenizer.utils import get_tags

input_html = "../data/textfiles/text.txt"

def test_bs_parser(input_html):
    unique_tags = get_tags(input_html)
    assert  unique_tags == ['td', 'h4', 'mml:math', 'table', 'html', 'mml:mo', 'style', 'mml:mrow', 'tr', 'th', 'mml:msub', 'mml:mtext', 'xref', 'alternatives', 'mml:mi', 'thead', 'tbody', 'mml:mn', 'mml:mover', 'italic', 'mml:msup', 'inline-formula', 'inline-graphic', 'body', 'tex-math']
    assert len(unique_tags) == 25
