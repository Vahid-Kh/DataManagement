# Python program to generate WordCloud

from wordcloud import STOPWORDS
import pandas as pd
from Archive import funcTxtAnlytcs as ff

"""----------------------------------------------"""
""" SELECT COLUMN TO SEARCH :::  """
"""----------------------------------------------"""
""" The column to read from """
colName = "Title"
# colName = "Abstract"
# colName = "Keywords"
"""----------------------------------------------"""

"""----------------------------------------------"""
""" Can only take lower case """
"""----------------------------------------------"""
""" SELECT FILE :::  """
"""----------------------------------------------"""
""" SELECT SEARCH WORD :::   %LOWER CASE ONLY % """
""" Can only take lower case """
"""----------------------------------------------"""
# fileName = r"ArticleCooling20172020.csv"
# searchWord = 'geothermal refrigeration'
# searchWord = 'nanorefrigerant '
# searchWord = 'refrigerated storage'
# searchWord = 'cascade refrigeration'
# searchWord = 'microstructure'
"""----------------------------------------------"""
# fileName = r"ArticleAirConditioning20172020.csv"
# searchWord = 'fuel cell'
# searchWord = 'energy storage'
# searchWord = 'demand response'
# searchWord = 'solar'
# searchWord = 'electric vehicle'
# searchWord = 'change material'
# searchWord = 'sensor'
"""----------------------------------------------"""
fileName = r"ArticleRefrigeration20172020.csv"
# searchWord = 'low grade'
searchWord = 'organic rankine'
# searchWord = 'falling film'
# searchWord = 'solar'
# searchWord = 'cold storage'
# searchWord = 'change material'
# searchWord = 'adsorption refrigeration'
# searchWord = 'absorption refrigeration'
# searchWord = 'ejector refrigeration'
# searchWord = 'geothermal'
# searchWord = 'cold chain'
# searchWord = 'thermoelectric'
# searchWord = 'ejector'
# searchWord = 'cascade'
"""----------------------------------------------"""
# fileName = r"ArticleHeatPump20172020.csv"
# searchWord = 'assisted heat'
# searchWord = 'thermal storage'
# searchWord = 'ground coupled'
# searchWord = 'renewable'
# searchWord = 'pv'
# searchWord = 'storage tank'
# searchWord = 'phase change'
# searchWord = 'geothermal heat'
# searchWord = 'solar assisted'
# searchWord = 'dual source'
# searchWord = 'liquid desiccant'
# searchWord = 'electric vehicle'
# searchWord = 'energy storage'
"""----------------------------------------------"""
# fileName = r""
# searchWord = ''
# searchWord = ''
# searchWord = ''
# searchWord = ''
# searchWord = ''
"""----------------------------------------------"""

searchOutpt = []
valList = []

comment_words = ''
stopwords = set(STOPWORDS)
lt = []

""" TO PRINT FULL DATAFRAME   """
# pd.set_option("display.max_rows", None, "display.max_columns", None)
# pd.options.display.max_colwidth = 100
""" Iterate through the csv file  """
df = pd.read_csv("Data/Raw Data/" + fileName , encoding="latin-1")
""" Empty dataframe for search"""
dfsearch = pd.DataFrame(columns = df.columns)

print('fileName   : ',fileName)
print('searchWord : ',searchWord)

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

dictionary = ff.wordListToFreqDict(keywords)
sorteddict = ff.sortFreqDict(dictionary)

# print(dfsearch.columns)
data = pd.DataFrame(dfsearch[['Title','Abstract','DOI', 'Publication Year']])
# print(data['Title'])
print("Number of matched papers " ,len(data['Title']))
data.to_excel("Data/Search Result/" + fileName[0:-4] + searchWord + "Output.xlsx")

# plt.show()










