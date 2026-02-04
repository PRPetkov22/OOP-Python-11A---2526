from pdf import PDF
from html import HTML
from txt import TXT

n = int(input())

for _ in range(n):
    data = input().split(maxsplit=1)
    doc_type = data[0]
    text = data[1] if len(data) > 1 else ""

    if doc_type == "PDF":
        doc = PDF()
    elif doc_type == "HTML":
        doc = HTML()
    elif doc_type == "TXT":
        doc = TXT()

    print(doc.export(text))