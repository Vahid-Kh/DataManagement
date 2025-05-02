"""

This script:
    1 - Takes an image & turns the text
    2 - The text is then checked for possible spelling errors
    3 - The right spelled text is then returned

    Hint: none

"""


import pytesseract as tess
"""https://github.com/UB-Mannheim/tesseract/wiki"""
tess.pytesseract.tesseract_cmd = r"C:\Users\u375297\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
from PIL import Image
from spellchecker import SpellChecker

# img = Image.open("2020-12-28 15_37_10-Data Scrape – TryTesseract.py.png")


img = Image.open(r"Data/Image/2022-01-13 15_35_34-Miro.png")
text = tess.image_to_string(img)

print(text)
#
# text = """
#
#
#
#
# """


"""Spellchecker """

print(text.replace("\n", "-"))
spell = SpellChecker()

"""
# find those words that may be misspelled
# misspelled = spell.unknown(['something', 'is', 'hapenning', 'here'])
"""
splitText = text.split()
misspelled = spell.unknown(splitText)
rightSpelled = " "
for word in splitText:
    if spell.correction(word) == word:
        rightSpelled += word
    else:
        rightSpelled += spell.correction(word)
    rightSpelled += " "

rightSpelled = rightSpelled.replace(" - ", "-")
print(rightSpelled)


