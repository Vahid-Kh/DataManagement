
import textract

from Archive import funcTxtAnlytcs as ff
from Archive.funcTxtAnlytcs import pdfparser

#Write a for-loop to open many files (leave a comment if you'd like to learn how).
# filename = 'Data/technology-radar-vol-22-en.pdf'
filename = "Data/larsen2020.pdf"

fileurl = filename
#open allows you to read the file.

"""OLD METHOD: DOES NOT WORK IN ALL SITUATIONS  """
"""
pdfFileObj = open(filename, 'rb')
# The pdfReader variable is a readable object that will be parsed.
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# Discerning the number of pages will allow us to parse through all the pages.
num_pages = pdfReader.numPages
count = 0
text = ""
# The while loop will read each page.
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()
"""

text = pdfparser(filename)

if text == "":
    text = textract.process("Data/US_10247455_B2.pdf")

print(text)
#Now we have a text variable that contains all the text derived from our PDF file. Type print(text) to see what it contains. It likely contains a lot of spaces, possibly junk such as '\n,' etc.
#Now, we will clean our text variable and return it as a list of keywords.
#The word_tokenize() function will break our text phrases into individual words.
# tokens = word_tokenize(text)

"""  To get rid of integers   """
# text = ''.join([i for i in text if not i.isdigit() or (i=='2' and text[-1]=='O') ])
text = ''.join([i for i in text if not i.isdigit()])
# text = ''.join([i for i in text if not i.isdigit() or i=='2' or i=='3' ])

tokens = text.split()

#We'll create a new list that contains punctuation we wish to clean.
punctuations = ['(',')',';',':','[',']',',','™','/','.']
#We initialize the stopwords variable, which is a list of words like "The," "I," "and," etc. that don't hold much value as keywords.

#We create a list comprehension that only returns a list of words that are NOT IN stop_words and NOT IN punctuations.
wanted =['cascade', 'ammonia', 'CO', 'learning']
keywords = [word for word in tokens if not word in ff.stopwords and not word in punctuations]

match = [word for word in tokens if word in wanted]
# print(match)
dictionary = ff.wordListToFreqDict(keywords)
sorteddict = ff.sortFreqDict(dictionary)

for s in sorteddict:
    # if s[0] >= 3:
        print(str(s))
dictionary = ff.wordListToFreqDict(match)
sorteddict = ff.sortFreqDict(dictionary)

for s in sorteddict: print(str(s))


