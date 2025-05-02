"""
This one is one of my favorite :D
This script:
    1 - Takes a link that contains ".pdf" format in its HTML code & turns the text
    2 - The text is then printed

    Hint: It is also possible to correct the spelling error at the bottom

"""

# You need install :
# pip install PyPDF2 - > Read and parse your content pdf
# pip install requests - > request for get the pdf
# pip install bs4 - > for parse the html and find all url hrf with ".pdf" final
from PyPDF2 import PdfFileReader
import requests
import io
from bs4 import BeautifulSoup
from spellchecker import SpellChecker
spell = SpellChecker()

# url = requests.get('https://www.freepatentsonline.com/y2013/0029477.html')
url = requests.get("https://patents.google.com/patent/US20100186833?oq=4+way+valve")

soup = BeautifulSoup(url.content,"lxml")

for a in soup.find_all('a', href=True):
    mystr= a['href']
    if(mystr[-4:]=='.pdf'):
        print ("url with pdf final:", a['href'])
        urlpdf = a['href']
        response = requests.get(urlpdf)
        with io.BytesIO(response.content) as f:
            pdf = PdfFileReader(f)

            information = pdf.getDocumentInfo()
            number_of_pages = pdf.getNumPages()
            txt = f"""
            Author: {information.author}
            Creator: {information.creator}
            Producer: {information.producer}
            Subject: {information.subject}
            Title: {information.title}
            Number of pages: {number_of_pages}
            """
            # Here the metadata of your pdf
            print(txt)
            # numpage for the number page
            numpage=6
            page = pdf.getPage(numpage)
            page_content = page.extractText()
            # print the content in the page 20
            print(page_content)

            """ To correct spelling error  """
            # splitText = page_content.split()
            # misspelled = spell.unknown(splitText)
            # rightSpelled = " "
            # for word in splitText:
            #     if spell.correction(word) == word:
            #         rightSpelled += word
            #     else:
            #         rightSpelled += spell.correction(word)
            #     rightSpelled += " "
            #
            # rightSpelled = rightSpelled.replace(" - ", "-")
            # print(rightSpelled)
