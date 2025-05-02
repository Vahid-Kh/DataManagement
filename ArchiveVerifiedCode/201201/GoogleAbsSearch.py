# Python program to generate WordCloud

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
from Archive import funcTxtAnlytcs as ff
from Archive.funcTxtAnlytcs import abstrctExtrct
""" SELECT FILE :::  """
"""----------------------------------------------"""
""" Can only take lower case """

fileName = r"PatentMoistureDirtAcidReclaimRecoveryPurger.csv"
# fileName = r"ArticleMoistureAcidDirtPurgerRetention.csv"
# fileName = r"PatentMoistureRemovalLow-ppmHumidityRequirementsAbsorb.csv"

"""----------------------------------------------"""
""" SELECT COLUMN TO SEARCH :::  """
"""----------------------------------------------"""
""" The column to read from """
colName = "Title"
# colName = "Abstract"
# colName = "Keywords"
"""----------------------------------------------"""
""" SELECT SEARCH WORD :::   %LOWER CASE ONLY % """
""" Can only take lower case """
"""----------------------------------------------"""
searchWord = 'fuel cell'
# searchWord = 'purger'v
# searchWord = 'spray drier'
# searchWord = 'retention'
# searchWord = 'organic compound'
# searchWord = 'vacuum'
# searchWord = ' '
wanted =['cascade', 'ammonia', 'CO', 'learning']
"""----------------------------------------------"""

searchOutpt = []
valList = []

comment_words = ''
stopwords = set(STOPWORDS)
lt = []

""" TO PRINT FULL DATAFRAME   """
# pd.set_option("display.max_rows", None, "display.max_columns", None)
# pd.options.display.max_colwidth = 100

print('fileName   : ',fileName)
print('searchWord : ',searchWord)
""" Iterate through the csv file  """
df = pd.read_csv("Data/Raw Data/"  + fileName , encoding="latin-1")
""" Empty dataframe for search"""
dfsearch = pd.DataFrame(columns = df.columns)

for val in df[colName]:
    # typecaste each val to string
    val = str(val)
    if searchWord in val.lower():
        dfsearch = dfsearch.append(df.loc[df[colName] == val])

    # split the value
    tokens = val.split()

    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
        lt.append(tokens[i])

        """OLD search method; replaced cause it could only take single word for searching"""
        # if tokens[i] == searchWord:
            # print(val, print(df.loc[df[colName] == val], sep='\n'))
            # searchOutpt.append(df.loc[df[colName] == val])
            # dfsearch = dfsearch.append(df.loc[df[colName] == val])
            # valList.append(val)

    comment_words += " ".join(tokens) + " "

#We'll create a new list that contains punctuation we wish to clean.
punctuations = ['(',')',';',':','[',']',',','™','/','.']
#We initialize the stopwords variable, which is a list of words like "The," "I," "and," etc. that don't hold much value as keywords.

#We create a list comprehension that only returns a list of words that are NOT IN stop_words and NOT IN punctuations.

keywords = [word for word in lt if not word in ff.stopwords and not word in punctuations]
# print(keywords)
# match = [word for word in lt if word in wanted]
# print(match)
dictionary = ff.wordListToFreqDict(keywords)
sorteddict = ff.sortFreqDict(dictionary)

for s in sorteddict:
    if s[0] >= 3:
        print(str(s))

# dictionary = ff.wordListToFreqDict(match)
# sorteddict = ff.sortFreqDict(dictionary)
# for s in sorteddict: print(str(s))

""" THIS EXTRACTS THE ABSTRACT FROM GOOGLE BY RECEIVING PUBLICATION NUMBER"""
print(dfsearch["Publication Number"])
abstract = [abstrctExtrct(num) for num in dfsearch["Publication Number"].tolist()]
dfsearch = dfsearch.assign(abstract=abstract)

# # plot the WordCloud image
wordcloud = WordCloud(width=2500, height=1500, background_color='white', stopwords=ff.stopwords,
                      prefer_horizontal=1, min_font_size=10).generate(comment_words)

plt.figure('General wordcloud', figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
""" Saves the figure as SVG format """
# figName = "Data/" + fileName[0:-4] + colName + ".svg"
# plt.savefig(figName, dpi=None, format="svg",)
figName = "Data/" + fileName[0:-4] + colName + ".pdf"
plt.savefig(figName, dpi=500, format="pdf",)
print(dfsearch.columns)
# data = pd.DataFrame(dfsearch)
data = pd.DataFrame(dfsearch[['Publication Number','Title','Inventors', 'Owners (US)', 'URL', 'Publication Year']])
data['IP Abstract'] = abstract
data.to_excel("Data/Search Result/" + fileName[0:-4] + searchWord + "Output.xlsx")

plt.show()
