"""

This script:
    1 - Takes batch of image with name format : " r"page_" + str(i) + ".jpg" " & turns the text
    2 - The text is then checked for possible spelling errors
    3 - The right spelled text is then returned

    Hint: none

"""


import pytesseract as tess
tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from PIL import Image
from spellchecker import SpellChecker

# img = Image.open("2020-12-28 15_37_10-Data Scrape – TryTesseract.py.png")
for i in range(1,100):
    print(i)
    try:
        img = Image.open(r"page_" + str(i) + ".jpg")
    except:
        break
    text = tess.image_to_string(img)
    # print(text)
    """Spellchecker """


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


