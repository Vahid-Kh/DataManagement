"""

This script:
    1 - Downloads any file format from HTML by searching for 'href' in the HTML code
    2 - in this example the goal is to find all PDF files

    Hint: The BeautifulSoup request is used in a way to search for CSV & works as long as the link
    contains the CSV file with the specified data

"""
# pip install PyPDF2 - > Read and parse your content pdf
# pip install requests - > request for get the pdf
# pip install bs4 - > for parse the html and find all url hrf with ".pdf" final
from PyPDF2 import PdfFileReader
import requests
import io
from bs4 import BeautifulSoup


# url = requests.get('https://www.lens.org/lens/patent/090-512-860-922-464')
url = requests.get("https://patents.google.com/patent/US20100186833?oq=4+way+valve")

soup = BeautifulSoup(url.content,"lxml")
# print(soup)
for a in soup.find_all('a', href=True):
    mystr= a['href']
    if(mystr[-4:]=='.pdf'):
        print("url with pdf final:", a['href'])
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
            """Here the metadata of your pdf"""
            # print(txt)
            """numpage for the number page"""
            for i in range(number_of_pages):
                page = pdf.getPage(i)
                page_content = page.extractText()
                """print the content in the page 20"""
                print(page_content)


for script in soup(["script", "style"]):
    script.decompose()
strips = list(soup.stripped_strings)

# print(strips)