#utf-8
""" # funcTxtAnlytcs.py

This library contains multiple functions performing followins:
- Removing Stop wordts from a text
- Removing tags, signs and all non-alphanumeric
- Makes a dictionary of a list of words and returns the frequency
- Parses a PDF into list
- Gets the IP number and downloads the abstract from Google and translates it into English
-
"""

import numpy as np
import pandas as pd
import matplotlib as plt
from wordcloud import WordCloud
codec = 'utf-8'

stopwords = ['The', 'a', 'about', 'above', 'across', 'after', 'afterwards',
             'again', 'against', 'all', 'almost', 'alone', 'along',
             'already', 'also', 'although', 'always', 'am', 'among',
             'amongst', 'amoungst', 'amount', 'an', 'and', 'another',
             'any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere',
             'are', 'around', 'as', 'at', 'back', 'be', 'became',
             'because', 'become', 'becomes', 'becoming', 'been',
             'before', 'beforehand', 'behind', 'being', 'below',
             'beside', 'besides', 'between', 'beyond', 'bill', 'both',
             'bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant',
             'co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de',
             'describe', 'detail', 'did', 'do', 'done', 'down', 'due',
             'during', 'each', 'eg', 'eight', 'either', 'eleven', 'else',
             'elsewhere', 'empty', 'enough', 'etc', 'even', 'ever',
             'every', 'everyone', 'everything', 'everywhere', 'except',
             'few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first',
             'five', 'for', 'former', 'formerly', 'forty', 'found',
             'four', 'from', 'front', 'full', 'further', 'get', 'give',
             'go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her',
             'here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers',
             'herself', 'him', 'himself', 'his', 'how', 'however',
             'hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed',
             'interest', 'into', 'is', 'it', 'its', 'itself', 'keep',
             'last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made',
             'many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine',
             'more', 'moreover', 'most', 'mostly', 'move', 'much',
             'must', 'my', 'myself', 'name', 'namely', 'neither', 'never',
             'nevertheless', 'next', 'nine', 'no', 'nobody', 'none',
             'noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of',
             'off', 'often', 'on', 'once', 'one', 'only', 'onto', 'or',
             'other', 'others', 'otherwise', 'our', 'ours', 'ourselves',
             'out', 'over', 'own', 'part', 'per', 'perhaps', 'please',
             'put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed',
             'seeming', 'seems', 'serious', 'several', 'she', 'should',
             'show', 'side', 'since', 'sincere', 'six', 'sixty', 'so',
             'some', 'somehow', 'someone', 'something', 'sometime',
             'sometimes', 'somewhere', 'still', 'such', 'system', 'take',
             'ten', 'than', 'that', 'the', 'their', 'them', 'themselves',
             'then', 'thence', 'there', 'thereafter', 'thereby',
             'therefore', 'therein', 'thereupon', 'these', 'they',
             'thick', 'thin', 'third', 'this', 'those', 'though', 'three',
             'three', 'through', 'throughout', 'thru', 'thus', 'to',
             'together', 'too', 'top', 'toward', 'towards', 'twelve',
             'twenty', 'two', 'un', 'under', 'until', 'up', 'upon',
             'us', 'very', 'via', 'was', 'we', 'well', 'were', 'what',
             'whatever', 'when', 'whence', 'whenever', 'where',
             'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon',
             'wherever', 'whether', 'which', 'while', 'whither', 'who',
             'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with',
             'within', 'without', 'would', 'yet', 'you', 'your', 'thereof',
             'yours', 'yourself', 'yourselves','according', 'therefor', '<-', '/,,',
             '->', '),', '(−)', '©', '|', '/.,', '/.', '.-', '-,', ').',
             '//','(',')',';',':','[',']',',','™','/','.', 'method', 'device',
             'apparatus', 'used', 'using', 'based', 'use', 'tested', 'observed',
             'experiment', 'shown', 'various', 'abstract', 'nan', 'Nan', 'NaN',
             'pubchem cid', 'pubchem', 'cid', 'ga', 'water', 'air', '&',
             'preparing', 'preparation', 'title', '.', 'jp', 'æ',
             'ø', 'å', "\ " ," \ " , '', '', '', '', '', '', '', '', '', '',
             '', '', '', '', '', '', '', '', '', '', '', '', '',]




