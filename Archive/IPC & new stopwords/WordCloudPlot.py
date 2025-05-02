# Python program to generate WordCloud

from wordcloud import WordCloud, STOPWORDS
from func_add_IPC_codes import add_IPC_description
import matplotlib.pyplot as plt
import pandas as pd
import funcFrqStpWrd as ff
""" SELECT FILE :::  """
"""----------------------------------------------"""
""" Can only take lower case """
fileName = r"PatentMoistureDirtAcidReclaimRecoveryPurger.csv"
# fileName = r"Step2.csv"
"""----------------------------------------------"""
""" SELECT COLUMN TO SEARCH :::  """
"""----------------------------------------------"""
""" The column to read from """
#colName = "IPC Description"
colName = "Title"
# colName = "Abstract"
# colName = "Keywords"
"""----------------------------------------------"""
""" SELECT SEARCH WORD :::   %LOWER CASE ONLY % """
""" Can only take lower case """
"""----------------------------------------------"""
searchWord = 'fuel cell'
# searchWord = 'purger'
"""----------------------------------------------"""

searchOutpt = []
valList = []

comment_words = ''
stopwords = set(STOPWORDS)
lt = []

""" TO PRINT FULL DATAFRAME   """
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.options.display.max_colwidth = 100
""" Iterate through the csv file  """
df = pd.read_csv("Data/Raw Data/" + fileName , encoding="latin-1")

## add ipc descriptions
df = add_IPC_description(df, 4)

# for val in df.Abstract:
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
        """OLD search method; replaced cause it could only take single word for searching"""
        # if tokens[i] == searchWord:
            # print(val, print(df.loc[df[colName] == val], sep='\n'))
            # searchOutpt.append(df.loc[df[colName] == val])
            # dfsearch = dfsearch.append(df.loc[df[colName] == val])
            # valList.append(val)

        lt.append(tokens[i])
    comment_words += " ".join(tokens) + " "

#We'll create a new list that contains punctuation we wish to clean.
punctuations = ['(',')',';',':','[',']',',','™','/','.']
#We initialize the stopwords variable, which is a list of words like "The," "I," "and," etc. that don't hold much value as keywords.

#We create a list comprehension that only returns a list of words that are NOT IN stop_words and NOT IN punctuations.
wanted =['cascade', 'ammonia', 'CO', 'learning']
keywords = [word for word in lt if not word in ff.stopwords and not word in punctuations]
# print(keywords)
match = [word for word in lt if word in wanted]
# print(match)
dictionary = ff.wordListToFreqDict(keywords)
sorteddict = ff.sortFreqDict(dictionary)

for s in sorteddict:
    if s[0] >= 3:
        print(str(s))

dictionary = ff.wordListToFreqDict(match)
sorteddict = ff.sortFreqDict(dictionary)
# for s in sorteddict: print(str(s))


print(dfsearch)

# # plot the WordCloud image
wordcloud = WordCloud(width=5000, height=3000, background_color='white', stopwords=ff.stopwords,
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

data = pd.DataFrame(dfsearch)
data.to_excel("Data/" + fileName[0:-4] + searchWord + "Output.xlsx")

plt.show()
