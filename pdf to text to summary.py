from PyPDF2 import PdfFileReader
from pathlib import Path

pdf = PdfFileReader('SheekarBanerjee.pdf')

page1object = pdf.getPage(0)
page1text = page1object.extractText()
print(page1text)