def rec_ave(n, xold, x, x10):
    return xold + 1 / n * (x - x10)


def is_nan(x):
    return (x is np.nan or x != x)


def mov_ave(a, n=30):
    mlt_mov_ave = a[0:n]
    x_old = sum(mlt_mov_ave) / n
    for i in range(n, len(a)):
        x_new = rec_ave(n, x_old, a[i], a[i - n])
        mlt_mov_ave.append(x_new)
        x_old = x_new

    return mlt_mov_ave

def stripTags(pageContents):
    pageContents = str(pageContents)
    startLoc = pageContents.find("<p>")
    endLoc = pageContents.rfind("<br/>")
    pageContents = pageContents[startLoc:endLoc]

    inside = 0
    text = ''

    for char in pageContents:
        if char == '<':
            inside = 1
        elif (inside == 1 and char == '>'):
            inside = 0
        elif inside == 1:
            continue
        else:
            text += char

    return text


def printtext(text):
    return text


# Given a text string, remove all non-alphanumeric
# characters (using Unicode definition of alphanumeric).


def stripNonAlphaNum(text):
    import re
    return re.compile(r'\W+', re.UNICODE).split(text)


# Given a list of words, return a dictionary of
# word-frequency pairs.


def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist, wordfreq)))


def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux


def removeStopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]


from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io


def pdfparser(data):
    """ Parses a PDF into list """

    fp = open(data, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        data =  retstr.getvalue()

    return data


def pdfTextCount(filename):

    from Archive.funcTxtAnlytcs import pdfparser
    text = pdfparser(filename)
    """  To get rid of integers   """
    # text = ''.join([i for i in text if not i.isdigit() or (i=='2' and text[-1]=='O') ])
    text = ''.join([i for i in text if not i.isdigit()])
    tokens = text.split()
    punctuations = ['(', ')', ';', ':', '[', ']', ',', '™', '/', '.']
    keywords = [word for word in tokens if not word in ff.stopwords and not word in punctuations]
    dictionary = ff.wordListToFreqDict(keywords)
    sorteddict = ff.sortFreqDict(dictionary)
    for s in sorteddict:
        # if s[0] >= 3:
        print(str(s))

def abstrctExtrct(patent_1):
    """- Gets the IP number and gets the abstract from Google and translates it into English"""

    from google_patent_scraper import scraper_class
    from googletrans import Translator
    # ~ Initialize scraper class ~ #
    patent_1 = patent_1.strip()
    patent_1 = patent_1.replace(" ", "")
    try:
        scraper=scraper_class()

        # ~ Add patents to list ~ #
        scraper.add_patents(patent_1)

        # ~ Scrape all patents ~ #
        scraper.scrape_all_patents()

        # ~ Get results of scrape ~ #
        patent_1_parsed = scraper.parsed_patents[patent_1]

        translator = Translator()
        return translator.translate(patent_1_parsed['abstract_text']).text
    except:
        return " "


IPC_codes = pd.read_csv(r'C:\Users\u375297\OneDrive - Danfoss\Documents - RAC Tech Center - Programming Projects\Python Projects\Data management\\IPC_table.xlsx').drop(columns=['Unnamed: 0'], axis=1)


def add_IPC_description(df, N):
    columnIPC = pd.DataFrame(df["IPCR Classifications"])
    columnIPC = columnIPC["IPCR Classifications"].str.split(';;', expand=True).add_prefix('code_')

    for i in columnIPC.columns:
        columnIPC[i] = columnIPC[i].astype(str).str[:N]
    for i in columnIPC.index:
        columnIPC.loc[i,:] = columnIPC.loc[i,:].drop_duplicates(keep='first')

    s = IPC_codes.set_index('code')['description']
    columnIPC = columnIPC.replace(s)
    columnIPC = columnIPC.fillna(value='')
    columnIPC['IPC Description'] = columnIPC[columnIPC.columns[0:]].apply(
        lambda x: ';'.join(x.dropna().astype(str)),
        axis=1
    )

    df['IPC Description'] = columnIPC['IPC Description']
    print('Descriptions added!')

    return df

def wordCloud(string):
    wordcloud = WordCloud(width=10000, height=7000, background_color='white', stopwords=stopwords,
                          prefer_horizontal=1, min_font_size=10).generate(string)

    plt.figure('General wordcloud', figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)

